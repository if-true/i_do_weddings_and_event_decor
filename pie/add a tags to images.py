##<div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
##<a href="https://live.staticflickr.com/65535/48665398862_22d319da15_b.jpg">
##<img class="image" src="https://live.staticflickr.com/65535/48665398862_22d319da15_b.jpg"></div></a>
from bs4 import BeautifulSoup as bs

list_inputdata = [i.strip() for i in open('image html.txt').read().split('<div class="row">')]
newfileoutput = open('add a tags to images_output.txt','w')

for row in list_inputdata:
    if row == '': continue
    soup = bs(row,'lxml')
    list_images = soup.find_all('img')
    list_imageurls = [str(i).split('<img class="image" src="')[1].split('"/>')[0] for i in list_images]

    newimagehtml = '<div class="row">'
    for url in list_imageurls:
        newimagehtml += '\n\t<div class="col-lg-6 col-md-6 col-sm-6 col-xs-6"><a href="'+url+'"  target="_blank"><img class="image" src="'+url+'"></div></a>'
    newimagehtml += '\n</div>\n\n'
    newfileoutput.write(newimagehtml)

newfileoutput.close()
