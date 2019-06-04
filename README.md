# Rotten-Tomotoes-Review-Scraper

This tool is written in Python using BeautifulSoup to scrape the Rotten Tomotoes website. I was using Spyder to run the file.

## Instructions
- Change the user agent to whatever browser you are using. In the example I am using Chrome.

- Change the for loop for the pages variable to the number of pages that you want to iterate through. In my example I am getting pages 1 (inclusive) through 617 (exclusive).

- The last thing to change is the line 
    r = requests.get("https://www.rottentomatoes.com/m/captain_marvel/reviews/?page=" + str(pages) + "&type=user&sort=", headers=  user_agent)
    The url will have to be changed to whatever movie you are wanting to get reviews from. Make sure it has the /?page= at the end. In my example it is getting reviews from the movie Captain Marvel. 
    
After every page it sleeps for between 10 and 25 seconds so that you are not continously requesting from their servers. This may take some time then to get the all of the reviews. I did 616 pages and that took around 4 hours time. There is a line that will print what number of request you are on and the frequency of it to help keep track. 

The output is stored into a pickel file. At the end I have it loading that pickle file into variable for it to be used. 

I have an example of this on my github for getting Captain Marvel reviews and then doing an analysis on it. The link is https://github.com/SierraK/movie-analysis-CaptainMarvel
