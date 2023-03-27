#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    re = str(input("ishodnic - "))
    wr = str(input("cuda - "))
    q = ""
    ot = ""
    with open(re, "r", encoding="utf-8") as file:
        ff = file.readlines()
    for i, ii in enumerate(ff):
        q = '; '.join([str(i + 1), ii])
        ot = ''.join([ot, q])
    with open(wr, "a", encoding="utf-8") as qe:
        qe.write(ot)

