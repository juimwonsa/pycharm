class Woman:
    def __init__(self, weight=None, height=None, iq=None):

        self.weight = weight
        self.height = height
        self.iq = iq

        if weight == None:
            self.weight = 60
        if height == None:
            self.height = 160
        if iq == None:
            self.iq = 100

    def eat(self):
        self.weight += 2
        self.height += 1

    def study(self):
        self.weight -= 1
        self.iq += 3

    def sleep(self):
        self.height += 2
        self.iq -= 2

    def status(self):
        print("현재 몸무게는 : ", self.weight)
        print("현재 키는 : ", self.height)
        print("현재 아이큐는 : ", self.iq)
