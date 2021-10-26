import math 

class Car: 
    def __init__(self, x=0, y=0, heading=0):
        self.x = x
        self.y = y
        self.heading = heading
        
    def turn(self, degrees):
        self.heading += degrees
        if self.heading > 360:
            self.heading -= 360
        elif self.heading < 0:
            self.heading += 360
        
    def drive(self, distance):
        self.x += distance * math.sin(math.radians(self.heading))
        self.y += distance * math.cos(math.radians(self.heading))
        
def sanity_check():
    crash_test = Car()
    crash_test.turn(90)
    crash_test.drive(10)
    crash_test.turn(30)
    crash_test.drive(20)
    
    print(f"Location: {crash_test.x}, {crash_test.y}")
    print(f"Heading: {crash_test.heading}")
    
    return crash_test

if __name__ == "__main__":
    sanity_check()
    