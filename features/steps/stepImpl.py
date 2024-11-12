import requests
from behave import *

from apiautomation.payload import add_book_payload
from utilities.configurations import get_config, get_github_email, get_github_token
from utilities.resources import ApiResources


@given('the book details which needs to be added to Library')
def step_impl(context):
    context.url_add_book = get_config()['API']['endpoint'] + ApiResources.add_book
    print(context.url_add_book)
    context.headers = {'Content-Type': 'application/json'}
    print(context.headers)


@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url_add_book = get_config()['API']['endpoint'] + ApiResources.add_book
    print(context.url_add_book)
    context.headers = {'Content-Type': 'application/json'}
    print(context.headers)
    context.payload = add_book_payload(isbn, aisle)


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    # Making post request using requests
    context.response = requests.post(context.url_add_book, json=add_book_payload("6754", "sdas"),
                                     headers=context.headers)
    print(context.response.status_code)


@then('book is successfully added')
def step_impl(context):
    # Printing the response
    post_response_json = context.response.json()
    print(post_response_json)

    # Checking if the Response has the Msg successfully added and extract ID
    for key, value in post_response_json.items():
        if post_response_json['Msg'] == 'successfully added':
            context.book_id = post_response_json['ID']
            print(f"Book Successfully added with ID {context.book_id}")
            break

    assert post_response_json['Msg'] == 'successfully added'


@given('I have github auth credentials')
def step_impl(context):
    context.github_session = requests.session()
    context.github_session.auth = auth = (get_github_email(), get_github_token())


@when('I hit getRepo API of github')
def step_impl(context):
    url_github = get_config()['API']['github_url']
    context.response = context.github_session.get(url_github, verify=False,
                                                  auth=(get_github_email(), get_github_token()))
    print(context.response.status_code)


@then('status code of response should be {statuscode:d}')  # d will read it as integer
def step_impl(context, statuscode):
    print(context.response.status_code)
    if statuscode == 200:
        assert context.response.status_code == 200
