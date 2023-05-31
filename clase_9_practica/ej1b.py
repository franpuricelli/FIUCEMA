import requests, json

#a) https://jsonplaceholder.typicode.com

url = "https://jsonplaceholder.typicode.com/todos"

# Define the data you want to send in your POST request
data = {
    "userId": 11,
    "id": 2,
    "title": "Tu nuevo título",
    "completed": True
}

# Make the POST request
response = requests.post(url, data=json.dumps(data), headers={'Content-type': 'application/json'})

# Print the response
print(response.text)
