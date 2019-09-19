rivers = []
counter = []
identification = 1
ocean = 1
boyfriend = 0
Hamilton = []
chicken = []
cucumber = []
while len(rivers ) <= 200000 :
          #ocean  += 1
          boyfriend = ocean + boyfriend
          rivers.append(boyfriend)
          Hamilton.append(ocean)
          ocean += 1 

##print( Hamilton)
Hamilton = list( range (1, 100, 1))
#print (Hamilton )
counter =0

while counter <=100000:
     #counter =0
     for item in rivers:
           for identification in Hamilton:
                 if item % identification ==0 and chicken.count( identification) == 0:
                             chicken.append(identification)
           if len(chicken) >= 500: 
                 print (item, chicken )
                 print(len(chicken ))
                 exit()
           chicken = []
     counter += 1 
     #print ( counter )
     
     # print(item)
