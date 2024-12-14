import pytest
from src.parser import ConfigParser
from xml.etree.ElementTree import tostring, fromstring


def test_full_config():
    content = """{
        key = [[value]];
        array = (list [[item1]] [[item2]]);
        [[42]] -> answer;
    }"""
    parser = ConfigParser()
    xml_root = parser.parse_config(content)
    xml_str = tostring(xml_root, encoding="unicode")

    # Проверяем корректность структуры XML
    expected = fromstring("""
    <config>
        <item>{"key": "value", "array": ["item1", "item2"]}</item>
    </config>
    """)
    assert fromstring(xml_str).tag == expected.tag
    assert len(fromstring(xml_str)) == len(expected)
