# webscraping
## 1. webscraper.py
This is the main script used to scrape data from the HTML files of the ransomware group sites. The onion sites for the chose ransomware groups either have human verification checkers or are pagenated hence there was some difficulty using a tor socket to request and scrape the url. However we circumvented this by simply saving the page as a HTML file and scraping from that. To run the scraping for each group, simply uncomment the group name and run the file. 

## 2. data.ipynp
This is the jupyter notebook file used to clean the data, process and generate visuals from the collated data. To determine the country the company is based in we fed the victim website through an LLM (llama3) with a prompt to only return the country it is from. We cleaned out data that the model could not determine the orgin country which were a minute portion that did not skew the data.

## 3. HTML files
Play_HTML, Ransomhub.html were the HTML files used to scrape the necessary data. For the group Lockbit3 collecting the information was difficult as most sites were seized by authorities and did not render much information so we had to use a third party, ransomlook.io that collected their results and we scraped their website instead.