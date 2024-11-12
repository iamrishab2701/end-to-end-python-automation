import json

courses = '{"name":"Rishab","language": ["Java" , "Python"]}'

# Loads method parse json string and it returns dictionary

dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses["name"])  # output Rishab

# Get me the first language from courses
list_language = dict_courses["language"][0]
print(list_language)

# Open the file and parse it
# load method also returns a dictionary

with open('/Users/rishab/PycharmProjects/end-to-end-python-automation/1jsonparsingexample/sample.json', 'r') as file:
    file_json = json.load(file)

with open('/Users/rishab/PycharmProjects/end-to-end-python-automation/1jsonparsingexample/sample2.json', 'r') as file2:
    file2_json = json.load(file2)

print(file_json['courses'][1]['title'])

# Get particular attribute without using index
for course in file_json['courses']:
    for key, value in course.items():
        if course[key] == 'RPA':
            print(course['price'])

# Comparing two json dictionary object
print(file_json == file2_json)
