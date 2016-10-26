#!/usr/bin/python

import os, re
import fnmatch
from os.path import join, getsize

for root, dir, files in os.walk("./source/cn"):
    if re.search("news/articles",root):
        print root
        print ""
        for items in fnmatch.filter(files, "*.erb"):
                print "..." + items
                with open(join(root,items), 'r') as searchfile:
                    for line in searchfile:
                        if "metaImage:" in line:
                            temp = re.search("metaImage: [\"\''](.+)[\"\'']",line)
                            print temp.group(1)
                            print ""
                        continue
        print ""
