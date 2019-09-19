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

#print( Hamilton)
print( "--------------------------------------------")

#Hamilton = list( range (1, 10000, 1))
#print (Hamilton )
counter =0

while counter <=100000000:
     #counter =0
     for item in rivers:
           for identification in Hamilton:
                 if item % identification ==0 and chicken.count( identification) == 0:
                             chicken.append(identification)
           if len(chicken) >= 460: 
                 print(rivers.index(item))
                 print(rivers[rivers.index(item)-1])
                 print(rivers.index(28))
                 print (item, chicken )
                 print(len(chicken ))
                 exit()
           chicken = []
     counter += 1 
     #print ( counter )
     
     # print(item)
