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


# This function opens Google Chrome with the Link Specified.
# win_type - "w" for New Window, "t" for New Tab
def chrome(link = "https://www.google.com", win_type = "w"):
    gc_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    wtype = None
    if win_type == 'w':
        wtype = '--new-window'
    elif win_type == 't':
        wtype = '--new-tab'
    os.system("\"{}\" {} {}".format(gc_path, wtype, link))


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



