import re
import xml.etree.ElementTree as ET

class ConfigParser:
    def __init__(self):
        self.constants = {}

    def parse_value(self, value):
        if value.isdigit():
            return int(value)
        elif value.startswith("[[") and value.endswith("]]"):
            return value[2:-2]
        elif value.startswith("(list") and value.endswith(")"):
            items = value[5:-1].split()
            return [self.parse_value(item) for item in items]
        elif value.startswith("{") and value.endswith("}"):
            items = re.findall(r"(\\w+) *= *([^;]+);", value)
            return {key: self.parse_value(val) for key, val in items}
        elif value.startswith("|") and value.endswith("|"):
            name = value[1:-1]
            if name in self.constants:
                return self.constants[name]
            raise ValueError(f"Undefined constant: {name}")
        else:
            raise ValueError(f"Invalid value: {value}")

    def parse_line(self, line):
        if line.startswith("!"):
            return None  # Comment line
        if "->" in line:
            value, name = map(str.strip, line.split("->"))
            self.constants[name] = self.parse_value(value)
            return None
        return self.parse_value(line)

    def parse_config(self, content):
        xml_root = ET.Element("config")
        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                parsed = self.parse_line(line)
                if parsed is not None:
                    ET.SubElement(xml_root, "item").text = str(parsed)
            except ValueError as e:
                raise SyntaxError(f"Error parsing line: '{line}': {e}")
        return xml_root
