from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import os


def get_imgs(site):
    source = requests.get(site).text
    soup = bs(source, "lxml")
    urls = [str(url["src"]) for url in soup.findAll("img")
            if ".jpg" in str(site+url["src"]) or ".png" in str(site+url["src"])]
    return urls


def download(urls):
    i = 1
    for url in urls:

        urllib.request.urlretrieve(url, "Images/img{}.png".format(i))
        print("image",i)
        i += 1



def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error")


create_folder("./Images/")
download(get_imgs("https://mangadejapan.com/articles/detail/1104"))
print("done")
