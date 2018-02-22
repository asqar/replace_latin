#!/usr/bin/env python3
# coding: utf-8

import string
import imp
import sys
imp.reload(sys)

cyrillic = u"АаӘәБбВвГгҒғДдЕеЖжЗзИиЙйКкҚқЛлМмНнҢңОоӨөПпРрСсТтУуҰұҮүФфХхҺһЦцЧчШшЩщЪъЫыІіЬьЭэ"
newlatin = u"AaÄäBbVvGgĞğDdEeJjZzÏïÝýKkQqLlMmNnÑñOoÖöPpRrSsTtWwUuÜüFfXxHhCcÇçŞşĆćʺʺIıİiʹʹÉé"

with open("in.txt","r") as in_file:
    with open("out.txt","a") as out_file:
        data =  in_file.read()
        symmap = {ord(c): ord(t) for c, t in zip(cyrillic, newlatin)}
        out = data.translate(symmap) \
            .replace(u"Щ", u"Şş") \
            .replace(u"щ", u"şş") \
            .replace(u"Ё", u"Yo") \
            .replace(u"ё", u"yo") \
            .replace(u"Ю", u"yu") \
            .replace(u"ю", u"yu") \
            .replace(u"Я", u"Ya") \
            .replace(u"я", u"ya")
        print(out, end="", file=out_file)