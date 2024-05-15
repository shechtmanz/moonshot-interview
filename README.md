
# Overview
This CLI application asks for a website url and checks whether it is likely legally safe to scrape it.
Currently, it conducts the following checks
* Checks that theres is no prohibitive values in the returned HTML header robots metadata tag (e.g. noindex, nofollow)
* Asks ChatGPT 

## Setup
Create a file .env with 
```
OPENAI_API_KEY = '<Your OpenAI key>
```

Make sure you purchased credit points in open ai.

Install Selenium webdriver. Follow [this link](https://www.geeksforgeeks.org/how-to-install-selenium-on-macos/) instructions

## run the tests
```
python -m pytest -v
```

## Run the application
```
python main.py
```