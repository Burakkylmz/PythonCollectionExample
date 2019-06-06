
print("Calculator")
print("---------------------------")
print("-------Operation Menu--------")
print("Toplama İşlemi İçin  --> 1'i")
print("Çıkarma İşilemi İçin --> 2'yi")
print("Çarpma İşlemi İçin   --> 3'ü")
print("Bölme İşlemi İçin    --> 4'ü")
print("------------------------ ---")

a = int(input("1.sayıyı girin: "))
b = int(input("2.sayıyı girin: "))

seçim = int(input("Lütfen bir işlem seçin: "))
if (seçim == "1"):
    print("{} + {} = {}".format(a,b,a+b))
elif (seçim == 2):
    print("{} - {} = {}".format(a,b,a-b))
elif (seçim == 3):
    print("{} x {} = {}".format(a,b,a*b))
elif (seçim == 4):
    print("{} / {} = {}".format(a,b,a/b))
else:
    print("Lütfen menüde ki işlemlerden birini seçin....")