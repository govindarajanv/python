class Bulb(object):
    TotalBulbCount = 0
    def __init__(self):
        Bulb.TotalBulbCount += 1
        self.isOn = False

    @classmethod
    def getBulbCount(cls):
        return cls.TotalBulbCount

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def bulbStatus(self):
        return self.isOn

class BulbDemo(object):
    @classmethod
    def main(cls,args):
        b = Bulb()
        print ("Bulb is on:{}".format(b.bulbStatus()))
        if b.bulbStatus() == False:
            print ("Bulb is OFF, switching it ON")
            b.turnOn()
        else:
            print ("Bulb is ON, switching it OFF")
            b.turnOff()
        print("Total bulb count: {}".format(Bulb.getBulbCount()))

if __name__ == '__main__':
    import sys
    BulbDemo.main(sys.argv)