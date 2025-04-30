class Temperatura:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            print("Temperatura inexistente.")
            self.__celsius = 0
        else:
            self.__celsius = valor

temp = Temperatura(25)

print(f"Temperatura em °C: {temp.celsius}°C")
print(f"Temperatura em °F: {temp.fahrenheit}°F")

temp.celsius = 100
print(f"Temperatura em °C: {temp.celsius}")
print(f"Temperatura em °F: {temp.fahrenheit}")

try:
    temp.celsius = -300
except ValueError as e:
    print(e)