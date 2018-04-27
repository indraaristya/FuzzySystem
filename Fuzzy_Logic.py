datasetEmosi = [97,36,63,82,71,79,55,57,40,57,77,68,60,82,40,80,60,50,100,11]
datasetProvokasi = [74,85,43,90,25,81,62,45,65,45,70,75,70,90,85,68,72,95,18,99]
datasetHasil = ["Ya","Ya","Tidak","Ya","Tidak","Ya","Tidak","Tidak","Tidak","Tidak","Ya","Ya","Tidak","Ya","Tidak","Ya","Tidak",
"Ya","Tidak","Ya"]

datatestEmosi = [58,68,64,57,77,98,91,50,95,27]
datatestProvokasi = [63,70,66,77,55,64,59,95,55,79]
datatestHasil = ["Tidak","Tidak","Tidak","Tidak","Tidak","Tidak","Tidak","Tidak","Tidak","Tidak"]

def FuzzyProg(a, b):
    emosi = a
    tidakEmosi = 0
    emosiSedang = 0
    sangatEmosi = 0

    provokasi = b
    tidakProvokasi = 0
    provokasiSedang = 0
    terProvokasi = 0

    hoaxTemp = 0
    hoax = 0
    tidakhoaxTemp = 0
    tidakhoax = 0


    #Tahap Fuzzification
    if (emosi <= 53):
        tidakEmosi = 1
        emosiSedang = 0
        sangatEmosi = 0
    elif (emosi >=79):
        tidakEmosi = 0
        emosiSedang = 0
        sangatEmosi = 1
    elif (emosi == 61):
        tidakEmosi = 0
        emosiSedang = 1
        sangatEmosi = 0
    else:
        if (emosi > 53 and emosi < 61):
            tidakEmosi = -(emosi-61)/(61-53)
            emosiSedang = (emosi-53)/(61-53)
            sangatEmosi = 0
        elif (emosi > 61 and emosi < 79):
            tidakEmosi = 0
            emosiSedang = -(emosi-79)/(79-61)
            sangatEmosi = (emosi-61)/(79-61)


    if (provokasi <= 57):
        tidakProvokasi = 1
        provokasiSedang = 0
        terProvokasi = 0
    elif (provokasi >= 85):
        tidakProvokasi = 0
        provokasiSedang = 0;
        terProvokasi = 1
    elif (provokasi == 71):
        tidakProvokasi = 0;
        provokasiSedang = 1;
        terProvokasi = 0;
    elif (provokasi > 57 and provokasi < 71):
        tidakProvokasi = -(provokasi-71)/(71-57)
        provokasiSedang = (provokasi - 57)/(75-57)
        terProvokasi = 0
    elif (provokasi > 71 and provokasi < 85):
        tidakProvokasi = 0
        provokasiSedang = -(provokasi-85)/(85-71)
        terProvokasi = (provokasi - 71)/(85-71)


    #Tahap Inference
    if (tidakEmosi != 0):
        if (tidakProvokasi != 0):
            tidakhoaxTemp = min(tidakEmosi,tidakProvokasi)
            if (tidakhoax < tidakhoaxTemp):
                tidakhoax = tidakhoaxTemp
        if (provokasiSedang != 0):
            tidakhoaxTemp = min(tidakEmosi, provokasiSedang)
            if (tidakhoax < tidakhoaxTemp):
                tidakhoax = tidakhoaxTemp
        if (terProvokasi != 0):
            hoaxTemp = min(tidakEmosi,terProvokasi)
            if (hoax < hoaxTemp):
                hoax = hoaxTemp


    if (emosiSedang != 0):
        if (tidakProvokasi != 0):
            tidakhoaxTemp = min(emosiSedang,tidakProvokasi)
            if (tidakhoax < tidakhoaxTemp):
                tidakhoax = tidakhoaxTemp
        if (provokasiSedang != 0):
            tidakhoaxTemp = min(emosiSedang,provokasiSedang)
            if (tidakhoax < tidakhoaxTemp):
                tidakhoax = tidakhoaxTemp
        if (terProvokasi != 0):
            hoaxTemp = min(emosiSedang,terProvokasi)
            if (hoax < hoaxTemp):
                hoax = hoaxTemp


    if (sangatEmosi != 0):
        if (tidakProvokasi != 0):
            tidakhoaxTemp = min(sangatEmosi,tidakProvokasi)
            if (hoax < tidakhoaxTemp):
                tidakhoax = tidakhoaxTemp
        if (provokasiSedang != 0):
            hoaxTemp = min(sangatEmosi, provokasiSedang)
            if (hoax < hoaxTemp):
                hoax = hoaxTemp
        if (terProvokasi != 0):
            hoaxTemp = min(sangatEmosi, terProvokasi)
            if (hoax < hoaxTemp):
                hoax = hoaxTemp


    #Tahap Defuzzification
    strhoax = str(hoax)
    strtidakhoax = str(tidakhoax)
    nilai1 = (hoax * 40)
    nilai2 = (tidakhoax * 20)
    jumlah = hoax + tidakhoax
    nilai = (nilai1 + nilai2)/jumlah


    if (nilai >= 22):
        kesimpulan = 'Ya'
    else:
        kesimpulan = 'Tidak'

    print(kesimpulan)
    #print(nilai)
    return kesimpulan

print("------------")
print("DATA TRAIN")
print("------------")
count = 0
benar = 0
while count < 20:
    train = datasetHasil[count]
    if (FuzzyProg(datasetEmosi[count],datasetProvokasi[count]) == train):
        benar = benar + 1
    count = count + 1

print("")
print("Akurasi: "+str((benar/20)*100))
print("------------")
print("")
print("------------")
print("DATA TEST")
print("------------")
print("")

countTest = 0
while countTest < 10:
    datasetHasil[countTest] = FuzzyProg(datatestEmosi[countTest],datatestProvokasi[countTest])
    countTest = countTest + 1

#print(datasetHasil[2])

# print("------------------------------")
# print("Data Training")
# print("------------------------------")
# print("-------------")
# print("Berita   HOAX")
# print("-------------")
# FuzzyProg(97,74,"B01")
# FuzzyProg(36,85,"B02")
# FuzzyProg(63,43,"B03")
# FuzzyProg(82,90,"B04")
# FuzzyProg(71,25,"B05")
# FuzzyProg(79,81,"B06")
# FuzzyProg(55,62,"B07")
# FuzzyProg(57,45,"B08")
# FuzzyProg(40,65,"B09")
# FuzzyProg(57,45,"B10")
# FuzzyProg(77,70,"B11")
# FuzzyProg(68,75,"B12")
# FuzzyProg(60,70,"B13")
# FuzzyProg(82,90,"B14")
# FuzzyProg(40,85,"B15")
# FuzzyProg(80,68,"B16")
# FuzzyProg(60,72,"B17")
# FuzzyProg(50,95,"B18")
# FuzzyProg(100,18,"B19")
# FuzzyProg(11,99,"B20")
# print("------------------------------")
# print("Data Testing")
# print("------------------------------")
# print("-------------")
# print("Berita   HOAX")
# print("-------------")
# FuzzyProg(58,63,"B21")
# FuzzyProg(68,70,"B22")
# FuzzyProg(64,66,"B23")
# FuzzyProg(57,77,"B24")
# FuzzyProg(77,55,"B25")
# FuzzyProg(98,64,"B26")
# FuzzyProg(91,59,"B27")
# FuzzyProg(50,95,"B28")
# FuzzyProg(95,55,"B29")
# FuzzyProg(27,79,"B30")
# print("")
# #print("Akurasi: "+str((19/20)*100))