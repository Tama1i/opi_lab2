#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":
    re = input("ishodnic - ")
    wr = input("cuda - ")
    ka = input("catalog - ")
    p = os.getcwd()
    path = os.path.join(p, ka)
    os.makedirs(path)
    q = ""
    ot = ""
    with open(re, "r", encoding="utf-8") as file:
        ff = file.readlines()
    for i, ii in enumerate(ff):
        q = '; '.join([str(i+1), ii])
        ot = ''.join([ot, q])

    os.chdir(path)
    with open(wr, "a", encoding="utf-8") as ge:
        ge.write(ot)
