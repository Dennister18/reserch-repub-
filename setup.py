from setuptools import setup, find_packages

setup(
    name="osint-research",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "duckduckgo-search>=3.9.0",
        "python-whois>=0.8.0",
        "dnspython>=2.4.0",
        "validators>=0.22.0",
    ],
    entry_points={
        "console_scripts": [
            "osint-research=src.main:main",
        ],
    },
    author="Dennister18",
    description="OSINT-инструмент",
    python_requires=">=3.8",
)
