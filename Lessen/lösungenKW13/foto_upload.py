import requests

CardID = "Kennzeichennummer des Kartes"

# define the relative path of the sample file
file_path = input("Laden Sie hier Ihr Bild hoch: ")

# store the target API URL
target_url = "https://httpbin.org/post"

# create a reference to the file
target_file = open(file_path, "rb")

# send the request
response = requests.post(target_url, files = {{CardID}: target_file})

# check the result
if response.ok:
    print("Upload complete")
    print(response.text)
else:
    print("Something went wrong")