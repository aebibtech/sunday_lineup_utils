# Author: Paul Abib Camano
# This module contains functions that
# operate on text files for extracting
# YouTube links.
#
# This can work as a standalone program. It opens links in the browser.
# For now, it works on Windows. 

import os

# This function gets the Youtube Links from a file
# returns a list
def get_links(file):
    links = []
    for line in file:
        if line.startswith("https://"):
            lnk = line.replace('\n', '') # Strip \n from link
            print('Link found: ', lnk)
            links.append(lnk)
    return links


# This function opens a lineup file in read mode and returns a file handle
def open_file(lineup_date):
    lineups = os.path.expanduser("~/Documents/Lineup Files")
    try:
        lineup_file = lineups + "/{}.txt".format(lineup_date)
        fhand = open(lineup_file)
        #print(fhand.read())
    except:
        print("File not found.\n\n")
    return fhand



