import pytest
import json
import requests


# def test_product():
#     url = "https://automationexercise.com/api/productsList"
#     response = requests.get(url)
#     assert response.status_code == 200
#
# def test_product1():
#     url = "https://automationexercise.com/api/productsList"
#     response = requests.post(url)
#     # print(response.text)
#     assert response.status_code == 405
#
# def test_getllabrandslist():
#     url = "https://automationexercise.com/api/brandsList"
#     response = requests.get(url)
#     # print(response.text)
#     assert response.status_code == 200
#
# def test_PUTtoAllBrandslist():
#     url = "https://automationexercise.com/api/brandsList"
#     response = requests.put(url)
#     # print(response.text)
#     assert response.status_code == 405

# def test_POSTtoSearch():
#     params = {'search_product': 'jeans'}
#     url = "https://automationexercise.com/api/searchProduct"
#     response = requests.post(url, data=params)
#     print(response.json())
#     data = response.json()
#     # print(data["responseCode"])
#     responceCode = data["responseCode"]
#     responceCode1 = data["products"]
#     print(responceCode1[0]["category"]["usertype"]["usertype"])
#     usertype = responceCode1[0]["category"]["usertype"]["usertype"]
#     assert usertype == "Men"
#     assert response.status_code == 200
#     assert responceCode == 200
#
# def test_PostToVerifyLogin():
#     params = {'email': 'abc@gmail.com',
#     'password': '12345'}
#     url = "https://automationexercise.com/api/verifyLogin"
#     response = requests.post(url, data=params)
#     print(response.json())
#     data = response.json()
#     responseCode = data["responseCode"]
#     responseMessage = data["message"]
#     error_message = "User not found!"
#     print(responseCode, responseMessage)
#     assert responseCode == 404
#     assert responseMessage == error_message, f"Expected message {error_message}, but got {responseMessage}"

# def test_PostLoginWithoutEmail():
#     params = {'password': '12345'}
#     url = "https://automationexercise.com/api/verifyLogin"
#     response = requests.post(url, data=params)
#     data = response.json()
#     responseCode = data["responseCode"]
#     responseMessage = data["message"]
#     error_message = "Bad request, email or password parameter is missing in POST request."
#     print(responseCode, responseMessage)
#     assert responseCode == 400
#     assert responseMessage == error_message

# def test_DeleteLogin():
#     url = "https://automationexercise.com/api/verifyLogin"
#     response = requests.delete(url)
#     data = response.json()
#     responseCode = data["responseCode"]
#     responseMessage = data["message"]
#     error_message = "This request method is not supported."
#     print(responseMessage, responseCode)
#     assert responseCode == 405
#     assert responseMessage == error_message

# def test_PostRegister():
#     params = {'name': 'Viktoria',
#     'email': 'viktoriaaaaa.f@gmail.com',
#     'password': 'qweqweqwe',
#     'title': 'Miss',
#     'birth_date': '07',
#     'birth_month': '10',
#     'birth_year': '1998',
#     'firstname': 'Viktoria',
#     'lastname': 'Ffffff',
#     'company': 'Wallester',
#     'address1': 'Kreutzwaldi 4',
#     'address2': '',
#     'country': 'Estonia',
#     'zipcode': '12345',
#     'state': 'Tln',
#     'city': 'Tallinn',
#     'mobile_number': '+3725848484'}
#     url = "https://automationexercise.com/api/createAccount"
#     response = requests.post(url, data=params)
#     print(response.json())
#     data = response.json()
#     responseCode = data["responseCode"]
#     responseMessage = data ["message"]
#     expected_message = "User created!"
#     print(responseMessage, responseCode)
#     assert responseMessage == expected_message
#     assert responseCode == 201

# def test_DeleteMethodParams():
#     params = {'email': 'v.f@gmail.com',
#     'password': 'qweqweqwe'}
#     url = "https://automationexercise.com/api/deleteAccount"
#     response = requests.delete(url, data=params)
#     data = response.json()
#     responseCode = data["responseCode"]
#     responseMessage = data["message"]
#     expected_message = "Account deleted!"
#     print(responseMessage, responseCode)
#     assert responseMessage == expected_message
#     assert responseCode == 200

# def test_PutUpdate():
#     params = {'name': 'Viktoria',
#     'email': 'viktoriaaaaa.f@gmail.com',
#     'password': 'qweqweqwe',
#     'title': 'Miss',
#     'birth_date': '07',
#     'birth_month': '10',
#     'birth_year': '1998',
#     'firstname': 'Viktoria',
#     'lastname': 'Ffffff',
#     'company': 'Wallester',
#     'address1': 'Kreutzwaldi 4',
#     'address2': '',
#     'country': 'Estonia',
#     'zipcode': '12345',
#     'state': 'Tln',
#     'city': 'Tallinn',
#     'mobile_number': '+3725848484'}
#     url = "https://automationexercise.com/api/updateAccount"
#     response = requests.put(url, data=params)
#     data = response.json()
#     responseCode = data["responseCode"]
#     responseMessage = data["message"]
#     expected_message = "User updated!"
#     print(responseCode, responseMessage)
#     assert responseCode == 200
#     assert responseMessage == expected_message

def test_GetUserDetails():
    params = {'email': 'viktoriaaaaa.f@gmail.com'}
    url = "https://automationexercise.com/api/getUserDetailByEmail"
    response = requests.get(url, params=params)
    data = response.json()
    responseCode = data["responseCode"]
    print(response.json())
    assert responseCode == 200