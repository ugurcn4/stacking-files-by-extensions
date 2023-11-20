import os

def duzenle():
    klasor = input("Düzenlemek istediğiniz klasörün adresini girin : ")
    dosyalar = [] # Dosyaları tutacak liste
    uzantilar = [] # Uzantıları tutacak liste

    def list_dir():
        for dosya in os.listdir(klasor): # Gezinilen dosya klasör mü?
            if os.path.isdir(os.path.join(klasor, dosya)):
                continue
            else:
                dosyalar.append(dosya)

    list_dir()
    # uzantıları çekme
    for dosya in dosyalar:
        uzanti = os.path.splitext(dosya)[1] # Gezinilen dosyanın uzantısı çekildi
        if uzanti in uzantilar:
            continue
        else:
            uzantilar.append(uzanti) # Uzantı daha önce listeye eklendi mi?

    for uzanti in uzantilar: # Aynı uzantı isminden klasör daha önceden mevcut mu?
        if os.path.isdir(os.path.join(klasor, uzanti)):
            continue
        else: # Klasörler Oluşturuluyor.
            os.mkdir(os.path.join(klasor, uzanti))

    for dosya in dosyalar:
        uzanti = os.path.splitext(dosya)[1]
        os.rename(os.path.join(klasor, dosya), os.path.join(klasor,uzanti,dosya))

if __name__ == "__main__":
    duzenle()