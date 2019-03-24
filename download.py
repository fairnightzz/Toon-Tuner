from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import os


def get_imgs(site):
    source = requests.get(site).text
    print(source)
    soup = bs(source, "lxml")
    urls = [str(url["src"]) for url in soup.findAll("img")
            if ".jpg" in str(site+url["src"]) or ".png" in str(site+url["src"])]
    return urls


def download(urls,directory):
    i = 1
    try:
        for url in urls:
            try:

                if url.find("/") == 0:
                    urllib.request.urlretrieve("https://merakiscans.com"+url, "%s/img%d.png"%(directory,i))
                else:
                
                    urllib.request.urlretrieve(url, "%s/img%d.png"%(directory,i))
                    print("image",i)
                i += 1
            except:
                print(url)
                i+=1
    except:
        pass






        

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error")


#create_folder("User Files/Images/")
#download(get_imgs("https://mangadejapan.com/articles/detail/1104"))
#download(get_imgs("https://merakiscans.com/"),"User Files/TEST")
print("done")
