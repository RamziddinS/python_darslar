# 06-dars. STRING (MATN)
# sana: 13/03/2022
# Muallif: Ramziddin

#shahar = "Qo'qon"
#viloyat = 'Вухоро' #1.. O'zgaruvchilar ichidagi malumot har xil alifboda bo'lishi m/n
#matn = "Men ertaga o'zimni 🚙 da ketaman"
#smayl = '😂'
#print(matn) 

# STRING USTIDA BAJARILADIGAN AMALLAR
#kitob = 'Adabiyat'
#print(" men yoshligimdan sevib o'qiydiganim "  + kitob)

#ism = "Sayfiddin"
#familiya = "Sayfiyev"
#print( ism  +  familiya )# ismlar orasida bo'shliq paydo qilish uchun 
# quyidagi amalni bajarish kerak
#print(ism + ' ' + familiya)
 
# f-string matnlarni jamlash uchun foydalaniladi va aynan {} manashu 
#belgidan foydalaniladi

#ism = 'Sayfiddin'
#familiya = 'Sayfiyev'
#ism_sharif = f"{ism} {familiya}" 
#print(ism_sharif)

#ism = "Abdujabbor"
#familiya = "Narimonov"
#print(f"mening ismim {familiya},{ism} {familiya}")
# MAXSUS BELGILAR

# \t Belgisi uzun bo'shliq qoldiradi
#print("Hello \tworld")

# STRING METODLAR

#ism = "james"
#familiya = "bond"
#ism_sharif = f'{ism} {familiya}'
#print(ism_sharif.upper())
# BU .upper () metodi stringdagi harflarni barchasini kattaga o'giradi buni 
#sonlarda qo'llab bo'lmaydi. Bu metodni print bilan bajarganda
# O'zgaruvchini ichidagi strig umuman o'zgarmaydi faqat natijagina o'zgaradi.
#lekin o'zgaruchini o'zi bilan bajarilganda ichidagi string o'zgaradi.
#Misol:
#ism_sharif = ism_sharif.upper() 
   
#print(ism_sharif.lower())
# .lower () metodi stringdagi harflarni hammasini kichkina harflarga o'giradi.

#print(ism_sharif.title()) 
# .title bu metod Matndagi har bir har bir so'zning birinchi harfini
#katta harfga o'giradi

#print(ism_sharif.capitalize())
# Bu .capitalize() metodi matndagi faqatgina
# birinchi harfni katta harfga o'giradi
#meva = "    olma    "
#print("Men " + meva.lstrip() + " yaxshi ko'raman") #bu metod chap tarafdagi bo'shliqni olib tashlaydi
#print("Men " + meva.rstrip() + " yaxshi ko'raman") #bu metod o'ng tomondagi bo'shliqni olib tashlaydi
#print("Men " + meva.strip() + " yaxshi ko'raman") #bu metod ikkala tomondagi bo'shliqni olib tashlaydi
#print("Men " + meva + " yaxshi ko'raman") # Bu metodlar matn ichida keladigan kerakli so'zlarni yoki 
#kalit so'zlarni qidirishda bo'shliqlar bo'ladi shu bo'shliqlarni yo'qotish uchun foydalaniladi'

# INPUT Izoh: foydalanuvchidan ham qandaydir malumot kiritishni talab qiladi.

#ism = input("Ismingiz nima?")
#print("Assalomu aleykum," + ism)
#ism = input("Ismingiz nima?\n>>>")
#print("Assalomu aleykum," + ism.title())