from setuptools import setup, find_packages

setup(
    name="config_to_xml",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={"test": ["pytest"]},
    entry_points={
        "console_scripts": [
            "config_to_xml=src.config_to_xml:main",
        ]
    },
    python_requires=">=3.8",
)
