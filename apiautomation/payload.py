from utilities.configurations import get_mysql_connection, get_query


def add_book_payload(isbn, aisle):
    body = {
        "name": "Test1",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Rishab"
    }
    return body


def payload_from_db(query):
    first_record_tuple = get_query(query)
    add_body = {'name': first_record_tuple[0],
                'aisle': first_record_tuple[1],
                'isbn': first_record_tuple[2],
                'author': first_record_tuple[3]}
    return add_body
