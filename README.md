# Idealista-WebScraper
This is a simple web scraper that uses selenium to get around captchas on Idealista



Use "first_scrape" when you want to collect more than one page at a time. Paste the URL of your search into the input and then tell it how many pages you would like to scrape. 
- It will produce a csv file ("output") with the name, cost and size of the apartment along with a link.
- It will produce a text file with the original URL in it for use by "update_for_most_recent".

Use "update_for_most_recent" when you want to check for new apartments after you've already done your first scrape.
It works best when your link is to a page that orders by most recent as it only checks the first page. Nonetheless, it can take the URL from the first search if you like. 
- It will produce produce two csv files:
  - "new_places" + the current date and time. This will contain all the new appartments that were found on that scrape. Nothing in the original "output" file will be reproduced here.
  - "new_output". This file is just used to compare against the original "output" file to ensure that nothing is repeated in the "new_places" file.
- All new items will be appended to the original "output file.
