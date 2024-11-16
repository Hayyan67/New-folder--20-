class BMW:
    def start_engine(self):
        return "BMW engine started"

    def stop_engine(self):
        return "BMW engine stopped"


class Ferrari:
    def start_engine(self):
        return "Ferrari engine started"

    def stop_engine(self):
        return "Ferrari engine stopped"



def car_test(car):
    print(car.start_engine())
    print(car.stop_engine())



bmw = BMW()
ferrari = Ferrari()


car_test(bmw)
car_test(ferrari)
