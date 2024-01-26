from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)

# Finds all the tags by name, and stores thim in a list in the variable
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
name = soup.select_one("#name")
print(name)

# Allows for the selection of a class heading
headings = soup.select_one(".heading")
print(headings)