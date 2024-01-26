from bs4 import BeautifulSoup
import requests

# Grabs the contents of the requested website
website = requests.get("https://news.ycombinator.com/news")

# Stores the website HTML in the contents variable
contents = website.text

# Loads the website html into BS for parsing
soup = BeautifulSoup(contents, "html.parser")

# Saves the first Article tittle, link, and up votes in the below variables, and prints to screen
first_article = soup.find(name="span", class_="titleline")
article_tag = first_article.find(name="a")
article_text = article_tag.get_text()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").get_text()
print(article_text)
print(article_link)
print(article_upvote)


















# import lxml

# with open("website.html") as file:
#     contents = file.read()

# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)

# Finds all the tags by name, and stores them in a list in the variable
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# loops through the all_anchor_tag variable, and uses the getText() module to grab the text
# for tag in all_anchor_tags:
#     print(tag.getText())

# loops through the all_anchor_tag variable, and uses the get module to grab the specified attribute
# for tag in all_anchor_tags:
#     print(tag.get("href"))

# Finds an element, and allows for the specification of the id attribute
# heading = soup.find(name="h1", id="name")
# print(heading)

# Allows you to select a class, as class is a python reserved name. so you use class_ to grab class objects
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# Allows the selection of an css id by name
# name = soup.select_one("#name")
# print(name)
#
# # Allows for the selection of a class heading
# headings = soup.select_one(".heading")
# print(headings)