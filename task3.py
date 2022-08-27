import json


with open("year_wise.json","r") as file:
    dec_arg=json.load(file)

    def group_by_decade(): ###task 3 movies
        moviedec={}
        y=1950
        for i in range(1950,2022,10):  #years  movies
            list1=[]  # remainder 3
            for j in dec_arg:
                if y>int(j) and int(j)<(y+10):
                    list1.append(dec_arg[j])
            moviedec[y]=list1
            y+=9
        with open("decade_wise.json","w") as f2:
            json.dump(moviedec,f2,indent=4)
    group_by_decade()

    