class House:
    def __init__(self, name, number_of_floors):
        self.nams = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        new_floor = int(new_floor)
        floor = 0
        if new_floor > self.number_of_floors or new_floor < 1:
            print('"Такого этажа не существует"')
        else:
            while new_floor > floor:
                floor += 1
                print(floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

h3 = House('9-этажное здание', 9)
h3.go_to(7)
h3.go_to(99)