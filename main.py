from open_lineup import *

fhand = open_file(input('Line-up Date (yyyy-mm-dd): '))
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