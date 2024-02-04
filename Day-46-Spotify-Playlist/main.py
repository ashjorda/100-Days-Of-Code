from bs4 import BeautifulSoup
import requests

# travel_year = input("Which year do you want to travel to? Type the date in the following format: YYYY-MM-DD:")

# Grabs the contents of the requested website
billboard_chart = requests.get(f"https://www.billboard.com/charts/hot-100/1986-04-28")

# Stores the website HTML in the contents variable
song_list = billboard_chart.text

# Loads the website html into BS for parsing
soup = BeautifulSoup(song_list, "html.parser")

artist = soup.find(name="li span", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
print(artist)
