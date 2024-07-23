# tagesschau.de-metadata-analysis
Analyze the Metadata stored in HTML source code from the German public news outlet tagesschau.de. This is useful if you have a bunch of HTML files that you scraped from tagesschau.de and want to categorize. The script will pull information out of locally stored HTML files and print the following data into a CSV file:

* The file path
* The HTML title
* The publication date
* The date of the last editorial update
* The categories the article is in

You can scrape the HTML files using a project like [biolds/sosse](https://github.com/biolds/sosse).

# Usage

Edit scrape_metadata.py to use your file path. Change the output file name if needed. Then just run the script.

Make sure you have BeautifulSoup4 installed via pip as this is a prerequisite.
