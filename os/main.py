#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":
    re = str(input("ishodnic - "))
    wr = str(input("cuda - "))
    ka = str(input("catalog - "))
    p = os.getcwd()
    path = os.path.join(p, ka)
    os.makedirs(path)

    with open(re,"r", encoding="utf-8") as file:
        w = 1
        q = ""
        ot = ""
        for i in file:
            q = str(w) + "; " + i
            w += 1
            ot = ot + q + "\n"
    os.chdir(path)
    ge = open(wr, "a")
    ge.write(ot)
    ge.close()
