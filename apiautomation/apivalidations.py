import requests
import json

# Making get request with query parameter
response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={"AuthorName": "Rishab"})

# Response Handling
print(response.text)
print(type(response.text))
dict_response = json.loads(response.text)
print(type(dict_response))

# Getting response in the json
json_response = response.json()

# Validating any value
for dicts in dict_response:
    for key, value in dicts.items():
        if dicts['aisle'] == "2277":
            print(dicts['isbn'])

# Response status
print(response.status_code)

# Check headers using .headers can be stored as dictionary
print(response.headers)
response_headers = response.headers
print(response_headers['Content-Type'])

# Retrieve the book detail with isbn 103 and comparing the response with expected dictionary
actual_book = {}
for book in json_response:
    actual_book = book
    if book['isbn'] == "103":
        print(book)
        break

print(actual_book)
expected_book = {
    "book_name": "Learn Postman API Testing",
    "isbn": "103",
    "aisle": "227"
}

print(expected_book == expected_book)


