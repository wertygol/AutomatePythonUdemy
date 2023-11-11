import requests

access_token = "EAAKm4lPnVJQBOZCZA6feZCo0TZBrPuHMyqRY8gTsPBkuIjNIOCcWMU9VDjAZCwxUImn00cqP4cJRomqCUivfkGtGbRn9ymsPdYlZAxgJTuGJm9fFl5qSzesMoy56Pfs9GELGUuk4IZBZB260uPTIVjOTRnQ4por7c4bhERuZAQxgUPZBNT62NWKxiSM2tZAjTd8HU3ygdX3n6L2lxFUAjxQC9a4G2UsIURSCt9WSfOLPc72651JZBM8eCxVYOL4iaXIZD"
url = "https://graph.facebook.com/v18.0/"
path = "me/photos/uploaded"
params = {"access_token": access_token}
response = requests.get(
    url + path,
    params,
)

# print(response.text)

for foto in response.json()["data"]:
    # print(foto)
    path = foto["id"]
    params = {"access_token": access_token, "fields": "images, name"}
    response = requests.get(url + path, params=params)
    name = response.json()["name"]

    for image in response.json()["images"]:
        image_bytes = requests.get(image["source"]).content
        image_name = (
            name + "_" + str(image["height"]) + "x" + str(image["width"]) + ".jpg"
        )

        with open(image_name, "wb") as f:
            f.write(image_bytes)
