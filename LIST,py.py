# 16/03/2022
# 07-dars: LIST
# Muallif: Ramziddin Sayfiyev

#    List - ro'yxat 
#mevalar = [ "olma ", " anjir ", " shaftoli ", "o\'rik"]
#narxlar = [12000, 14000, 10500, 22690, 547, 84049, 8900, 7939, 89098, 75749]
#sonlar = [ 'bir', 'ikki', 3, 4, 5]
#ismlar = []
# IZOH: Indeks - tartib raqam [0] bilan boshlanadi ro'yxatni oxirgisini 
# [ -1 ] orqali aniqlasak bo'ladi va manfiy raqamlar bilan ham ro'yxatdagi 
# malumotlarni aniqlasak bo'ladi.

# .append() bu metod ro'yxatning oxiriga qiymat qo'shadi 
# .insert() bu metod ro'yxatning ma'lun bir qismiga qiymat qo'shadi 
# miso uchun o'rtasiga yoki boshiga --- buning uchun (0,) qavs ichiga 
# indeks qiymat raqami kiritilishi kerak.
#mevalar.append("tarvuz")
#mevalar.insert(3, "banan")
#mevalar.insert(0, "qovun")

#cars = [] # bo'sh ro'yxat yaratib olamiz . Ro'yxatga avtomabillarni birin-ketin qo'shamiz

#cars = [ 'lasetti', 'Nexia', 'Cobalt']

#cars = ["Lasetti", "Nexia", "Malibu", "Jiguli"]
'''  del ''' #--- list (ro'yxat) ichidan tanlangan indeks(qiymat orqali)ni o'chiradi
#del cars[0] # vahokazolar

'''  Remove ''' # indeks orqalimas tanlangan matn orqali o'chirib tashlaydi
#hayvonlar = ["It","Mushuk","Sigir","Qo'y","Quyon","Mushuk"]
#hayvonlar.remove('Mushuk')

'''Pop''' # Bu metod ro'yxatdan bitta qiymatni sug'urib oladi va boshqa 
# o'zgaruvchini ichiga joylab qo'yadi

#bozorlik = ["Un","Yog'","Shakar","Go'sht","Sabzi","Piyoz"]
#mahsulot = bozorlik.pop(3) #Ro'yxattdan go'shtni sug'irib olamiz
#print("Men " + mahsulot + " sotib oldim")
#print("Olinmagan mahsulotlar", bozorlik)
#mahsulot2 = bozorlik.pop()

#narxlar.remove(89098)
#narxlar[0]=narxlar[0]+3000

#ismlar = ["Botir", "Karim", "Ilhom","Shaxboz"]
#print(ismlar[0],"ertaga qaytib kelasanmi, o'rtoq?")
#print("Pasportingni nusxasini tashla", ismlar[1])
#print("Assalomu aleykum,", ismlar[2], "jo'rajon uzurda, u kuni borolmadim")
#print("Eee, san qanaysan", ismlar[3], "ishlaring yaxshimi")

sonlar = [12500, 8905,-900,6500,90.5]

t_shaxslar = ["Alisher Navoiy","Abu Rayhon Beruniy","Jaloliddin Manguberdi"]
z_shaxslar = ["Ilon Mack","Bill Geyt","Robert Kiyosaki"]
print("Men tarixiy shaxslardan " + t_shaxslar.pop(1) + " bilan,")
print("zamonaviy shaxslardan esa - " + z_shaxslar.pop(0) + " bilan suhbatlashishni istar edim")

friends = []
#print(sonlar)

