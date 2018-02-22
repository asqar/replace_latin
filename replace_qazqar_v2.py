#!/usr/bin/env python3
# coding: utf-8

import string
import imp
import sys
imp.reload(sys)

cyrillic = u"АаӘәБбВвГгҒғДдЕеЗзИиЙйКкҚқЛлМмНнҢңОоӨөПпРрСсТтУуҰұҮүФфХхҺһЦцЪъЫыІіЬьЭэ"
newlatin = u"AaÁáBbVvGgĞğDdEeZzÍíJjKkQqLlMmNnŃńOoÓóPpRrSsTtWwUuÚúFfXxHhCc‘‘YyIi‘‘Éé"

with open("in.txt","r") as in_file:
    with open("out.txt","a") as out_file:
        data =  in_file.read()
        symmap = {ord(c): ord(t) for c, t in zip(cyrillic, newlatin)}
        out = data.translate(symmap) \
        	.replace(u"Ж", u"Zh") \
        	.replace(u"ж", u"zh") \
        	.replace(u"Ш", u"Sh") \
        	.replace(u"ш", u"sh") \
        	.replace(u"Щ", u"Sh") \
        	.replace(u"щ", u"sh") \
        	.replace(u"Ч", u"Ch") \
        	.replace(u"ч", u"ch") \
        	.replace(u"Ё", u"Jo") \
        	.replace(u"ё", u"jo") \
        	.replace(u"Ю", u"Ju") \
        	.replace(u"ю", u"ju") \
        	.replace(u"Я", u"Ja") \
        	.replace(u"я", u"ja")
        print(out, end="", file=out_file)