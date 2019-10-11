import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

file_output = open('list of image links.txt','w')
item = 'live.staticflickr.com/65535/'
url = 'https://www.flickr.com/photos/184012295@N04/pagePAGENUMBER'
web = webdriver.Chrome('../../../../pie/support files/chromedriver.exe')

for page in range(1,3):
    newurl = url.replace('PAGENUMBER',str(page))
    print(newurl)
    web.get(newurl)
    for i in range(10):
        web.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(1)

    list_images = web.find_elements_by_class_name('photo-list-photo-view')
    for imageurl in list_images:
        imageurl.click()
        time.sleep(2)
        web.find_element_by_class_name('share-photo-icon').click()
        web.find_element_by_class_name('embed-type-button').click()
        web.find_element_by_class_name('embed-code-text-field').text
        web.find_element_by_tag_name('body').send_keys(Keys.CTRL)
        
    for url_image in list_images: file_output.write(url_image+'\n')

file_output.close()
