# Fetch swellnet rating for input site

import requests
from bs4 import BeautifulSoup

def getSwellnetRating(swellnet_website):
    response = requests.get(swellnet_website)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    rating_label = parser.select(".views-field-field-surf-report-rating")
    report_times = parser.select(".views-field-field-surf-report-date")

    print("Today's ratings are:")

    for rating in xrange(0, len(rating_label)):
        time = report_times[rating].select(".field-content")[0].text
        rating = rating_label[rating].select(".field-content")[0].text
        print(time)
        print(rating)