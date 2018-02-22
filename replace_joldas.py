#!/usr/bin/env python3
# coding: utf-8

import string
import imp
import sys
imp.reload(sys)

cyrillic = u"АаӘәБбВвГгҒғДдЕеЁёЖжЗзИиЙйКкҚқЛлМмНнҢңОоӨөПпРрСсТтУуҰұҮүФфХхҺһЦцШшЩщЪъЫыІіЬьЭэ"
newlatin = u"AaÁáBbVvGgĞğDdEeEeJjZzİiİiKkQqLlMmNnŃńOoÓóPpRrSsTtUuÚúÜüFfHhHhSsWwWw‘‘YyIı‘‘Éé"

with open("in.txt","r") as in_file:
    with open("out.txt","a") as out_file:
        data =  in_file.read()
        symmap = {ord(c): ord(t) for c, t in zip(cyrillic, newlatin)}
        out = data.translate(symmap) \
        	.replace(u"Ч", u"Ch") \
        	.replace(u"ч", u"ch") \
        	.replace(u"Ю", u"Yu") \
        	.replace(u"ю", u"yu") \
        	.replace(u"Я", u"Ya") \
        	.replace(u"я", u"ya")
        print(out, end="", file=out_file)