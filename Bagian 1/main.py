from Vehicle import Vehicle
from Ship import Ship
from Plane import Plane

Sh1 = Ship()
Sh1.setShip("Ship", 120, "Battle Ship", "MFO", 1500, 1, "Ireland")
Sh1.outputShip()

Sh2= Ship()
Sh2.setType("Ship")
Sh2.setAge(60)
Sh2.setTypeVech("Cargo")
Sh2.setFuel("MFO")
Sh2.setMaxPass(90000)
Sh2.setMoves(1)
Sh2.setCounty("India")
Sh2.outputShip()

Sh3 = Ship()
Sh3.setShip("Ship", 12, "Ferry", "MFO", 15000, 0, "Indonesia")
Sh3.outputShip()

Sh4 = Ship()
Sh4.setType("Ship")
Sh4.setAge(60)
Sh4.setTypeVech("Cruise")
Sh4.setFuel("MFO")
Sh4.setMaxPass(2000)
Sh4.setMoves(0)
Sh4.setCounty("America")
Sh4.outputShip()

Sh5 = Ship()
Sh1.setShip("Ship", 60, "Navy", "MFO", 100, 1, "Russia")
Sh1.outputShip()

Pl1 = Plane()
Pl1.setPlane("Plane", 24, "Cargo", "Avtur", 240, 0, "10")
Pl1.outputPlane()

Pl2 = Plane()
Pl2.setPlane("Plane", 30, "Fighter", "Avtur", 100, 0, "14")
Pl2.outputPlane()

Pl3= Plane()
Pl3.setPlane("Plane", 10, "Rescue", "Avtur", 50, 0, "5")
Pl3.outputPlane()

Pl4 = Plane()
Pl4.setPlane("Plane", 20, "Private", "Avtur", 10, 0, "15")
Pl4.outputPlane()

Pl5 = Plane()
Pl5.setPlane("Plane", 30, "Jet", "Avtur", 50, 0, "9")
Pl5.outputPlane()

