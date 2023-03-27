#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def gl(f):
    s = "aeyuioj"
    if f in s:
        return 1

if __name__ == "__main__":
    with open("f1.txt","r", encoding="utf-8") as file:
        f = file.read()
    f = f.lower()
    f = (f" {f} \n")
    s = ""
    i = 1
    ot = ""
    for i, ii in enumerate(f):
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
