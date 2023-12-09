import requests
from datetime import datetime

# Pixe.la Documentation Page https://docs.pixe.la/

USERNAME = '<username>'
TOKEN = '<user token>'
PROFILE_PAGE = f'https://pixe.la/@{USERNAME}'
CREATION_URL = 'https://pixe.la/v1/users'
GRAPH_ID = '<graphid>'
# today = datetime(year=2023, month=12, day=8) # If you need to modify a previous date, use this today variable
today = datetime.now()
PROMPT = "<ex. How many hours did you code today?>"  # The prompt should correspond to measurement of what's being
# tracked


# Create User on Pixe.la
user_params = {
    "token": "3hgds83kdfjlsf",
    "username": "ashjorda",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

creation_url = 'https://pixe.la/v1/users'

user_creation = requests.post(url=creation_url, json=user_params)
print(user_creation.text)

# Create Graph on Pixe.la
# graph_params = {
#     "id": "c387dh01",
#     "name": "codinghours",
#     "unit": "commit",
#     "type": "int",
#     "color": "sora",
#     "timezone": "America/Chicago",
# }
#
# header = {
#     "X-USER-TOKEN": TOKEN
# }
#
# graph_creation_url = f'{CREATION_URL}/{USERNAME}/graphs'
#
# graph_creation = requests.post(url=graph_creation_url, json=graph_params, headers=header)
# response = graph_creation.text
# print(response)

# Post Pixel to a specified date on your graph on Pixe.la
# pixel_params = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": input(f"{PROMPT}") # Prompt for the quality of what's being measured
# }

# header = {
#     "X-USER-TOKEN": TOKEN
# }
#
# post_pixel_url = f"{CREATION_URL}/{USERNAME}/graphs/{GRAPH_ID}"
#
# pixel_post = requests.post(url=post_pixel_url, json=pixel_params, headers=header)
# response = pixel_post.text
# print(response)

# # Update a pixel for current date or past date on a graph on Pixe.la
# update_pixel_params = {
#     "quantity": "4"
# }
#
# header = {
#     "X-USER-TOKEN": TOKEN
# }
#
# put_pixel_url = f"{CREATION_URL}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# pixel_put = requests.put(url=put_pixel_url, json=update_pixel_params, headers=header)
# response = pixel_put.text
# print(response)

# # Delete a pixel for current date or past date on a graph on Pixe.la
# header = {
#     "X-USER-TOKEN": TOKEN
# }
#
# delete_pixel_url = f"{CREATION_URL}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# pixel_delete = requests.delete(url=delete_pixel_url, headers=header)
# response = pixel_delete.text
# print(response)
