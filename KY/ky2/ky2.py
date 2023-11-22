import sys
import json
import ssl
import re
from urllib.request import Request, urlopen

def get_arguments():
    if len(sys.argv) > 1:
        p = sys.argv[1]
        depth = int(sys.argv[2])
    else:
        p = input("Enter the package name: ")
        depth = int(input("Enter the depth of scanning: "))
    return p, depth

p, depth = get_arguments()

result = ""
used = set()

def request_json(url):
    request = Request(url)
    contxt = ssl._create_unverified_context()
    with urlopen(request, context=contxt) as response:
        return json.loads(str(response.read(), encoding='utf-8'))

def plot(curname, current_depth):
    global result
    global used
    used.add(curname)
    if current_depth > depth:
        return
    print(curname)
    s = request_json("https://pypi.org/pypi/" + curname + "/json")["info"]["requires_dist"]
    if s is None:
        return
    for i in s:
        print(i)
    q = ([re.split(r'==|\[| |;|<|>|]|=|~|!', i)[0] for i in s])
    print(q)
    for i in q:
        result += (curname.replace('-', '_').replace('.', '_') + " -> " + i.replace('-', '_').replace('.','_') + ";\n")
        if i not in used:
            plot(i, current_depth + 1)

plot(p, 0)

result = "digraph G {\n" + result + "\n}"
with open(p + ".dot", "w") as f:
    f.write(result)
