import requests

from utilities.configurations import get_config

# Managing Cookies

cookie_url = get_config()['API']['endpoint_cookie']
cookie = {'visit-month': 'February'}
cookie_response = requests.get(cookie_url, cookies=cookie)
print(cookie_response.status_code)

cookie_url2 = get_config()['API']['httpbin_cookie']
cookie_session = requests.session()
cookie_session.cookies.update({'visit-year': 'February'})
httpbin_cookie_response = cookie_session.get(cookie_url2, cookies={'visit-year': '2022'})
print(httpbin_cookie_response.text)

# Redirection and timeout
# 301 response for redirection then we will see 200
# To stop redirection use allow_redirects=False in the request
# For timeout we can add timeout=seconds in the requests

print(cookie_response.history)
print(cookie_response.status_code)

# Send Attachments through API
pet_store_image_upload_url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('/Users/rishab/PycharmProjects/end-to-end-python-automation/apiautomation/dog-png-22667.png',
                      'rb')}  # File should be passed in dictionary
image_upload_response = requests.post(pet_store_image_upload_url, files=files)
print(image_upload_response.status_code)
print(image_upload_response.text)
