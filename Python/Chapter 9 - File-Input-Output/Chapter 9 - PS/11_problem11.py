
with open("Chapter 9 - PS/old.txt", "r") as f:
    content = f.read()

with open("Chapter 9 - PS/renamed_by_python.txt", "w") as f:
    f.write(content)
