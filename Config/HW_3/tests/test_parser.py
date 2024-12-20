import pytest
from src.parser import ConfigParser

def test_parse_constants():
    parser = ConfigParser()
    parser.parse_line("[[42]] -> answer;")
    assert parser.constants["answer"] == "42"

def test_parse_list():
    parser = ConfigParser()
    result = parser.parse_value("(list [[item1]] [[item2]] [[item3]])")
    assert result == ["item1", "item2", "item3"]

def test_parse_dictionary():
    parser = ConfigParser()
    result = parser.parse_value("{key1 = [[value1]]; key2 = [[value2]];}")
    assert result == {"key1": "value1", "key2": "value2"}

def test_undefined_constant():
    parser = ConfigParser()
    with pytest.raises(ValueError):
        parser.parse_value("|undefined|")
