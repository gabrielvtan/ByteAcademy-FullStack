list = [[('2018-11-01 09:38:52.835798', 'Kenny', 'I like SUPREME....')], [('2018-11-01 09:32:14.637064', 'Jason', 'I like watching the WWE...')], [('2018-11-01 09:38:11.704805', 'Matt', 'I like to eat dank ass food...')], [('2018-11-01 20:40:03.819816', 'Gabby', '"Hello, World!"'), ('2018-11-01 11:20:20.235267', 'Gabby', 'Last tweet'), ('2018-11-01 11:20:15.946016', 'Gabby','Jason is dumb - 2'), ('2018-11-01 11:20:09.040715', 'Gabby', 'Jason look at me - 1'), ('2018-11-01 09:35:35.559562', 'Gabby', 'I like would like a pet llama...'), ('2018-11-01 09:28:13.863115', 'Gabby', 'I like to watch Shakespeare in the Park...')]]

list_2 =[]
for i in list:
    for j in i:
        list_2.append(j)

print(sorted(list_2, key=lambda x:x[0]))