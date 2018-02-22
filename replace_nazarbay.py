#!/usr/bin/env python3
# coding: utf-8

import string
import imp
import sys
imp.reload(sys)

cyrillic = u"АаБбВвГгДдЕеЖжЗзКкҚқЛлМмНнОоПпРрСсТтҰұФфХхҺһЦцЪъЫыІіЬьЭэ"
newlatin = u"AaBbVvGgDdEeJjZzKkQqLlMmNnOoPpRrSsTtUuFfHhHhSs‘‘YyIi‘‘Ee"

with open("in.txt","r") as in_file:
    with open("out.txt","a") as out_file:
        data =  in_file.read()
        symmap = {ord(c): ord(t) for c, t in zip(cyrillic, newlatin)}
        out = data.translate(symmap) \
            .replace(u"Ә", u"A'") \
            .replace(u"ә", u"a'") \
            .replace(u"Ғ", u"G'") \
            .replace(u"ғ", u"g'") \
            .replace(u"И", u"I'") \
            .replace(u"и", u"i'") \
        	.replace(u"Й", u"I'") \
        	.replace(u"й", u"i'") \
        	.replace(u"Ң", u"N'") \
        	.replace(u"ң", u"n'") \
        	.replace(u"Ө", u"O'") \
        	.replace(u"ө", u"o'") \
        	.replace(u"У", u"Y'") \
        	.replace(u"у", u"y'") \
        	.replace(u"Ү", u"U'") \
        	.replace(u"ү", u"u'") \
        	.replace(u"Ч", u"C'") \
        	.replace(u"ч", u"c'") \
        	.replace(u"Ш", u"S'") \
        	.replace(u"ш", u"s'") \
        	.replace(u"Щ", u"S'") \
        	.replace(u"щ", u"s'") \
        	.replace(u"Ё", u"I'o") \
        	.replace(u"ё", u"i'o") \
        	.replace(u"Ю", u"I'y'") \
        	.replace(u"ю", u"i'y'") \
        	.replace(u"Я", u"i'a") \
        	.replace(u"я", u"i'a")
        print(out, end="", file=out_file)