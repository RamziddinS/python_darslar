# 30/03/2022
# 09-Dars: FOR LOOP
# Muallif: Sayfiyev Ramziddin

#mehmonlar = ["Jobir", "Sobir", "Qobil", "Nosir", "G'ulom"]
#for mehmon in mehmonlar:# Bu abonet hamma dasturlash tillarida qo'llaniladi 
# va bu abonent ma'lum bir kodni qayta-qayta takrorlash uchun ishlatiladi 
# Bunda albatta ( : ) ikki nuqta oxirida qo'yilishi kerak
    #print("Salom", mehmon)# Matnning o'ngga surib yozilgan qismi Siklning Badani hisoblanadi
    #print("Xayr", mehmon)
#mehmonlar = ["Jobir", "Sobir", "Qobil", "Nosir", "G'ulom"]
#for mehmon in mehmonlar:
    #print(f"Hurmatli {mehmon}, sizni 21 iyun kuni nahorga oshga taklif qilamiz")
    #print("Hurmat bilan, Sayfiyevlar oilasi\n")

#sonlar = list(range(1,11))    
#for son in sonlar:
    #print(f"{son} ning kvadrati {son**2} ga teng\n")

#sonlar = list(range(11))    
#sonlar_kvadrati = []
#for son in sonlar : #sonlardagi har bir son uchun
    #sonlar_kvadrati.append(son**2) # uning kvadratini hisoblab 
    # Uni sonlar_kvadratiga joylashtir 
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = [] # Bo'sh ro'yxat
#print(" 5 ta eng yaqin do'stingiz kim?")  
#for n in range(5): # n bu yerdan 0 dan 4 gacha bo'lgan sonlar
# qiymatini oladi 
      #dostlar.append(input(f"{n+1 }- do'stingizning ismini kiriting:\n>>> "))
#print(dostlar)  

#ismlar = ["Sardor", "Sayfiddin", "Ramziddin", "Botir", "Damirjon", "Bahrom", "Baxtishod", "Doston"]
#for ism in ismlar:
#    print(f"{ism},ertadan Ro'zayi Ramazon boshlanadi g'aflatda qolmang!\n>>>")
    
#print("Kod 8 marta takrorlandi")

#toq_sonlar = range(11,100,2)
#for toq_son in toq_sonlar:
#    print(f" {toq_son**3}\n" ) Har bir 10dan 100 gacha bo'lgan toq sonlarning kubini alohida qatorga chiqarish.

#kitoblar = [] # Bo'sh ro'yxat
#print("5 ta eng sevimli kitobingiz qaysi?")
#for n in range(5):
 #     kitoblar.append(input(f"{n+1}- kitobni nomini kiriting:\n>>>"))
#print( kitoblar)     

suhbatdoshlar = [] # bo'sh ro'yxat 
n_people = int(input("Bugun nechta odam bilan suhbatlashdingiz?>>>"))
for n in range(n_people):
    suhbatdoshlar.append(input(f"{n+1}- suhbatlashgan odamingiz kim edi:\n>>>"))
print(suhbatdoshlar)