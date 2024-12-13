from setuptools import setup, find_packages

setup(
    name="dependency-visualizer",  # Название пакета
    version="1.0.0",  # Версия пакета
    description="A tool to visualize Maven package dependencies in Mermaid format",  # Краткое описание
    long_description=open("README.md").read(),  # Подробное описание из README.md
    long_description_content_type="text/markdown",  # Формат README
    author="Your Name",  # Ваше имя
    author_email="your.email@example.com",  # Ваш email
    url="https://github.com/your-repo/dependency-visualizer",  # Ссылка на проект (например, GitHub)
    packages=find_packages("src"),  # Поиск всех пакетов в каталоге src
    package_dir={"": "src"},  # Указание корневой директории
    install_requires=[
        "requests>=2.20.0",  # Указание зависимостей (например, requests)
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",  # Поддерживаемые версии Python
        "License :: OSI Approved :: MIT License",  # Лицензия
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Минимальная версия Python
    entry_points={
        "console_scripts": [
            "dependency-visualizer=src.main:main",  # Создание команды в CLI
        ],
    },
    include_package_data=True,  # Включение дополнительных данных из MANIFEST.in
    keywords="maven dependencies visualization mermaid",
    license="MIT",  # Лицензия проекта
)
