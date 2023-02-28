### Scraping job listings from job.amilcar.com
This project is a web scraping tool that extracts job listings data from the website job.amilcar.com. The data is then saved in a CSV file for further analysis.
### How to use
Configure a virtual environment:
``` python -m venv .venv```
This will create a new virtual environment in the current directory.
### Activate the virtual environment:
``` source .venv/bin/activate ```
### Install the Scrapy framework:
``` pip install scrapy ```
This will install the necessary dependencies for running the scraper.
### Run the spider:
``` scrapy crawl job_listings_spider -o job_listings-`date +\%m`-`date +\%d`-`date +\%y`.csv ```
This command will start the spider and save the extracted data in a CSV file named "job_listings-MM-DD-YY.csv" in the current directory.
### Deactivate the virtual environment:
``` deactivate ```
Additional resources
If you encounter special characters in the extracted data, you can use the following website to convert them:
https://r12a.github.io/