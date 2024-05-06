from setuptools import setup, find_packages

setup(
    name='easy_typecheck',
    version='0.1.0',
    packages=find_packages(),
    description='A Python package for runtime type checking of function arguments and return values that works for modern Python versions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='HP',
    url='https://github.com/HP2706/easy_typecheck',
    license='MIT',
    install_requires=[
        'typing; python_version<"3.5"',
        'inspect',
        'asyncio; python_version<"3.7"'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)