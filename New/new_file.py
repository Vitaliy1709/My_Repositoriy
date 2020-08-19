import requests

res = requests.get("https://jsonplaceholder.typicode.com/posts")

data = res.json()

new_data = ["".join(i['title'].capitalize() + "\n" + i['body'].capitalize() + "." + "\n\n" for i in data)]

with open("C:/Users/user 79/My_Repositoriy/New/new_text.txt", "w") as file:
    for j in new_data:
        file.write(str(j))
