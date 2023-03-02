#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def gl(f):
    if ((f == "a") or (f == "e") or (f == "y") or (f == "u") or
            (f == "i") or (f == "o") or (f == "j")):
        return 1

if __name__ == "__main__":
    file = open("f1.txt", encoding='UTF')
    f = file.read()
    f = f.lower()
    f = " " + f + "\n"
    s = ""
    i = 1
    ot = ""
    for i in range(len(f)-1):
        if (f[i-1] == " ") or (f[i-1] == "\n"):
            k = 1
            if (gl(f[i]) == 1):
                k = 2
        if k == 2:
            s = s + f[i]
            if (f[i] == " ") or (f[i] == "\n"):
                k = 0
                ot = s + " "

    print(ot)
