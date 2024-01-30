from bs4 import BeautifulSoup
import requests

# Grabs the contents of the requested website
website = requests.get("https://news.ycombinator.com/news")

# Stores the website HTML in the contents variable
contents = website.text

# Loads the website html into BS for parsing
soup = BeautifulSoup(contents, "html.parser")

#  Creates two empty list to contain the article titles, and associated links. Then loops through all titles
# and links and appends them to the empty list.

article_titles = []
article_links = []

for articles in soup.find_all(name="span", class_="titleline"):
    article = articles.find(name="a")
    article_titles.append(article.get_text())
    article_links.append(article.get("href"))

# Perform list comprehension to extract the scores for each article from the above operation
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Print the top voted article, and it's link based the highest score of the articles of the day.
print(article_titles[article_upvote.index(max(article_upvote))])
print(article_links[article_upvote.index(max(article_upvote))])
# print(article_upvote)


















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