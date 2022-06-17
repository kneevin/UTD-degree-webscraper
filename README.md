# UTD-degree-webscraper
Scrape UTD Website for Courses

1. https://www.utdallas.edu/wp-sitemap-posts-fact_sheets-1.xml
    - Leads to 'fact-sheets' of 143 degrees
    - Store all links, tag="td" class="loc"
2. Go to each link, on each link do the following first:
    - Find catalog page: tag="a" href=True
        - a['href'] will return the link string
        - Store the a['href'] string into a textfile, then add a new line
3. Now with all href links, open it then start scraping each link:
    - Scrape all things with class xind-0 to xind-6
    - Scrape h2 tag with class="xind-1" -> this is the name of the degree
    - Add all of this to a textfile, with the name being the h2 tagged degree

NOTES / DON'T KNOW HOW TO DO:
    - How do I store these text files? Should I just store them as txt