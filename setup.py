from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'manager',
    version = '0.1.0',
    author = 'David Moya',
    author_email = 'davidmoyalopez@outlook.es',
    license = 'Apache',
    description = 'service manage tools',
    long_description = long_description,
    # long_description_content_type = "text/markdown",
    url = 'https://github.com/davidmoyalopez/python-manager.git',
    # py_modules = ['openvpn'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Linux",
    ],
    entry_points ={
        'console_scripts':
        ['manager=manager:main'],
    }
)
