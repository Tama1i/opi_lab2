#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":
    re = str(input("ishodnic - "))
    wr = str(input("cuda - "))
    kn = input("vvedite nov catalog ")
    p = os.getcwd()
    path = os.path.join(p, kn)
    os.makedirs(path)

    with open(re, "w+", encoding="utf-8") as file:
        qe = open(wr, "a")
        w = 1
        q = ""
        ot = ""
        for i in file:
            q = str(w) + "; " + i
            w += 1
            ot = ot + q + "\n"
        os.chdir(path)
        qe = open(wr, "a")
        qe.write(ot)

