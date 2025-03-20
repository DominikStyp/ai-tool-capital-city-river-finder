# AI Tool based on ChatGTP to find the river of the capital city by prompt

## Getting started

### Prerequisites
First make sure you have proper API secret key set up:
```
cp .env.example .env
```
Then open `.env` file and set `API_SECRET_KEY` to your secret key.
<br />
Secret key can be found in the [API Keys setting](https://platform.openai.com/api-keys).

Make sure you have Python 3.10 installed, then install following packages:
```
pip3 install langchain python-dotenv pytest
```
Install the current package:
```
pip3 install .
```

### How to run tests
```
pytest tests/test_capital_city_river_finder.py
```

### Example usage
`find_capital_river_example.py` has the usage example
