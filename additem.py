#!/usr/bin/env python

import sys

WISHLIST_FILE="./wishlist.md"

class NewReadingItem(object):
    def __init__(self,item):
        self.title=item[0]
        self.url=item[1]
    
    def __str__(self):
        return("- [%s](%s)\n" % (self.title,self.url))
        
    def append_to_wishlist(self,wishlist_file):
        open(wishlist_file,"a").write(str(self))


def main(title,url,wl_file=WISHLIST_FILE):
    item=NewReadingItem((title,url))
    item.append_to_wishlist(wl_file)
    
    
if __name__=="__main__":
    if(len(sys.argv)==3):
        main(sys.argv[1],sys.argv[2])
    elif(len(sys.argv)==4):
        main(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print("Specify article title, article URL, and optionally path to wishlist file.")
        sys.exit(1)
    
    sys.exit(0)

    