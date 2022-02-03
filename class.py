class Car():
    def __init__(self, company, name, speedLimit, color):
        self.name = name
        self.company = company
        self.speedLimit = speedLimit
        self.color = color

    def start(self):
        print('started')   

    def changeGear(self):
        print('gears changes to 6')

    def acclerate(self):
        print('acclearation at 20')

    def stop(self):
        print('turning off the engine')
    

# Define some students
Nexon = Car("Tata","Nexon",120,"black")
Tesla = Car("Tesla", "modelX",160, "white")

# Now we can get to the grades easily
Nexon.start()
#print(Tesla.color)
#print(Tesla.changeGear())
#print(Nexon.stop())
Nexon.color = "white"
print(Nexon.color)
