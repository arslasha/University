import argparse
import re
import xml.etree.ElementTree as ET

def parse_config(content):
    constants = {}

    def parse_value(value):
        value = value.strip()
        if value.isdigit():
            return int(value)
        elif value.startswith("[[") and value.endswith("]]"):
            return value[2:-2]
        elif value.startswith("(list") and value.endswith(")"):
            items = re.findall(r"\[\[.*?\]\]|\d+", value[5:-1])
            return [parse_value(item) for item in items]
        elif value.startswith("{") and value.endswith("}"):
            return parse_dict(value[1:-1])
        elif value.startswith("|") and value.endswith("|"):
            name = value[1:-1]
            if name in constants:
                return constants[name]
            raise ValueError(f"Undefined constant: {name}")
        else:
            raise ValueError(f"Invalid value: {value}")

    def parse_dict(content):
        result = {}
        # Allow parsing nested dictionaries
        buffer = ""
        nesting = 0
        for char in content:
            if char == "{" and nesting == 0:
                nesting += 1
                buffer += char
            elif char == "{" and nesting > 0:
                nesting += 1
                buffer += char
            elif char == "}" and nesting > 1:
                nesting -= 1
                buffer += char
            elif char == "}" and nesting == 1:
                nesting -= 1
                buffer += char
                key, value = re.match(r"(\w+) *= *(.*);", buffer.strip()).groups()
                result[key.strip()] = parse_value(value.strip())
                buffer = ""
            elif nesting > 0:
                buffer += char
            elif char == ";":
                key, value = re.match(r"(\w+) *= *(.*);", buffer.strip()).groups()
                result[key.strip()] = parse_value(value.strip())
                buffer = ""
            else:
                buffer += char
        if buffer:
            raise ValueError(f"Invalid dictionary content: {buffer}")
        return result

    def parse_line(line):
        if line.startswith("!"):
            return None  # Это строка комментария
        if "->" in line:
            value, name = map(str.strip, line.split("->"))
            constants[name] = parse_value(value)
            return None
        return line

    xml_root = ET.Element("config")
    buffer = []
    in_dict = False

    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("!"):
            continue
        if line == "{":
            in_dict = True
            buffer = []
        elif line == "}":
            in_dict = False
            dict_content = " ".join(buffer)
            parsed_dict = parse_dict(dict_content)
            ET.SubElement(xml_root, "item").text = str(parsed_dict)
            buffer = []
        elif in_dict:
            buffer.append(line)
        else:
            parsed = parse_line(line)
            if parsed is not None:
                ET.SubElement(xml_root, "item").text = str(parsed)

    return xml_root

def config_to_xml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        xml_root = parse_config(content)
        return ET.tostring(xml_root, encoding="unicode", method="xml")
    except SyntaxError as e:
        print(e)
        return ""

def main():
    parser = argparse.ArgumentParser(description="Convert config to XML.")
    parser.add_argument("file", help="Path to the config file.")

    args = parser.parse_args()
    xml_output = config_to_xml(args.file)
    if xml_output:
        print(xml_output)

if __name__ == "__main__":
    main()