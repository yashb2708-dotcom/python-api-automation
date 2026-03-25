import requests
import json

url = "https://api.github.com/users/octocat"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("User:", data["login"])
        print("Followers:", data["followers"])
        print("Public Repos:", data["public_repos"])

        with open("output.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Data saved to output.json")

    else:
        print("Failed with status:", response.status_code)

except Exception as e:
    print("Error:", str(e))
