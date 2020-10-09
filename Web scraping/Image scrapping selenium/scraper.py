

from selenium import webdriver
import os
import urllib.request
import time



path = r'D:\working repos\Python-Workspace\Web scraping\Image scrapping selenium\webdriver\chromedriver.exe'

url_prefix = "https://www.google.com.sg/search?q="
url_postfix = "&source=lnms&tbm=isch&sa=X&ei=0eZEVbj3IJG5uATalICQAQ&ved=0CAcQ_AUoAQ&biw=939&bih=591"

save_folder = r'D:\working repos\Python-Workspace\Web scraping\Image scrapping selenium\Images'





'''topics = ['Cleaning products','dish-washing powder','detergents','Cigarettes','Alcohol','Coffee packet','sugar packet','takeaway meals'
        ,'pet food packet','Fruit and vegetables','Regular medicines',
        'Computers',
'Mobile phones',
'Entertainment equipment',
'Cameras',
'Household furniture',
'Washing machines','dishwashers',
'Clothing',
'Sports equipment',
'plates', 'pots' , 'pans',
'Luggage',
'Perfumes' ,'cosmetics',
'Running shoes',
'Everyday jewelry',
'House repairs tools', 'paint']'''
topics = [
'Puzzle toys' ,'assembly toys',
'Science toys',
'optical toys',
'Sound toys',
'Spinning toys',
'Wooden toys']
number = [50,40,30]




import random



for topic in topics:
    save_folder = r'D:\working repos\Python-Workspace\Web scraping\Image scrapping selenium\Images'
    save_folder = save_folder + str("\{}".format(topic))
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    print(topic," On going")
    n_images = random.choice(number)
    print("Total number = ",n_images)
    search_url = url_prefix+topic+url_postfix
    path = r'D:\working repos\Python-Workspace\Web scraping\Image scrapping selenium\webdriver\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(search_url)
    value = 0
    for i in range(3):
        driver.execute_script("scrollBy("+ str(value) +",+1000);")
        value += 1000
        time.sleep(1)
    elem1 = driver.find_element_by_id('islmp')
    sub = elem1.find_elements_by_tag_name('img')
    
    
    count=0
    for j,i in enumerate(sub):
        if j < n_images:
            src = i.get_attribute('src')                         
            try:
                if src != None:
                    src  = str(src)
                    #print(src)

                    urllib.request.urlretrieve(src, os.path.join(save_folder, topic+str(j)+'.jpg'))

                else:
                    raise TypeError
            except Exception as e:   
                print(f'fail with error {e}')
    print(topic," done")
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")

    driver.close()