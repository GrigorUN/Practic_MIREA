import json
import hashlib
import subprocess
import sys
from graph import Graph


def cmdDict(file):
    global col
    res = {}
    target = ""
    for i in file:
        mkblock = i.split(' ')
        print("\nmkblock: ", end='')
        print(mkblock)
        if i[0] in [' ', '\t']:
            if target + '_cmds' not in res:
                res[target + '_cmds'] = [i]
            else:
                res[target + '_cmds'].append(i)
            print("commands: ", end='')
            print(res[target + '_cmds'])
        else:
            target = mkblock[0][:-1]
            col.add(target)
            print("target: ", end='')
            print(target)
            res[target] = mkblock[1:]
            print('dependencies: ', end='')
            print(mkblock[1:])
            for a in mkblock[1:]:
                col.add(a)
    return res


def createGraph(col, d):
    g = Graph(col)
    for i in d.keys():
        if not str(i).__contains__("_cmds"):
            if isinstance(d[i], list):
                for qq in d[i]:
                    g.addEdge(qq, i)
            else:
                g.addEdge(d[i], i)
    return g


def md5(fname):
    hash_md5 = hashlib.md5()
    with open('files/' + fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def run_make(li):
    if (li):
        li.reverse()
    print("LI: ",end='')
    print(li)
    global d
    db = json.loads(open('db.json').read())
    print(db)
    for i in li:
        print(i)
        if i.find('.') != -1:
            print(db.get(i))
            if db.get(i) == None:
                if isinstance(d[i + "_cmds"], list):
                    for q in d[i + "_cmds"]:
                        try:
                            subprocess.run(str(q),check=True)
                        except:
                            print('Command not completed')
                            break
                else:
                    try:
                        subprocess.run(str(d[i + "_cmds"]),check=True)
                    except:
                        print('Command not completed')
                        break
                try:
                    if db[i] != md5(i):
                        db[i] = md5(i)
                except:
                    db[i] = md5(i)
            elif db.get(i):
                if db[i] != md5(i):
                    try:
                        if isinstance(d[i + "_cmds"], list):
                            for q in d[i + "_cmds"]:
                                try:
                                    subprocess.run(str(q),check=True)
                                except:
                                    print('Command not completed')
                                    break

                        else:
                            try:
                                subprocess.run(str(d[i + "_cmds"]),check=True)
                            except:
                                print('Command not completed')
                                break
                        db[i] = md5(i)
                    except KeyError:
                        db[i] = md5(i)
                        run_make(li)
        else:
            if isinstance(d[i + "_cmds"], list):
                for q in d[i + "_cmds"]:
                    try:
                        subprocess.run(str(q),check=True)
                    except:
                        print('Command not completed')
                        break

            else:
                try:
                    subprocess.run(str(d[i + "_cmds"]),check=True)
                except:
                    print('Command not completed')
                    break
    file = open("db.json", "w")
    file.write(json.dumps(db))
    file.close()


def createSubGraph(actname, gr):
    global d
    if actname in d.keys():
        print(d[actname])
        if isinstance(d[actname], list):
            if len(d[actname]) == 0:
                gr.addEdge(actname, actname)
            for qq in d[actname]:
                gr.addEdge(qq, actname)
                createSubGraph(qq, gr)
        else:
            gr.addEdge(d[actname], actname)
    return gr


makefile = open('makefile').readlines()
makefile = [item.replace('\n', '') for item in makefile if item != '\n']
print('*' * 12 + 'MAKEFILE' + '*' * 12)
for item in makefile:
    print(item)
print('*' * 12 + 'MAKEFILE' + '*' * 12)
col = set()
d = cmdDict(makefile)
g = createGraph(len(col), d)
print('\ntargets: ', end='')
print(col)
print('\ndict: ', end='')
print(d)
makellist = g.topologicalSort()

args = sys.argv
if len(args) > 1:
    if args[1] == 'clean':
        run_make(['clean'])
        file = open("db.json", "w")
        file.write(json.dumps({}))
        file.close()
    else:
        gg = createSubGraph(args[1], Graph(0))
        newli = gg.topologicalSort()
        print("NEWLIST: ", end='')
        print(newli)
        run_make(newli)
else:
    run_make(d['all'])
