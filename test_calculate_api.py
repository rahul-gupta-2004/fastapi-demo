import requests

BASE_URL = "https://fastapi-demo-3wek.onrender.com"

# Example: Add two numbers
response = requests.get(f"{BASE_URL}/add", params={"a": 5, "b": 3})
print("Add:", response.json())

# Example: Subtract two numbers
response = requests.get(f"{BASE_URL}/subtract", params={"a": 10, "b": 4})
print("Subtract:", response.json())

# Example: Multiply two numbers
response = requests.get(f"{BASE_URL}/multiply", params={"a": 6, "b": 7})
print("Multiply:", response.json())

# Example: Divide two numbers
response = requests.get(f"{BASE_URL}/divide", params={"a": 20, "b": 5})
print("Divide:", response.json())

# Root endpoint
response = requests.get(BASE_URL)
print("Root:", response.json())

