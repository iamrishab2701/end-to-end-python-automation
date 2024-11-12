import requests

from apiautomation.payload import payload_from_db, add_book_payload
from utilities.configurations import get_config, get_github_token, get_github_email
from utilities.resources import *

url_add_book = get_config()['API']['endpoint'] + ApiResources.add_book
url_delete_book = get_config()['API']['endpoint'] + ApiResources.delete_book
url_github = get_config()['API']['github_url']
headers = {'Content-Type': 'application/json'}
url_github_fetch_repo = get_config()['API']['github_url'] + '/repos'

db_query = 'select * from books'

# Making post request using requests
post_response = requests.post(url_add_book, json=payload_from_db(db_query),
                              headers=headers)

# Printing the response
post_response_json = post_response.json()
print(post_response_json)

# Checking if the Response has the Msg successfully added and extract ID
book_id = ''
for key, value in post_response_json.items():
    if post_response_json['Msg'] == 'successfully added':
        book_id = post_response_json['ID']
        print(f"Book Successfully added with ID {book_id}")
        break

# Deleting the book by making post request

delete_response = requests.post(url_delete_book, json={'ID': book_id})
print(delete_response.text)
delete_response_json = delete_response.json()

for key, value in delete_response_json.items():
    if delete_response_json['msg'] == 'book is successfully deleted':
        print(delete_response_json['msg'])
        break

# GitHub APIs with Authorization
github_session = requests.session()
github_session.auth = auth = (get_github_email(), get_github_token())
github_response = github_session.get(url_github, verify=False, auth=(get_github_email(), get_github_token()))
print(github_response.status_code)

# Session Managing using session() method and auth function

repo_response = github_session.get(url_github_fetch_repo)
print(repo_response.status_code)
