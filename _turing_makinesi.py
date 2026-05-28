def turing_makinesi_simulasyonu(plaka):
    bant = list(plaka)
    mevcut_durum = "q0"
    print(f"--- Başlangıç: {plaka} ---\n")
    for i in range(len(bant)):
        karakter = bant[i]
        okunan_tip = "N" if karakter.isdigit() else ("L" if karakter.isalpha() and karakter.isupper() else "Hata")
        if karakter.islower():
            okunan_tip = "Hata"
        print(f"Adım {i+1}: Durum {mevcut_durum}, Okunan: {karakter}, Bant: {''.join(bant)}")
        if mevcut_durum == "q0" and okunan_tip == "N": mevcut_durum = "q1"
        elif mevcut_durum == "q1" and okunan_tip == "N": mevcut_durum = "q2"
        elif mevcut_durum == "q2" and okunan_tip == "L": mevcut_durum = "q3"
        elif mevcut_durum == "q3" and okunan_tip == "L": mevcut_durum = "q4"
        elif mevcut_durum == "q4" and okunan_tip == "N": mevcut_durum = "q5"
        elif mevcut_durum == "q5" and okunan_tip == "N": mevcut_durum = "q6"
        elif mevcut_durum == "q6" and okunan_tip == "N": mevcut_durum = "q7"
        else:
            print(">>> HATA: Geçersiz karakter veya format! RED.")
            return "RED"
    if mevcut_durum == "q7" and len(bant) == 7:
        print(">>> Başarıyla tamamlandı. KABUL.")
        return "KABUL"
    else:
        print(">>> HATA: Eksik karakter veya format hatası! RED.")
        return "RED"
test_girdileri = ["55AB123", "34TR456", "5AB123", "555AB12", "55ab123"]
for girdi in test_girdileri:
    print(f"\nTest Ediliyor: {girdi}")
    turing_makinesi_simulasyonu(girdi)
    print("-" * 30)