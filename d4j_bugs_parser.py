import json

count = 0
x = []
with open('defects4j-bugs.json', 'r') as rf:
    data = json.load(rf)
    for version in data:
        if version["project"] == "Lang":
            x.append(version)
x.sort(key=lambda x: x.get('bugId'))
bugs_json = json.dumps(x, indent=4)

with open("lang_bugs.json","w") as wf:
    wf.write(bugs_json)
