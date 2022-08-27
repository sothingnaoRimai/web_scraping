import json
from scraping import scrap

def group_by_year(a):  ##task 2
    years=[]
    movie_dict={}
    for i in a:
        year=i['year']
        if year not in years:
            years.append(year)
    for i in years:
        movie_dict[i]=[]
        # print(movies)

    for j in a:
        year=j['year']
        for k in movie_dict:
            if str(k)==str(year):
                movie_dict[k].append(j)
    with open("year_wise.json","w") as f1:
        json.dump(movie_dict,f1,indent=4,sort_keys=True)
    for i in movie_dict:
        data=''
    f1.close()
    # return (movie_dict)
group_by_year(scrap)
dec_arg=group_by_year(scrap)