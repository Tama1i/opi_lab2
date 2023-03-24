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
    w = 1
    q = ""
    ot = ""
    with open(re,"r", encoding="utf-8") as file:
        ff = file.readlines()
    for i in ff:
        q = (f"{str(w)}; {i}")
        w += 1
        ot = (f'{ot}{q}\n')
    os.chdir(path)
    with open(wr, "a", encoding="utf-8") as ge:
        ge.write(ot)
