# setup.py

from setuptools import setup, find_packages

setup(
    name='capital_city_river_finder',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'langchain_openai',  # Ensure this is the correct package name
        # Add other dependencies as needed
    ],
)