import sys
import webbrowser
from tkinter import filedialog
from open_lineup import *

lineup_date = ''
fhand = None
to_open = None
try:
    lineup_date = sys.argv[1]
    fhand = open_file(lineup_date)
except:
    # lineup_date = input('Line-up Date (yyyy-mm-dd): ')
    fhand = filedialog.askopenfile('r')


to_open = get_links(fhand)

if len(to_open) == 0:
    exit()

print(to_open)

print('# of Links: ', len(to_open))
i = 0
for link in to_open:
    if i == 0:
        # open_link(link, 1)
        webbrowser.open(link, 1)
    else:
        # open_link(link, 2)
        webbrowser.open(link, 2)
    i = i + 1
