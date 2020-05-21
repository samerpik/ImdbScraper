import requests

from bs4 import BeautifulSoup

URL = "https://www.imdb.com/title/tt0088763/"

headers = {
    "User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

def check_rating():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    movieName = soup.select('h1')[0].text.strip()
    ratingValue = soup.find(itemprop="ratingValue").get_text()
    totalVotes = soup.find(itemprop="ratingCount").get_text()

    # Use for decimals, if you need.
    # converterRatingValue = float(ratingValue[0:5])
        

    print(totalVotes + " IMDb users have given a weighted average vote of " + ratingValue + "/10 for " + movieName  )

check_rating()

