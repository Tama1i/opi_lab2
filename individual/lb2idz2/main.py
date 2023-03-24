#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    re = str(input("ishodnic - "))
    wr = str(input("cuda - "))
    w = 1
    q = ""
    ot = ""
    with open(re,"r", encoding="utf-8") as file:
        ff = file.readlines()
    for i in ff:
        q = (f"{str(w)}; {i}")
        w += 1
        ot = (f'{ot}{q}\n')
    with open(wr, "a", encoding="utf-8") as qe:
        qe.write(ot)

