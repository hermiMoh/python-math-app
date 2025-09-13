pipeline {
    agent {
        docker {
            image 'python:3.11-slim-bookworm' // Pin a specific, stable version
            args '--user 1000:1000' // Run as non-root for security
            reuseNode true
        }
    }
    environment {
        // Define all configuration here for easy management
        VENV_DIR = "${env.WORKSPACE}/venv"
        PYTHON = "${VENV_DIR}/bin/python"
        PIP = "${VENV_DIR}/bin/pip"
        UNIT_TEST_REPORT = 'test-reports/results.xml'
        SECURITY_SCAN_DIR = 'security-reports'
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10')) // Keep only last 10 builds
        timeout(time: 15, unit: 'MINUTES') // Fail build if it hangs
        disableConcurrentBuilds() // Prevent race conditions
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checks out the code from Git
            }
        }
        stage('Build & Install') {
            steps {
                sh '''
                    # Create a clean virtual environment
                    python -m venv ${VENV_DIR}
                    # Upgrade pip inside the venv
                    ${PIP} install --upgrade pip setuptools wheel
                    # Install project dependencies from requirements.txt
                    ${PIP} install -r requirements.txt
                '''
            }
        }
stage('Test') {
    steps {
        sh """
            # Install test-specific dependencies
            ${PIP} install pytest pytest-cov
            # Run tests with coverage, output JUnit XML for reporting
            ${PYTHON} -m pytest --junitxml=${UNIT_TEST_REPORT} --cov=sources/ --cov-report=term tests/
        """
    }
    post {
        always {
            junit "${UNIT_TEST_REPORT}" // This will still give you basic test reporting
            // Simple console output of test results
            script {
                echo "Test results available in JUnit format"
                echo "Coverage report shown in console above"
            }
        }
    }
}
        stage('Security Scan') {
    steps {
        sh """
            # Install safety for vulnerability scanning
            ${PIP} install safety
            # Scan dependencies, output to file and console
            mkdir -p ${SECURITY_SCAN_DIR}
            safety check -r requirements.txt --full-report --output ${SECURITY_SCAN_DIR}/safety_report.txt || true
        """
    }
    post {
        always {
            // Archive the security report as a build artifact
            archiveArtifacts artifacts: "${SECURITY_SCAN_DIR}/safety_report.txt", fingerprint: true
            
            // Simple security gate - fail build on critical vulnerabilities
            script {
                def report = readFile("${SECURITY_SCAN_DIR}/safety_report.txt")
                if (report.contains("CRITICAL") && !report.contains("No known security vulnerabilities found")) {
                    error("Critical security vulnerabilities found! Build failed.")
                }
            }
        }
    }
}
        stage('Package') {
            steps {
                sh """
                    # Install pyinstaller inside the venv
                    ${PIP} install pyinstaller
                    # Create the standalone executable
                    ${PYTHON} -m PyInstaller --onefile --name my-python-app sources/calc.py
                """
            }
        }
        stage('Archive Artifact') {
            steps {
                // Archive the final executable
                archiveArtifacts artifacts: 'dist/my-python-app', fingerprint: true
            }
        }
        stage('Deliver to Staging') {
            steps {
                echo "Simulating deployment of ${env.BUILD_ID} to staging environment..."
                // In a real scenario, this would be:
                // - scp dist/my-python-app user@staging-server:/app/
                // - ssh user@staging-server "systemctl restart my-python-service"
                sleep 30 // Simulate a deployment process
            }
        }
    }
    post {
        always {
            echo "Build #${env.BUILD_ID} - ${currentBuild.currentResult}."
            cleanWs() // Clean up the workspace to save disk space
        }
        success {
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "The build is successful. Please check at ${env.BUILD_URL}",
                to: "devops-team@yourcompany.com"
            )
        }
        failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "The build has failed. Please check at ${env.BUILD_URL}",
                to: "devops-team@yourcompany.com"
            )
        }
    }
}