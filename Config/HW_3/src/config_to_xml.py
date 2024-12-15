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
        buffer = ""
        nesting = 0

        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue

            if nesting == 0:
                if line.endswith("{"):
                    nesting += 1
                    buffer += line[:-1].strip() + " "
                else:
                    key, value = re.match(r"(\w+) *= *(.*);", line).groups()
                    result[key.strip()] = parse_value(value.strip())
            else:
                if line == "}":
                    nesting -= 1
                    result[buffer.strip()] = parse_dict("\n".join(buffer.splitlines()[1:]))
                    buffer = ""
                else:
                    buffer += line + "\n"

        if buffer:
            raise ValueError(f"Unclosed dictionary or invalid syntax in: {buffer}")

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
            dict_content = "\n".join(buffer)
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
