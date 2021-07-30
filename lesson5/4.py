class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed=speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("машина поехала")
    def stop(self):
        print("машина остановилась")
    def turn_right(self):
        print("повернула (направо)")
    def turn_left(self):
        print("повернула (налево)")
    def show_speed(self):
        return f'Текущая скорость {self.name} -{self.speed}'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость {self.name} -{self.speed}')
        if self.speed > 40:
            return f'Скорость {self.name} для town car превышенна'
        else:
            return f'Скорость {self.name} для town car нормальная'
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость {self.name} -{self.speed}')
        if self.speed > 60:
            return f'Скорость {self.name} для WorkCar превышенна'
        else:
            return f'Скорость {self.name} для WorkCar нормальная'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name}  Машина из полицейского участка'
        else:
            return f'{self.name} Машина не из полицейского участка'

hyndai = TownCar(50,'Red','grandeu',False)
kia = SportCar (60,'white','kia',False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(hyndai.show_speed())
print(kia.show_speed())
print(lada.show_speed())
print(ford.show_speed())
print(hyndai.stop())
print(lada.turn_left())