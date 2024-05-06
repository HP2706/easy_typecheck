from setuptools import setup, find_packages

setup(
    name='easy_typecheck',
    version='0.1.0',
    description='a type-checking function decorator for modern python',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'typing; python_version<"3.8"',
        'asyncio; python_version<"3.8"'
        'typing-extensions; python_version<"3.8"'
    ],
)