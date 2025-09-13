import pytest
from sources.helpers import parse_args, calculate

def test_parse_args_valid():
    args = ['add', '5', '3']
    result = parse_args(args)
    assert result == {'operation': 'add', 'x': 5.0, 'y': 3.0}

def test_parse_args_invalid_length():
    with pytest.raises(ValueError, match="Usage:"):
        parse_args(['add', '5'])

def test_parse_args_non_numeric():
    with pytest.raises(ValueError, match="must be numbers"):
        parse_args(['add', '5', 'abc'])

def test_calculate_operations():
    assert calculate('add', 5, 3) == 8
    assert calculate('subtract', 5, 3) == 2
    assert calculate('multiply', 5, 3) == 15
    assert calculate('divide', 6, 3) == 2

def test_calculate_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        calculate('power', 2, 3)