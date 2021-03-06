from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="croissantsapi",
    version="1.0.0",
    description="Coolest API in the world",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SocgenGoToCloud/CroissantsAPI",
    author="Sygmei",
    author_email="admin@sygmei.io",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="cool api",
    packages=find_packages(),
    install_requires=["fastapi", "sqlalchemy", "psycopg2-binary", "uvicorn"],
    extras_require={
        "tests": ["tox", "flake8"],
        "production": ["hypercorn", "uvloop", "httptools"],
    },
    entry_points={
        "console_scripts": [
            "croissants_configure_db=croissantsapi.database.models:configure_database",
            "croissants_populate_db=croissantsapi.database.populate:populate",
        ]
    },
    project_urls={
        "Bug Reports": "https://github.com/SocgenGoToCloud/CroissantsAPI/issues",
        "Source": "https://github.com/SocgenGoToCloud/CroissantsAPI",
    },
)
