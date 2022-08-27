from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


url="https://www.imdb.com/india/top-rated-indian-movies/"
html=urlopen(url) #To open the web page, pass url to urlopen()
soup=BeautifulSoup(html,"lxml")
# soup=BeautifulSoup(url,"lxml")

def top_movie_list(position_l,name_l,year_l,rating_l,url_l):
    Top_movies=[]
    details={'position':'','name':'','year':'','rating':'','url':''}
    for i in range (0,len(position_l)):
        details['position']=int(position_l[i])
        details['name']=str(name_l[i])
        year_l[i]=year_l[i][1:5]
        details['year']=int(year_l[i])
        details['rating']=float(rating_l[i])
        details['url']=url_l[i]
        Top_movies.append(details.copy())
    return (Top_movies)
    
def scrap_top_list():
    title=soup.title
    main_div=soup.find('div',class_="lister")
    t_body=main_div.find('tbody',class_="lister-list")
    trs=t_body.find_all('tr')

    title=[]
    ratings=[]
    year=[]
    position=[]
    movie_urls=[]
    for tr in trs:
        titleColumn=tr.find("td",class_="titleColumn").a.get_text()
        title.append(titleColumn)

        yearColumn=tr.find('td',class_="titleColumn").span.get_text()
        year.append(yearColumn)

        ratingColumn=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        ratings.append(ratingColumn)

        url_t_data=tr.find('td',class_="titleColumn").a['href']
        movie_url="http://www.imdb.com"+ url_t_data
        movie_urls.append(movie_url)
    position=[str(i) for i in range(1,len(trs)+1)]
    x=top_movie_list(position,title,year,ratings,movie_urls)

    with open("details_one_movie.json","w") as f:
        json.dump(x,f,indent=4)
    for i in x:
        data=''
        # for j in i:
            # data=data+str(i[j])+"  "
    f.close()
    return x
scrap=scrap_top_list()
