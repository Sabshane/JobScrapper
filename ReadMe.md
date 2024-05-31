# JobUp.ch Scraper

This repository contains a Python script to scrape job listings from [JobUp.ch](https://www.jobup.ch/), a popular job search website. The script collects job links, locations, work rates, contract types, and company names, and stores them in a CSV file. It's more meant to be a test repository to practice scraping data with python.

## Features

- Scrapes job listings from all available pages on JobUp.ch
- Collects detailed job information including:
  - Job link
  - Location
  - Work rate (part-time/full-time)
  - Contract type (permanent/temporary)
  - Company name
- Saves the data into a CSV file for easy analysis
- Uses a progress bar to indicate the scraping progress

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup4` library
- `tqdm` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 tqdm
```
## Usage

1) Clone this repository to your local machine:

```bash
git clone https://github.com/Sabshane/JobScrapper.git
cd JobScrapper
```

2) Run the script

```bash
python scrap.py
```

## How it works
1) __Initialize:__ The script starts by determining the total number of pages of job listings available on JobUp.ch.
2) __Session Setup:__ A session is created with a user-agent header to simulate an incognito browser.
3) __Scraping Loop:__ The script iterates through each page, extracts job links, and collects detailed job information.
4) __Save Data:__ The collected data is saved into a CSV file
