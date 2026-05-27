class PerangkatElektronik:
    def __init__(self, merek):
        self.merek = merek
        print(f"[{self.merek}] Inisialisasi Perangkat Elektronik")

    def booting(self):
        return f"{self.merek} sedang menyala..."

class Kamera(PerangkatElektronik):
    def __init__(self, merek, resolusi):
        super().__init__(merek)
        self.resolusi = resolusi
        print(f"[{self.merek}] Inisialisasi Fitur Kamera ({self.resolusi})")

    def ambil_foto(self):
        return f"Mengambil foto dengan resolusi {self.resolusi}."

class PemutarMusik(PerangkatElektronik):
    def __init__(self, merek, format_audio):
        super().__init__(merek)
        self.format_audio = format_audio
        print(f"[{self.merek}] Inisialisasi Fitur Pemutar Musik ({self.format_audio})")

    def putar_lagu(self):
        return f"Memutar musik berformat {self.format_audio}."

class Smartphone(Kamera, PemutarMusik):
    def __init__(self, merek, resolusi, format_audio, tipe_os):
        super().__init__(merek, resolusi=resolusi)
        
        self.format_audio = format_audio
        self.tipe_os = tipe_os
        print(f"[{self.merek}] Inisialisasi Smartphone dengan OS {self.tipe_os}")

    def info_gadget(self):
        return f"Gadget: {self.merek} | OS: {self.tipe_os} | Kamera: {self.resolusi} | Audio: {self.format_audio}"

print("=== Proses Inisialisasi Objek (MRO Python) ===")
hp_saya = Smartphone("Samsung S26", "108 MP", "FLAC", "Android 16")
print("\n" + "="*45 + "\n")

print("=== Pengujian Metode Hasil Pewarisan ===")
print(hp_saya.booting())       
print(hp_saya.ambil_foto())     
print(hp_saya.putar_lagu())     
print(hp_saya.info_gadget())    

print("\n" + "="*45 + "\n")
print("=== Urutan Eksekusi MRO (Method Resolution Order) ===")
for urutan, cls in enumerate(Smartphone.__mro__, start=1):
    print(f"{urutan}. {cls.__name__}")