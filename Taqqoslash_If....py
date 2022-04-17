# 03/04/2022
# 10-Dars: TARMOQLASH
# Muharrir: Ramziddin Sayfiyev

#avtolar = ["audi", "bmw", "volvo", "kia", "hyundai"]

#for avto in avtolar: # avtolar ichidagi har bir avto uchun
    #if avto == "bmw": # ... Agar avto bmw ga teng bo'lsa ...
     #   print(avto.upper()) # avto nomini hamma harflarini katta harfga...
    #else: #aks holda...
        #print(avto.title()) # avto nomini faqat birinchi harfini katta qilib yoz...
        
#ism = "Ali" # matnlarni solishtirishda iloji bo'lsa hammasini bitta ko'rinishga keltirib olishimiz kerak
#ism.lower() == "ali" #aks holda xato natija ham olishimiz mumkin

#ism = input("Ismingiz nima?\n>>>") # Foydalanuvchini ismini so'raydi
#if ism.lower() != "ali": # barcha harflarni kichikka aylantirib agar Aliga teng bo'lmasa...
 #   print(f"Uzr, {ism.title()} biz Alini kutyapmiz.") # bu amalni bajaradi 
#else:# aks holda Teng bo'lsa ...
    #print("Salom Ali")  # bu amalni bajaradi

#javob = float(input("12*6 nechiga teng?>>>"))
#if javob != 72:
 #    print("Javob xato!")  

#yosh = int(input("Yoshingiz nechchida?>>>"))
#if yosh >= 18:# yosh 18 dan katta yoki teng bo'lsa
#    print("Xush kelibsiz!") # shu javob
#else:# aks holda 
    #print("Kirish mumkin emas!") #bu javob
    
#login = input("Yangi login tanlang!")
#if len(login)<=5:# Login uzunligini tekshiramiz
 #     print("Login 5 ta harfdan ko'proq bo'lishi kerak!")

#yil = int(input("Tug'ilgan yilingizni kiriting:"))
#if 2022-yil < 18:#Foydalanuvchining yoshini hisoblaymiz
    #print(f"Yoshingiz {2022-yil} da ekan.")
    #print("Kirish mumkin emas!")
#else:
    #print("Xush kelibsiz!")    
#yosh = int(input("Yoshingiz nechchida?>>>"))
#if yosh > 65: print("Siz COVID-19 risk guruhida ekansiz")    
 # Bu yerda bir qatorda ham shartni ham shartning badanini kirittik.   

#x, y = 25, 50 # ikkita qiymat x=25 y=50 
#print("x>y") if x>y else print("x<y")# Manashu ko'rinishda biz ..If.. ..Else..
# bog'lamasini bir qatorda joylashtirishimiz mumkin 
# If  ni badani if dan oldin  Else  ni badani esa else dan keyin keladi...

#cars = ['toyota', 'mazda', 'hyundai','gm', 'kia']
#for car in cars:
    #print(car.title())
 #   if car != 'gm':
  #      print(car.title())
   # else:
    #    print(car.upper())
#login = input("Login ismingizni kiriting!\n>>>")
#if login.lower() == "admin":
 #   print(" Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
 #   print(f"Xush kelibsiz, {login.title()}!")

#x = int(input("Birinchi sonni kiriting!\n>>>"))
#y = int(input("Ikkinchi sonni kiriting!\n>>>"))
#if x == y: print(f"Sonlar teng:{x}={y}")
    
#x = int(input("Istalgan sonni kiriting!"))
#print(f"Manfiy son:{x}") if x < 0 else print(f"Musbat son:{x}")

#son = float(input("Istalgan sonni kiring!\n>>>")) 
#print(son**(1/2)) if son>0 else print("Musbat son kiriting!")