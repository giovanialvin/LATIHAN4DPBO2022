from lib2to3.pgen2.driver import Driver
from Person import Person
from Job import Job
from Driver import Driver

Pers1 = Person(32, "Andre", "Pria", 1)
Job1 = Job(Pers1, 101, "Go Jek", "Driver")
Dri1 = Driver(Pers1, 101, "Gofood", "Driver", 1002, "2 Jan 2020", "Taxi")
Job1.outputJob()
Dri1.outputDriver()

Pers2 = Person(33, "Yuli", "Wanita", 0)
Job2 = Job(Pers2, 102, "Tix.com", "General Manager")
Job2.outputJob()
print("=================================================")

Pers3 = Person(34, "Hendra", "Pria", 0)
Job3 = Job(Pers3, 103, "Grab", "Driver")
Dri3 = Driver(Pers3, 103, "Grab", "Driver", 1003, "1 Agu 2024", "Sepeda Motor")
Job3.outputJob()
Dri3.outputDriver()

Pers4 = Person(35, "Bambang", "Pria", 0)
Job4 = Job(Pers4, 105, "First Media", "CEO")
Job4.outputJob()
print("=================================================")

Pers5 = Person(50, "Diana", "Wanita", 1)
Job5 = Job(Pers5, 106, "Buka Lapak", "Staff")
Job5.outputJob()
print("=================================================")
