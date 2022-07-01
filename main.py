import sys
from open_lineup import *

lineup_date = ''

try:
    lineup_date = sys.argv[1]
except:
    lineup_date = input('Line-up Date (yyyy-mm-dd): ')

fhand = open_file(lineup_date)
to_open = get_links(fhand)
print(to_open)

print('# of Links: ', len(to_open))
i = 0
for link in to_open:
    if i == 0:
        chrome(link)
    else:
        chrome(link, 't')
    i = i + 1
