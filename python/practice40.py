word = "Donkey"
with open("Donkey.txt", "r") as f:
    content = f.read()

contentnew = content.replace("Donkey","#####")

with open("Donkey.txt", "w") as f:
    f.write(contentnew)
