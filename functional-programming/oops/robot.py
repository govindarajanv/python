# Robots

class Robot:
    TotalRobots = 0

    def __init__ (self, name):
        self.name = name
        Robot.TotalRobots += 1

    def __del__(self):
        print ("I am Robot {} dying. See you!!!".format(self.name))
        Robot.TotalRobots -= 1

    def greet(self):
        print ("I am Robot {}".format(self.name))
        if Robot.TotalRobots > 1:
            print ("Apart from me, there are {} Robots working".format(Robot.TotalRobots-1))
        else:
            print ("I am the only one Robot left")
    
    @staticmethod
    def TotRobots():
        return Robot.TotalRobots

    @classmethod
    def getRobotCount(self):
        return Robot.TotalRobots

robot1 = Robot('alpha')
robot1.greet()
print ("Total Robots:{}".format(Robot.TotRobots()))
print ("Get Total count of Robots:{}".format(Robot.getRobotCount()))
robot2 = Robot("Beta")
robot2.greet()
print ("Total Robots:{}".format(Robot.TotRobots()))
print ("Get Total count of Robots:{}".format(Robot.getRobotCount()))
robot3 = Robot("gamma")
robot3.greet()
print ("Total Robots:{}".format(Robot.TotRobots()))
print ("Get Total count of Robots:{}".format(Robot.getRobotCount()))

del robot1
del robot2
del robot3

    

