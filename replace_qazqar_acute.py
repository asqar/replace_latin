#!/usr/bin/env python3
# coding: utf-8

import string
import imp
import sys
imp.reload(sys)

cyrillic = u"АаӘәБбВвГгҒғДдЕеЖжЗзИиЙйКкҚқЛлМмНнҢңОоӨөПпРрСсТтУуҰұҮүФфХхҺһЦцЧчШшЩщЫыІіЭэ"
newlatin = u"AaÁáBbVvGgHhDdEeJjZzÏïYyKkQqLlMmNnŃńOoÓóPpRrSsTtWwUuÚúFfXxḦḧŠšČčCcĆćIiÍíÉé"

with open("in.txt","r") as in_file:
    with open("out.txt","a") as out_file:
        data =  in_file.read()
        symmap = {ord(c): ord(t) for c, t in zip(cyrillic, newlatin)}
        out = data.translate(symmap) \
            .replace(u"Ъ", u"") \
            .replace(u"ъ", u"") \
            .replace(u"Ь", u"") \
            .replace(u"ь", u"") \
            .replace(u"Ё", u"Yo") \
            .replace(u"ё", u"yo") \
            .replace(u"Ю", u"yu") \
            .replace(u"ю", u"yu") \
            .replace(u"Я", u"Ya") \
            .replace(u"я", u"ya")
        print(out, end="", file=out_file)