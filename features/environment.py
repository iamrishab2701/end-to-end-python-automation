import requests

from utilities.configurations import get_config
from utilities.resources import ApiResources


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        # Check if book_id exists before attempting to delete the book
        if hasattr(context, 'book_id'):
            url_delete_book = get_config()['API']['endpoint'] + ApiResources.delete_book
            delete_response = requests.post(url_delete_book, json={'ID': context.book_id})

            # Check if delete request was successful
            if delete_response.status_code == 200:
                delete_response_json = delete_response.json()
                if delete_response_json.get('msg') == 'book is successfully deleted':
                    print(delete_response_json['msg'])
                else:
                    print("Book deletion message not found in response.")
            else:
                print(f"Failed to delete book. Status code: {delete_response.status_code}")
        else:
            print("No book_id found; nothing to delete.")
