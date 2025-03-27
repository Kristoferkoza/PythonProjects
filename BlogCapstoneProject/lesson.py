import requests
your_name = input("Input your name: ")
parameters = {
    "name": your_name
}
agify_link = requests.get("https://api.agify.io", params=parameters)
print(agify_link.text)
genderize_link = requests.get("https://api.genderize.io", params=parameters)
print(genderize_link.text)