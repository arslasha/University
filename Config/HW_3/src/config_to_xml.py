import re
import sys
import argparse
import xml.etree.ElementTree as ET


class ConfigParser:
    def __init__(self, content):
        self.content = content
        self.data = {}
        self.variables = {}

    def parse(self):
        # Удаляем комментарии
        content_no_comments = re.sub(r'!.*', '', self.content)

        # Парсим списки
        list_matches = re.findall(
            r'\(list\s+([\s\S]+?)\)', content_no_comments)
        for list_match in list_matches:
            items = re.findall(r'\[\[(.*?)\]\]', list_match)
            for i in range(0, len(items), 2):
                if i + 1 < len(items):
                    key, value = items[i], items[i + 1]
                    self.variables[key] = value

        # Парсим блоки и присваивания
        block_match = re.search(r'\{([\s\S]+?)\}', content_no_comments)
        if block_match:
            block_content = block_match.group(1)
            for line in block_content.split(';'):
                line = line.strip()
                if line:
                    self._parse_line(line)

        # Выполняем арифметические операции
        self._resolve_math_expressions()

    def _parse_line(self, line):
        # Пример: host = [[localhost]]
        key_value_match = re.match(r'(\w+)\s*=\s*(.+)', line)
        if key_value_match:
            key, value = key_value_match.groups()
            if '[[[' in value and ']]]' in value:
                value = re.search(r'\[\[\[(.*?)\]\]\]', value).group(1)
            elif '[[' in value and ']]' in value:
                value = re.search(r'\[\[(.*?)\]\]', value).group(1)
            elif '{' in value and '}' in value:
                nested_parser = ConfigParser(value)
                nested_parser.parse()
                value = nested_parser.data
            self.variables[key] = value

    def _resolve_math_expressions(self):
        # Пример: force = |mass| * |acceleration|
        for key, value in list(self.variables.items()):
            if isinstance(value, str) and re.search(r'\|.*?\|', value):
                resolved_value = value
                for var in re.findall(r'\|(.*?)\|', value):
                    if var in self.variables:
                        resolved_value = resolved_value.replace(
                            f'|{var}|', str(self.variables[var]))
                try:
                    self.variables[key] = eval(resolved_value)
                except Exception as e:
                    print(f"Ошибка вычисления для {key}: {e}")

    def to_xml(self):
        root = ET.Element('config')
        for key, value in self.variables.items():
            item = ET.SubElement(root, 'item')  # создаем простой тег <item>
            # формат текста: "ключ : значение"
            item.text = f"{key} : {value}"
        return ET.tostring(root, encoding='unicode')


def main():
    # Парсим аргументы командной строки
    parser = argparse.ArgumentParser(
        description="Учебный конфигурационный язык -> XML")
    parser.add_argument("file", help="Путь к входному файлу конфигурации")
    args = parser.parse_args()

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
            config_parser = ConfigParser(content)
            config_parser.parse()
            xml_output = config_parser.to_xml()
            print(xml_output)
    except FileNotFoundError:
        print(f"Ошибка: файл {args.file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()