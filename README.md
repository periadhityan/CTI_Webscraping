# webscraping
## 1. webscraper.py
This is the main script used to scrape data from the HTML files of the ransomware group sites. The onion sites for the chose ransomware groups either have human verification checkers or are pagenated hence there was some difficulty using a tor socket to request and scrape the url. However we circumvented this by simply saving the page as a HTML file and scraping from that. To run the scraping for each group, simply uncomment the group name and run the file. 

## 2. Cleaning.ipynp
This is the jupyter notebook file used to clean the data, process and generate visuals from the collated data. To determine the country the company is based in we fed the victim website through an LLM (llama3) with a prompt to only return the country it is from. We cleaned out data that the model could not determine the orgin country which were a minute portion that did not skew the data.

## 3. Merge_file.py
This script combines all the scraped CSV files from different ransomware groups for ransomware activity into a single file with consistent formatting. With the combined data in a single CSV file, we are able to generate comparison charts using tableau.

## 4. Raw_HTML
These were the HTML files of the actual Ransomware group sites. We scraped data from these files to answer the question for the report.

## 5. CSV_files
CSV files contain the csv files that have been cleaned and seperated for data visualisation by Country and Industry

## Preparation
To run the webscraper and jupyternotebook files, install the dependancies by running 'pip install -r requirements.txt' to ensure all dependancies have been installed and then run each file. Uncomment each function you want to run to scrape data again if you have uploaded a new HTML file.
