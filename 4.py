import requests
import json
from bs4 import BeautifulSoup

with open("details_one_movie.json","r") as f:
    a=json.load(f)
    i=0
    b=[]
    while i<len(a):
        print(i+1,":",a[i]["name"])
        b.append(a[i]["url"]),
        i=i+1
    user=int(input("enter no: "))
    x=b[user]
    d=requests.get(x)
    soup=BeautifulSoup(d.text,'html.parser')
    c=soup.find('script',type="application/ld+json").text