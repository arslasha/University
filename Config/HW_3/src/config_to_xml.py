import argparse
import re
import xml.etree.ElementTree as ET

def parse_config(content):
    """Парсинг конфигурационного файла и конвертация в XML."""
    constants = {}  # Словарь для хранения определенных констант

    def parse_value(value):
        """
        Разбор значения строки, включая числа, строки, списки, словари и выражения с константами.
        """
        value = value.strip()
        if value.isdigit():  # Целое число
            return int(value)
        elif re.match(r"^\d+\.\d+$", value):  # Число с плавающей точкой
            return float(value)
        elif value.startswith("[[") and value.endswith("]]"):  # Строка в формате [[...]]
            return value[2:-2]
        elif value.startswith("(list") and value.endswith(")"):  # Список значений
            items = re.findall(r"\[\[.*?\]\]|\d+|\d+\.\d+", value[5:-1])
            return [parse_value(item) for item in items]
        elif value.startswith("{") and value.endswith("}"):  # Вложенный словарь
            return parse_dict(value[1:-1])
        elif re.search(r"\|.*?\|", value):  # Выражение с константами
            return evaluate_expression(value)
        else:
            raise ValueError(f"Invalid value: {value}")

    def evaluate_expression(expression):
        """
        Разбор и вычисление выражений, содержащих константы и арифметические операции.
        Например: |mass| * |acceleration|.
        """
        # Заменяем константы в выражении их значениями из словаря
        def replace_constant(match):
            const_name = match.group(1)
            if const_name in constants:
                return str(constants[const_name])
            raise ValueError(f"Undefined constant: {const_name}")

        # Шаблон для поиска констант между символами |...|
        expression = re.sub(r"\|(\w+)\|", replace_constant, expression)

        try:
            # Безопасное вычисление арифметического выражения
            return eval(expression, {"__builtins__": None}, {})
        except Exception as e:
            raise ValueError(f"Invalid arithmetic expression: {expression}. Error: {e}")

    def parse_dict(content):
        """
        Разбор словаря вида:
        key1 = value1;
        key2 = { ... };
        """
        result = {}
        buffer = ""
        nesting = 0

        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue

            if nesting == 0:
                if line.endswith("{"):  # Начало вложенного словаря
                    nesting += 1
                    buffer = line[:-1].strip() + " "
                else:  # Простой ключ-значение
                    match = re.match(r"(\w+)\s*=\s*(.+);", line)
                    if not match:
                        raise ValueError(f"Invalid dictionary entry: {line}")
                    key, value = match.groups()
                    result[key.strip()] = parse_value(value.strip())
            else:  # Вложенный словарь
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
        """
        Разбор строк, содержащих определения переменных и констант.
        Например: 10 -> mass.
        """
        if line.startswith("!"):  # Строка комментария
            return None
        if "->" in line:  # Определение константы
            value, name = map(str.strip, line.split("->"))
            constants[name] = parse_value(value)
            return None
        return line

    xml_root = ET.Element("config")
    buffer = []
    in_dict = False

    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("!"):  # Пропускаем пустые строки и комментарии
            continue
        if line == "{":  # Начало словаря
            in_dict = True
            buffer = []
        elif line == "}":  # Конец словаря
            in_dict = False
            dict_content = "\n".join(buffer)
            parsed_dict = parse_dict(dict_content)
            ET.SubElement(xml_root, "item").text = str(parsed_dict)
            buffer = []
        elif in_dict:  # Добавляем строки внутрь словаря
            buffer.append(line)
        else:  # Обрабатываем строки с константами
            parsed = parse_line(line)
            if parsed is not None:
                ET.SubElement(xml_root, "item").text = str(parsed)

    return xml_root

def config_to_xml(file_path):
    """
    Чтение файла конфигурации и конвертация его в XML.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        xml_root = parse_config(content)
        return ET.tostring(xml_root, encoding="unicode", method="xml")
    except ValueError as e:
        print(f"Error: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""

def main():
    """Основная функция для запуска скрипта."""
    parser = argparse.ArgumentParser(description="Convert config to XML.")
    parser.add_argument("file", help="Path to the config file.")
    args = parser.parse_args()

    xml_output = config_to_xml(args.file)
    if xml_output:
        print(xml_output)

if __name__ == "__main__":
    main()
