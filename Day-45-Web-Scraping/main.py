from bs4 import BeautifulSoup
import requests

# Grabs the contents of the requested website
website = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

# Stores the website HTML in the contents variable
contents = website.text

# Loads the website html into BS for parsing
soup = BeautifulSoup(contents, "html.parser")

# # Creates a list called "titles", with all the titles from the contents variable.
titles = [titles.get_text() for titles in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")]
titles.reverse()  # Reverses the list, so that number 1 is first and not 100

# Creates a file called "top100.txt", and writes each title on a new line.
with open("top100.txt", "w") as movies:
    for entries in titles:
        movies.write(f"{entries} \n")
