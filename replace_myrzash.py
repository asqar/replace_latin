#!/usr/bin/env python3
# coding: utf-8

import string
import imp
import sys
imp.reload(sys)

cyrillic = u"АаБбВвГгДдЕеИиЙйЗзКкҚқЛлМмНнОоПпРрСсТтУуҰұФфХхҺһЦцЪъЫыІіЬь"
newlatin = u"AaBbVvGgDdEeJjJjZzKkQqLlMmNnOoPpRrSsTtUuWwFfXxXxCc''YyIi''"

with open("in.txt","r") as in_file:
    with open("out.txt","a") as out_file:
        data =  in_file.read()
        symmap = {ord(c): ord(t) for c, t in zip(cyrillic, newlatin)}
        out = data.translate(symmap) \
            .replace(u"Ә", u"Ah") \
            .replace(u"ә", u"ah") \
            .replace(u"Э", u"Ye") \
            .replace(u"э", u"ye") \
            .replace(u"Ғ", u"Gh") \
            .replace(u"ғ", u"gh") \
            .replace(u"Ж", u"Zh") \
            .replace(u"ж", u"zh") \
        	.replace(u"Ң", u"NH") \
        	.replace(u"ң", u"nh") \
        	.replace(u"Ө", u"Oh") \
        	.replace(u"ө", u"oh") \
        	.replace(u"Ү", u"Uh") \
        	.replace(u"ү", u"uh") \
        	.replace(u"Ч", u"Ch") \
        	.replace(u"ч", u"ch") \
        	.replace(u"Ш", u"Sh") \
        	.replace(u"ш", u"sh") \
        	.replace(u"Щ", u"Sch") \
        	.replace(u"щ", u"sch") \
        	.replace(u"Ё", u"Yo") \
        	.replace(u"ё", u"yo") \
        	.replace(u"Ю", u"Yu") \
        	.replace(u"ю", u"yu") \
        	.replace(u"Я", u"Ya") \
        	.replace(u"я", u"ya")
        print(out, end="", file=out_file)