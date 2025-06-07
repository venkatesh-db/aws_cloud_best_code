
# combiation of DSA used in AWS 

laptop1=["dell","i5"]
laptop2=["hp","i7"]
laptop3=["mac","m1"]

familylaptop=[ ["dell","i5"] ,["hp","i7"] , ["mac","m1"]     ]
#                index 0        index 1       index 2 

familylaptop.append(["mac","m2"] )

for i in familylaptop:
    print(i)

familylaptop1=[ { "son1":["dell","i5"] } ,{"dughter1":["hp","i7"] } , {"father":["mac","m1"] }     ]

for i in familylaptop1:
    print(i.values())
    
for i in familylaptop1:
     for j in i.keys():
         print(j)
         
