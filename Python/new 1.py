def shipGround(weight):
  #send by ground
  flatCharge = 20.00
  if weight <= 2.0:
    cost = 1.50*weight
  elif weight <= 6.0:
    cost = 3.00*weight
  elif weight <= 10.0:
    cost = 4.00*weight
  else:
    cost = 4.75*weight
  cost+=flatCharge
  return cost
  
def shipDrone(weight):
  #send by ground
  flatCharge = 0.00
  if weight <= 2.0:
    cost = 4.50*weight
  elif weight <= 6.0:
    cost = 9.00*weight
  elif weight <= 10.0:
    cost = 12.00*weight
  else:
    cost = 14.25*weight
  cost+=flatCharge
  return cost

def shipBest(weight):
  shipCostGround = shipGround(weight)
  shipCostDrone = shipDrone(weight)
  shipCostPremium = 125.00
  
  if shipCostGround <= shipCostDrone:
    # Ground tanszy
    if shipCostGround <= shipCostPremium:
    # Ground tanszy 
      print("Najtansza opcja to Ground")
      print(shipCostGround)
    else:
      print("Najtansza opcja to Premium")
      print(shipCostPremium)
  else:
    # Drone tanszy
    if shipCostDrone <= shipCostPremium:
    # Drone tanszy 
      print("Najtansza opcja to Drone")
      print(shipCostDrone)
    else:
      print("Najtansza opcja to Premium")
      print(shipCostPremium)
    

print(shipGround(8.4))
print(shipDrone(1.5))
shipBest(0.5)