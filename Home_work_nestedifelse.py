#
#           Ornegin : Kullanicidan cinsiyetini ve yasini alin,
#           Kadin, 60 yas ve uzeri , Erkek 65 yas ve uzeri emekli olabilir.
#           Cinsiyet ve yasini dikkate alarak “Emekli olabilirsin”
#           veya “Emekli olmak icin .. Yil daha calisman gerekir” yazdirin.
#

cins = input("Lütfen cinsiyetinizi E/K olarak giriniz : ")

yas = input("Lütfen yaşınızı giriniz : ")
yas = int(yas)

if cins == "E" and cins == "e":
    if yas < 0 or yas > 90:
        print("geçersiz yaş girişi yaptınız.")
    elif yas < 65:
        print("Emekli olmak için ", (65 - yas), " yıl daha çalışmalısın.")
    else:
        print("Emekli olabilirsin.")
elif cins == "K" and cins == "k":
    if yas < 0 or yas > 90:
        print("geçersiz yaş girişi yaptınız.")
    elif yas < 60:
        print("Emekli olmak için ", (60 - yas), " yıl daha çalışmalısın.")
    else:
        print("Emekli olabilirsin.")
else:
    print("Hatalı cinsiyet girişi yaptınız, lütfen tekrar deneyiniz.")

#BECEREMEDİK
