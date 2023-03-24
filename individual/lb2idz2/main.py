#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    re = str(input("ishodnic - "))
    wr = str(input("cuda - "))
    with open(re,"r", encoding="utf-8") as file:
        qe = open(wr,"a")
        w = 1
        q = ""
        for i in file:
            q = str(w) + "; " + i
            w += 1
            qe.write(q+"\n")

