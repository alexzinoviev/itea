class PetrolEngine:
    def start(self):
        print('RRRR')

class ElectricEngine:
    def start(self):
        print('UUUU')



class Car:
    def __init__(self, engine):
        self.engine = engine
    def start(self):
        self.engine.sart()


c = Car(engine=ElectricEngine())
c.start()



"""
Pertrol engine
Electric engine - like CSV or JSon Classes


----

class Car - like our controller

----

when we create instance of the class - we send classname

"""