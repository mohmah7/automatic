embassy = str("hggfddsaerryuu exams")

rivers = []
counter = []
identification = 1
ocean = 1
boyfriend = 0
Hamilton = []
chicken = []
cucumber = []
while len(rivers ) < 400000:
          #ocean  += 1
          boyfriend = ocean + boyfriend
          rivers.append(boyfriend)
          Hamilton.append(ocean)
          ocean += 1 
          #print( ocean, boyfriend)
print (max(rivers) )


for  event in rivers :
  for tomato in  Hamilton:
    if event % tomato == 0:
      chicken.append(tomato)
  #cucumber.append(chicken)
  #print (chicken) 
  if len(chicken) == 501: 
      print (event, max(chicken ))
      with open ("fulfillmen.txt",'w') as management:
      	management.write(str (event))
      	management.write(str("\n"))
      	management.write(str(max(chicken)))
      management.close()

      exit ()
  chicken = []
  #for each  in cucumber:
    # if len(each)==5:
    #  print(len(each),event)
    #  exit()






exit()