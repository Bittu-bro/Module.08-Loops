'''
we have the following dictionary containing details:
user = {
"user_name": "bittu",
"password": "Test@123",
"email": "test12345@gmail.com",
"address": "test,000001",
"country": "India"
}
Delete the sensitive information form the dictionary present in a list
sensitive_info = ["address", "password"]
'''


user = {
"user_name": "bittu",
"password": "Test@123",
"email": "test12345@gmail.com",
"address": "test,000001",
"country": "India"
}
sensitive_info = ["address", "password", "phone"]
for key in sensitive_info:
    if key in user:
        print(f"Deleted => key: {key}, Value: {user[key]}")
        user.pop(key)
    else:
        print(f"{key} not present in the Dictionary")
print(f"Updated dictionary: {user}")    