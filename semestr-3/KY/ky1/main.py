import sys
import zipfile

root = sys.argv[1]
file = zipfile.ZipFile(root, 'r')
files = file.namelist()
info = file.infolist()


def isFolder(path):
    for i in info:
        if path == i.filename:
            return i.is_dir()
    return False


cw = root[:-4] + "/"

while 1:
    print(cw, end=" ")
    cmd = list(map(str, input().split()))
    if len(cmd) > 0:
        if cmd[0] == "exit" or cmd[0] == "quit":
            print('*' * 17 + "\nПРОГРАММА ЗАКРЫТА\n" + '*' * 17)
            exit(0)

        elif cmd[0] == "pwd":
            print(cw)

        elif cmd[0] == "ls":
            for i in files:
                qq = list(map(str, cw.split('/')))
                qq = [x for x in qq if len(x) > 0]
                if cw in i:
                    q = list(map(str, i.split('/')))
                    q = [x for x in q if len(x) > 0]
                    if len(q) == len(qq) + 1:
                        print(i[len(cw):], end="\t\t")
            print()

        elif cmd[0] == "cd":
            if len(cmd) == 1:
                cw = root[:-4] + "/"
                continue
            nw = cmd[1]
            if ".." in cmd[1]:
                up_level = cmd[1].count("..")
                qq = list(map(str, cw.split('/')))
                qq = [x for x in qq if len(x) > 0]
                if len(qq) > up_level:
                    qq = qq[:len(qq) - up_level]
                    cw = ""
                    for i in qq:
                        cw += i + "/"
                else:
                    cw = root[:-4] + "/"
            else:
                if cmd[1][0] == "/":
                    if isFolder(cmd[1][1:] + '/'):
                        cw = cmd[1][1:] + "/"
                else:
                    if cmd[1][0:2] == "./":
                        nw = cw + cmd[1][2:] + '/'
                    else:
                        nw = cw + cmd[1] + '/'
                    if nw in files and isFolder(nw):
                        cw = nw
                    else:
                        print(f"cd: can't cd to {cmd[1]}: No such directory")

        elif cmd[0] == "cat":
            if len(cmd) == 1:
                print("cat: argument required")
                continue
            with zipfile.ZipFile(root) as ar:
                try:
                    with ar.open((cw + cmd[1]), 'r') as fi:
                        symb = [x.decode('utf8').strip() for x in fi.readlines()]  # декод в текст
                        for s in symb:
                            print(s)
                except Exception as e:
                    print("cat: can't open '" + cmd[1] + "': No such file")

        else:
            print(f"sh: {cmd[0]}: not found")
