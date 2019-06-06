
a = int(input("a değeirni giriniz: "))
b = int(input("b değeirni giriniz: "))
c = int(input("c değeirni giriniz: "))

delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5 / (2 * a))
x2 = (-b + delta ** 0.5 / (2 * a))

print("Birinci Kök: {}\nİkinci Kök: {}\n".format(x1,x2))