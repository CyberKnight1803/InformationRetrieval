import os

path =r"../dataset"
os.chdir(path)

docs = []
data = {}

def read_files(file_path):
    with open(file_path, 'r') as file:
        doc = ''
        for line in file:
            doc += line
        docs.append(doc)

for file in os.listdir():
    if file.endswith('.txt'):
        file_path =f"{file}"
    read_files(file_path)

n = len(file)

for i in range(n):
    data[i] = {}
    data[i]['title'] = (docs[i].split("\n")[0])

    meta = [i for i in docs[i].split("\n")[1:7]]
    merged_meta = ""
    for j in meta:
        merged_meta += j + "\n"

    print(i)
    data[i]['meta'] = merged_meta

    data[i]['body'] = docs[i].split("\n",7)[-1]

print(data)