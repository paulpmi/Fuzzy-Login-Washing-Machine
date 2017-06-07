from random import random
from random import randint

class texture:
    def __init__(self):
        self.startPoint = random()
        self.evaluate = None

        self.verySoft = None
        self.soft = None
        self.normal = None
        self.resistant = None

        self.checkResistance()

    def checkResistance(self):
        #self.verySoft = min([(self.startPoint-0)/0.2, (0.4-self.startPoint)/0.2])
        self.verySoft = (0.4-self.startPoint)/0.2
        self.soft = min([(self.startPoint -0.2)/0.2, (0.8-self.startPoint)/0.4])
        self.normal = min([(self.startPoint - 0.3)/0.4, (0.9-self.startPoint)/0.2])
        self.resistant = (self.startPoint-0.7)/0.2

        #self.resistant = min([(self.startPoint - 0.7)/0.2, (1-self.startPoint)/0.1])
class load:
    def __init__(self):
        self.startPoint = random()*5
        self.evaluate = None

        self.small = None
        self.medium = None
        self.high = None

        self.checkLoad()

    def checkLoad(self):
        #self.small = min([(self.startPoint - 0) / 1, (2 - self.startPoint) / 1])
        self.small = 2-self.startPoint
        self.medium = min([(self.startPoint - 1) / 1.5, (4 - self.startPoint) / 2.5])
        self.high = (self.startPoint-3)
        #self.high = min([(self.startPoint - 3) / 1, (5 - self.startPoint) / 1])

class cycle:
    def __init__(self, texture, load):
        self.texture = texture
        self.load = load

        self.evaluate = None

        self.delicate = None
        self.easy = None
        self.normal = None
        self.intense = None

        self.checkCycle()

        self.vector = (0.04*self.texture.verySoft + 0.14*self.texture.soft + 0.28*self.texture.normal+0.42*self.texture.resistant + 0.64*self.load.small+0.78*self.load.medium+0.92*self.load.high)/(self.texture.verySoft+self.texture.soft+self.texture.normal+self.texture.resistant+self.load.small+self.load.medium+self.load.high)
        print('vector: ', self.vector)
        self.solution()


    def checkCycle(self):

        textures = []
        for i in [self.texture.verySoft, self.texture.soft, self.texture.normal, self.texture.resistant]:
            #print(i)
            if i > 0:
                textures.append(i)

        texture = min(textures)


        loads = []
        for i in [self.load.small, self.load.medium, self.load.high]:
            if i > 0:
                loads.append(i)

        load = min(loads)


        fraction = texture/load
        print('texture: ', texture, 'load: ', load, 'fraction: ', fraction)

        self.delicate = min([(fraction - 0) / 0.2, (0.4 - fraction) / 0.2])
        self.easy = min([(fraction - 0.2) / 0.3, (0.8 - fraction) / 0.3])
        self.normal = min([(fraction - 0.3) / 0.4, (0.9 - fraction) / 0.3])
        self.intense = min([(fraction - 0.8) / 0.1, (1 - fraction) / 0.1])

    def solution(self):
        #self.evaluate = max([self.delicate, self.easy, self.normal, self.intense])
        if 0 <= self.vector <= 0.4:
            self.evaluate = "delicate"
        elif 0.2 <= self.vector <= 0.8:
            self.evaluate = "easy"
        elif 0.3 <= self.vector <= 0.9:
            self.evaluate = "normal"
        elif 0.7 <= self.vector <=1:
            self.evaluate = "intense"
        else:
            self.evaluate = "delicate2"


class Controller:
    def __init__(self):
        pass

    def run(self):
        for i in range(0,30):
            t = texture()
            l = load()
            c = cycle(t,l)

            print('verySoft: ', t.verySoft, ' soft: ', t.soft, ' normal: ',t.normal, ' resistance: ', t.resistant)
            print('small: ', l.small, ' medium: ', l.medium, ' high: ',l.high)
            print('delicate: ', c.delicate, ' easy: ',c.easy, ' normal: ',c.normal, ' intense: ',c.intense)
            print(c.evaluate, ' ', c.vector)
            print('')

class View:
    def __init__(self,c):
        self.c = c
        self.c.run()

c= Controller()
v = View(c)
