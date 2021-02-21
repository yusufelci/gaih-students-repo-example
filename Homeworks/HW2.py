

ogr=["ogr1","ogr2","ogr3","ogr4","ogr5"]
notlar=["midterm","final","homework"]
d={}


for i in range(len(ogr)):
    ogr[i]=str(input("Please write your name and Surname: "))
    notlar[0]=int(input("Midterm: "))
    notlar[1]=int(input("Final: "))
    notlar[2]=int(input("Homework: "))
    ave=(notlar[0]+notlar[1]+notlar[2])/3
    d[ogr[i]]=ave
        
print(d)


sorted_dict = dict( sorted(d.items(),
                           key=lambda item: item[1],
                           reverse=True))
print("Congralations: ",[key for key in sorted_dict.keys()][0]) 
   
    

