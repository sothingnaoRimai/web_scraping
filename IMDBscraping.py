# from bs4 import BeautifulSoup
# import requests

# # try:
# # url="https://www.imdb.com/chart/top/"
# source=requests.get("https://www.imdb.com/chart/top/")
# # source=requests.get(url)
# print(source)
# source.raise_for_status()
# soup=BeautifulSoup(source.text,"html.parser")
# # print(soup)
# movies=soup.find("tbody",class_="lister-list").find_all("tr")
#     # print(len(movies))
# for movie in movies:
#     name=movie.find("td",class_="titleColumn").a.text  #only a will give the content# but .text give the exact name of the movieThe Shawshank Redemption
#     # rank=  movie.find("td",class_="titleColumn").text      # 1. The Shawshank Redemption (1994) 
#     # rank=  movie.find("td",class_="titleColumn").get_text(strip=True).split(".") #['1', 'The Shawshank Redemption(1994)']
#     rank=  movie.find("td",class_="titleColumn").get_text(strip=True).split(".") [0] # 1
#     year=movie.find("td",class_="titleColumn").span.text.strip("()") #  here i got the year (1994) .strip will removes the brackets 1994
#     # rating=movie.find("td",class_="ratingColumn imdbRating") #<td class="ratingColumn imdbRating">
#                       #<strong title="9.2 based on 2,620,893 user ratings">9.2</strong>
#                        # </td>
#     rating=movie.find("td",class_="ratingColumn imdbRating").strong.text # shows only rating #9.2
        
# #     # print(movie)
# #     # print(name)
# #     # print(rank)
# #     # print(year)
# #     # print(rating)
#     print(rank,name,year,rating)
#     # break
# # except Exception as e:
# #     print(e)



# The HTML <td> element is found in an HTML table within the <body> tag. The <td> tag defines the standard cells 
# in the table which are displayed as normal-weight, left-aligned text. The <tr> tag defines the table rows. 
# There must be at least one row in the table.

from bs4 import BeautifulSoup
import requests
import json
source=requests.get("https://www.imdb.com/chart/top/")
# print(source)
source.raise_for_status()
soup=BeautifulSoup(source.text,"html.parser")
movies=soup.find("tbody",class_="lister-list").find_all("tr")
position=[]
movie=[]
year=[]
rating=[]
for movie in movies:
    name=movie.find("td",class_="titleColumn").a.text 
    movie.append(name)
    rank=  movie.find("td",class_="titleColumn").get_text(strip=True).split(".") [0]
    position.append(rank)
    year1=movie.find("td",class_="titleColumn").span.text.strip("()") 
    year.append(year1)

    rating1=movie.find("td",class_="ratingColumn imdbRating").strong.text 
    rating.append(rating1)
    print(rank,name,year,rating)
    break

# def top_movie_list(position_l,name_l,year_l,rating_l,url_l):
#     Top_movies=[]
#     details={'position':'','name':'','year':'','rating':'','url':''}
#     for i in range (0,len(position_l)):
#         details['position']=int(position_l[i])
#         details['name']=str(name_l[i])
#         year_l[i]=year_l[i][1:5]
#         details['year']=int(year_l[i])
#         details['rating']=float(rating_l[i])
#         details['url']=url_l[i]
#         Top_movies.append(details.copy())
#     return (Top_movies)