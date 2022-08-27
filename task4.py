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
    a=json.loads(c)
    with open('task4_detail.json','w') as f:
        json.dump(a,f,indent=4)
    with open('task4_detail.json','r') as f1:
        r=json.load(f1)
    e={}
    for j in r:
        e['movie']=r['name']
        e['director']=[r['director'][0]['name']]
        e['image']=r['name']
        e['description']=r['description']
        e['language']=r['review']['inLanguage']
        e['genre']=r['genre']
        e['runtime']=r['duration']
        e['country']='india'

    with open("fourth_task.json",'w') as f1:
        json.dump(e,f1,indent=4)
