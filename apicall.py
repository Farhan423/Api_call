#Question 06 :- Make an REST API call to Virus total and print the response.

         #api key - "                                                 "

         #hash file - "                                               "


import requests

# Define the API key and the hash file
api_key = "__________________________________________________________"
hash_file = "________________________________________________________"

# Define the URL for the API call
url = f"                                 {hash_file}"

# Define headers with the API key
headers = {
    "x-apikey": api_key
}

# Make the API call
response = requests.get(url, headers=headers)

# Print the response
print(response.json())
