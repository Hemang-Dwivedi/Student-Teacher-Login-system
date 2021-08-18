import requests

url = 'http://127.0.0.1:5000/login/admin/admin123'
resp = requests.get(url).text
print(resp)
if resp == "Success":
    print("YES")
else:
    print(str(resp))
