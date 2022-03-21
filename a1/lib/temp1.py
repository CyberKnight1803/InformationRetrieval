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

for i in range(len(file)):
    data[i] = {}
    data[i]['title'] = (docs[i].split("\n")[0])

    meta = [i for i in docs[i].split("\n")[1:7]]
    merged_meta = ""
    for j in meta:
        merged_meta += j + "\n"

    print(i)
    data[i]['meta'] = merged_meta

    data[i]['body'] = docs[i].split("\n",7)[-1]

zone_index = {}

for i in range(len(file)):
    categories = ['title', 'meta', 'body']
    for category in categories:
        for word in data[i][category].split():
            if word not in zone_index:
                zone_index[word] = {
                    "title": set(),
                    "meta": set(),
                    "body": set()
                }
            zone_index[word][category].add(i)

print(zone_index['Dream'])