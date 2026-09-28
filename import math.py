import math
user_input=input("Введите строку:")
parts= user_input.split('|')
diameter_str=parts[1].split('=')[1].strip().replays('m','').strip()
diameter=float(diameter_str)
height_str=parts[2].split('=')[1].strip()
height=float(height_str)
radius=diameter/2
volume=math.pi*math.pow(radius,2)*height
volume_floor=math.floor(volume)
print("\n---ОТЧЕТ---")
print(f"Радиус:{radius}м")
print(f"Обьем(точный):{volume}куб.м")
print(f"Обьем(округленный вниз):{volume_floor}куб.м")
if __name__=="__main__":main()