#!/usr/bin/env python3
# coding: utf-8

import string
import imp
import sys
imp.reload(sys)

cyrillic = u"АаӘәБбВвГгҒғДдЕеЖжЗзИиЙйКкҚқЛлМмНнҢңОоӨөПпРрСсТтУуҰұҮүФфХхҺһЦцЪъЫыІіЬьЭэ"
newlatin = u"AaÁáBbVvGgĞğDdEeJjZzIıIıKkQqLlMmNnŃńOoÓóPpRrSsTtÝýUuÚúFfHhHhSs‘‘YyIi‘‘Éé"

with open("in.txt","r") as in_file:
    with open("out.txt","a") as out_file:
        data =  in_file.read()
        symmap = {ord(c): ord(t) for c, t in zip(cyrillic, newlatin)}
        out = data.translate(symmap) \
        	.replace(u"Ш", u"Sh") \
        	.replace(u"ш", u"sh") \
        	.replace(u"Щ", u"Sh") \
        	.replace(u"щ", u"sh") \
        	.replace(u"Ч", u"Ch") \
        	.replace(u"ч", u"ch") \
        	.replace(u"Ё", u"Io") \
        	.replace(u"ё", u"ıo") \
        	.replace(u"Ю", u"Iu") \
        	.replace(u"ю", u"ıu") \
        	.replace(u"Я", u"Ia") \
        	.replace(u"я", u"ıa")
        print(out, end="", file=out_file)