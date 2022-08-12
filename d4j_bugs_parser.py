import json

count = 0
with open('defects4j-bugs.json', 'r') as rf:
    data = json.load(rf)
    for version in data:
        if version["project"] == "Lang":
            print(version["bugId"], version["changedFiles"])