# My Python Application

A robust Python application demonstrating CI/CD best practices with Jenkins.

## Features

- Performs mathematical calculations.
- Packaged as a standalone executable using PyInstaller.
- Full CI/CD pipeline with testing, security scanning, and packaging.

## Local Development

### Prerequisites

- Python 3.11+
- pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/my-python-app.git
    cd my-python-app
    ```

2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt -r requirements-dev.txt
    ```

### Running the Application

```bash
python -m sources.calc