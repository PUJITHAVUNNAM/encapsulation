class Engine:
    def __init__(self):
        self.__temperature = 30

    def start(self):
        self.__temperature += 40
        print("Engine started")

    def cool(self):
        self.__temperature -= 20
        if self.__temperature < 30:
            self.__temperature = 30
        print("Engine cooled")


class Car:
    def __init__(self):
        self.__engine = Engine()

    def start_car(self):
        self.__engine.start()

    def cool_engine(self):
        self.__engine.cool()


car = Car()

car.start_car()
car.cool_engine()