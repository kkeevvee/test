#wszystkie 3 robia to samo

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for ages_element in ages:
  if ages_element < 21:
    a = 1
  else:
      print(ages_element)
	  
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for ages_element in ages:
  if ages_element < 21:
    continue
  print(ages_element)
  
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for ages_element in ages:
  if ages_element < 21:
    continue
  else:
      print(ages_element)