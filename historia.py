import random

class Event:
    def __init__(self, d, n):
        self.date = d
        self.name = n

points = 0
arr = [
Event("1177", "Złamanie zasady senioratu - objęcie tronu krakowskiego przez Kazimierza Sprawiedliwego"),
Event("1227", "Zjazd w Gąsawie, śmierć Leszka Białego - złamanie zasady pryncypatu"),
Event("1226", "Sprowadzenie Krzyżaków do Polski"),
Event("1238", "Śmierć Henryka Brodatego"),
Event("1241", "Pierwszy najazd mongolski"),
Event("1241", "Bitwa pod Legnicą"),
Event("1253", "Kanonizacja biskupa Stanisława ze Szczepanowa"),
Event("1259", "Drugi najazd mongolski"),
Event("1283", "Podporządkowanie sobie Prusów przez Krzyżaków"),
Event("1287", "Trzeci najazd mongolski"),
Event("1288", "Zajęcie Krakowa przez Henryka Probusa"),
Event("1290", "Śmierć Henryka Probusa"),
Event("1291", "Zajęcie ziemi krakowskiej przez Wacława II"),
Event("1295", "Koronacja Przemysła II na króla Polski przez abp. gnieźnieńskiego Jakuba Świnkę"),
Event("1296", "Zamordowanie Przemysła II w Rogoźnie"),
Event("1300", "Koronacja Wacława II na króla Polski przez abp. gnieźnieńskiego Jakuba Świnkę"),
Event("1304", "Powrót do kraju Władysława Łokietka. Wybuch powstania antyczeskiego przeciw rządom Wacława II"),
Event("1305", "Śmierć Wacława II"),
Event("1306", "Śmierć Wacława III"),
Event("1306", "Objęcie władzy w Krakowie przez Władysława Łokietka"),
Event("1308", "Oblężenie Gdańska przez Brandenburczyków"),
Event("1311", "Powstanie mieszczan pod wodzą wójta Alberta przeciwko Łokietkowi"),
Event("1320", "Koronacja Władysława Łokietka na króla Polski"),
Event("1325", "Sojusz Łokietka z Litwą"),
Event("1331", "Bitwa pod Płowcami"),
Event("1333", "Śmierć Władysława Łokietka"),
Event("1333", "Koronacja Kazimierza Wielkiego na króla Polski"),
Event("1335", "Zjazd w Wyszehradzie"),
Event("1343", "Pokój wieczysty w Kaliszu"),
Event("1348", "Pokój w Namysłowie"),
Event("1349", "Podporządkowanie sobie Rusi Czerwonej przez Kazimierza Wielkiego"),
Event("1362", "Ukazanie się Statutu piotrkowskiego i Statutu wiślickiego"),
Event("1365", "Odwiedziny Kazimierza Wielkiego w Malborku"),
]
s = len(arr)
while len(arr) > 0:
    indx = random.randint(0, len(arr) - 1)
    print(arr[indx].name)
    answer = input()
    if(answer == arr[indx].date):
        points += 1
        print("Dobrze!")
    else:
        print("Źle. Dobra odpowiedź to " + arr[indx].date)
    arr.pop(indx)
print("-------------")
print(str(points) + " na " + str(s) + ", " + str(float(points/s * 100)) + "%")