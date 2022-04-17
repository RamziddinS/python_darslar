# Dasturlash asoslari
# 08-Dars: LISTS
# Muallif: Ramziddin Sayfiyev

# TARTIBLASH
#cars =["Bmw","mercedes benz","volvo","general motors","tesla","audi"]
# cars.sort() # SORT-Bu metod ro'yxatni alifbo ketma ketligida terib chiqadi
# print(cars) # Katta harflar kichkina harflardan oldinda turadi  
#cars.sort(reverse=True) # Bu argumend orqali biz biz ro'yxatninteskari tartibda taxlaymiz
#print(sorted(cars)) # Sorted bu metod orqali biz asl ro'yxatga tegmagan holda 
# consolda ro'yxatni tartib bilan teramiz
#print(sorted(cars,reverse=True)) # bu orqali biz ro'yxatni colsolda teskari tartibda joylashtiramiz
# BU METODLARNI SONLARDA HAM QO'LLASHIMIZ MUMKIN
#sonlar = [45, 26, 1234, 56.9, 567,-34, 0.45]
#cars.reverse() # Bu metod orqali biz ro'yxatni teskarisiga aylantiramiz

#len(cars) # bu funksiya orqali ro'yxatni uzunligini o'lchaymiz lengs - uzunlik
#uzunlik = len(cars)

#sonlar = list(range(0,10)) # range bu metod malum bir oraliqdagi sonlarni qaytaradi

#toq_sonlar = list(range(1,20,2))
#juft_sonlar = list(range(0,20,2))
#sanash= list(range(0,100,10))
#max_qiymat = max(juft_sonlar)

#narxlar = [12000, 5600, 9000, 5450, 4500, 23000, 10000]
# MAX Bu metod sonlar ichidan eng kattasini topadi
# MIN Bu metod sonlar ichidan eng kichigini topib beradi
# SUM BU metod qiymatlarning yig'indisini chiqarib beradi
#arzon = min(narxlar)
#qimmat = max(narxlar)
#jami = sum(narxlar)
#print("Eng arzon narx", arzon, ". Eng qimmati", qimmat, ", Ularning jami qiymati", jami)

#RO'YXATNI KESISH
#print(cars[0])
#print(cars[4])
# print(cars[0:3]) # Ro'yxatdan malum bir qiymatni kesib olish uchun  malum bir
# qiymatlarning indekslarini olamizdaularni orasini(:) bilan ajratamiz
#print(cars[2:6]) 
#print(cars[:3])
#print(cars[1:])#faqat bitta indeksni belgilab ikki nuqta 
#qo'yadigan bo'lsak ham ro'yxatning malum bir qismini ajratib beradi

# RO'YXATDAN NUSXA OLISH
#my_cars = cars # Bundan ro'yxatdan nusxa olinmadi balki ikkita
# bir xil (turli xil) nomdagi o'zgaruvchi vujudga keldi. Bunday holatda
# bitta o'zgaruvchidan qaysidir qimmatni olib tashlasak yoki qo'shsak
# ikkala o'zgaruvchida ham bir xil o'garish bo'ladi chunki biz 
# nusxa ko'chirmadik

#my_cars = cars[:] # Mana bu holatda esa endi nusxa ko'chirildi

#     Ro'yxatning yangi turi

# TUPLE bu o'zgarmas ro'yxat degani. Bunda ro'yxat yaratganda
# to'rtburchak qavsmas dumaloq qavs qo'yiladi  
#Misol:
#toys = ('bus','car','bear','dino','snake','lizard') 
#toys[0] = "teddy" #Bu elementlarni qo'llab bo;lmaydi'
#toys.append('teddy')# Bu elementni ham qo'llab bo'lmaydi

# Faqat bir xil holatda  TUPLE ni o'zgartirsa bo'ladi Misol:
#toys = list(toys) # Tuple ni listga o'girib olganimizdan keyin
# uning ichidagi qiymatlarni bemalol o'zgartira olamiz 
# Bu o'zgaruvchini yana Tuple ga almashtirmoqchi bo'lsak:
    
#toys = tuple(toys) #mana shu amalni bajarishimiz kerak    

#davlatlar = ["O'zbekiston", "Rossiya", "Ukraina", "Qozoqiston","Turkiya","Berlin"]
#print(davlatlar)
#sonlar = list(range(120,1200,2))
#print(sonlar)
#print(min(sonlar))# sonlarning eng kichik qiymati
#print(max(sonlar)) # sonlarning eng katta qiymati
#print(sum(sonlar)) #sonlarning jami yig'indisi qiymati 
#print(max(sonlar) - min(sonlar))#eng katta va kichik qiymatning ayirmasi
#print(len(sonlar))# sonlarning uzunligi Umumiy sanog'i
#print(sonlar[530:550])

taomlar = ["Osh", "Somsa", "Chuchvara","Manti","Xonim"]
nonushta = taomlar[:]
#print(nonushta.pop(1))
#print(nonushta)
#print(nonushta.pop(0))
#print(nonushta)
print(nonushta.pop(1))
print(nonushta.pop(1))
print(nonushta.pop(1))
print(nonushta.pop(1))
print(nonushta)
print(taomlar)