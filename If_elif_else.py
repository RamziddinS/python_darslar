# 07/04/2022
# 11 - DARS: IF - ELIF - ELSE 
# Muallif: Ramziddin Sayfiyev

#son = -72 
#if son <0 :
   # print("Manfiy son")
#else:
    #print("Musbat son")
    
#yosh = int(input("Yoshingiz nechida? "))
#if yosh<4:
 #   narx = 0
#elif yosh<=12:
 #   narx = 5000
#elif yosh<16:
 #   narx = 8000
#else:
#    narx = 10000
#print(f"Sizga kirish {narx} so'm!")
     
#kun = input("Bugun qaysi kun?\n>>>")
#if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#    print("Bugun dam olish kuni!")
#else:
 #   print("Bugun ish kuni!")
 
 
#kun = input("Bugun qaysi kun?\n>>>")
#harorat = float(input("Havo harorati qanday?\n>>>"))
#if (kun.lower()=="yakshanba" or kun.lower()=="shanba" ) and harorat>30:
#    print("Cho'milgani kettik!")
#elif(kun.lower()=="yakshanba" or kun.lower()=="shanba" ) and harorat<30:
#    print("Uyda dam olamiz!")
          # Boolean -- mantiqiy ma'lumot turi
#narx = 15000 # mijoz 15000 so'mga narsa oldin
#choy = True # mijoz choy ham oldi
#salat = False # mijoz salat olmadi Agar biz mana bu shartni ham True ga o'zgartirsak mijoz sajat ham olgan hisoblanardi
#if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa 
#     narx = narx+10000 # narxga 10000 so'm qo'shamiz
#elif choy or salat: #agar choy yoki salat olgan bo'lsa
#     narx = narx+5000  # narxga 5000 so'm qo'shamiz
# True va False ni ham biz o'zgaruvchilarning qiymati qilib qo'shishimiz mumkin ekan
# bular ham mantiqiy malumot turlari hisoblanadi Bu qiymatlarning javoblari aniq bo'ladi  

#print(f"Jami {narx} so'm") # yakuniy narxni chiqaramiz

# ELIF ELSE metodlaridagi kamchilik bunda faqat bitta shartni(tekshirganidan) bajarganidan keyin 
# qolgan shartlarni bajarmaydi(tekshirmaydi.)
 
#narx = 15000
#hoy = 1 # True va False o'rniga biz  (1) yoki (0) ham qo'yib ketishimizam mumkin
#salat = 0
#non = 1
#kompot = 1
#assorti = 1
# Quyidagi shartlar har biri alohida tekshiriladi va bir-biriga bog'liq emas
#if choy: #agar choy sotib olsa
#    print("Mijoz choy sotib oldi")
#    narx = narx + 3000
#f salat: # agar salat sotib olsa
#    print("Mijoz salatsotib oldi")
#    narx = narx + 5000
#if non: #agar mijoz non sotib olsa
#   print("Mijoz non sotib oldi")
#    narx = narx + 2000
#if kompot: # agar mijoz kompot sotib 
#    print("Mijoz kompot sotib oldi")
#    narx = narx + 5000
#if assorti: #agar mijoz assorti sotib olsa
#    print("Mijoz assorti sotib oldi")
#    narx = narx + 15000
#print(f"Jami {narx} so'm")    
    # YUQORIDAGI SHARTLAR HAR BIRI ALOHIDA MUSTAQIL HAR BIRI TEKSHIRILADI
    #BU SHARTLARDAN BIRORTASI BAJARILSA HAM BALARILMASA HAM
    # KEYINGI SHARTGA O'TADI VA O'ZIDAN KEYINGISINI HAM TEKSHIRADI
    # HECH BIR SHART TASHLAB O'TIB KETILMAYDI(ELIF ELSE GA O'XSHAB)
    
#menu = ['osh','qozonkobob','shashlik','norin','somsa']
#'manti' in menu # menuda manti bormi?
#
#menu = ['osh','qozonkobob','shashlik','norin','somsa']
#ovqat = input("Nima ovqat yeysiz?\n>>>")
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi.") 
#else:
#    print("Afsuski bizda bunday ovqat yo'q.")

#menu = ['osh','qozonkobob','shashlik','norin','somsa']
#buyurtmalar = ['osh','somsa','manti','shashlik']
#if buyurtmalar: # Ro'yxatda biror element bo'lsa bu element True qaytaradi
#  for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor!")
#    else:
#        print(f"Kechirasiz, menuda {taom} yo'q")  
#else:# Agar ro'yxat bo'sh bo'sh bo'lsa
#    print("Savatchangiz bo'sh!")

#son = int(input("Juft son kiriting:"))
#if son%2:
#    print("Bu son juft emas")
#else:
#    print("Rahmat")

#yosh = int(input("Yoshingiz nechchida?\n>>>"))
#if yosh<4 or yosh>60:
#    print("Sizga muzeyga kirish bepul!")
#elif yosh<18:
#    print("Sizga muzeyga kirish 10000 so'm!")
#else:
#    print("Sizga muzeyga kirish 20000 so'm!")           
 

#son1 = int(input("Birinchi sonni kiriting!\n>>>"))
#son2 = int(input("Ikkinchi sonni kiriting!\n>>>"))
#if son1<son2: 
#   print(f"{son1} soni {son2} sonidan kichkina") 
#elif son1>son2:
#    print(f"{son1} soni {son2} sonidan katta")
#else:
#    print("Sonlar teng ekan!")


#mahsulotlar = ["non", "shakar", "un", "anor", "olma", "uzum", "olxori", "anjir", "qulupnay","o'rik", "shaftoli"]
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:"))


#bor_mahsulotlar = []
#mavjud_emas = []    
#for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            bor_mahsulotlar.append(mahsulot)
#        else:
#            mavjud_emas.append(mahsulot)

#if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q: ")
#    for mahsulot in mavjud_emas:
#      print(mahsulot)     
#else:
#      print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
     
#foydalanuvchilar = ["anvar","rustam","yusuf","ramziddin","sardor"]
#login = input("Yangi login tanlang:")
 
#if login in foydalanuvchilar:
#    print("Login band, yangi login tanlang")     
#else:
#    print("Xush kelibsiz, foydalanuvchi!")

#son = int(input("Istalgan butun son kiriting:\n>>>"))

#for n in range(4,11):
#    if not (son%n):
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

        
      
                            
  
      
