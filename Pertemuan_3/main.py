class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tampilkan_detail(self):
        return f"Produk: {self.nama} | Harga: Rp{self.harga:,} | Stok: {self.stok} unit"

    def hitung_total_nilai(self):
        total = self.harga * self.stok
        return f"Total nilai aset {self.nama}: Rp{total:,}"


    @staticmethod
    def validasi_kode_produk(kode):
        if kode.startswith("PRD-") and len(kode) == 7:
            return True
        return False


produk_1 = Produk("Laptop Gaming", 15000000, 5)
produk_2 = Produk("Mouse Wireless", 350000, 20)

print("___ PENGUJIAN INSTANCE METHOD ___")

print(produk_1.tampilkan_detail())
print(produk_1.hitung_total_nilai())
print("_" * 40)
print(produk_2.tampilkan_detail())
print(produk_2.hitung_total_nilai())
print("\n" + "_"*40 + "\n")

print("___ PENGUJIAN STATIC METHOD ___")

cek_class = Produk.validasi_kode_produk("PRD-101")
print(f"Validasi via Class (PRD-101): {cek_class}")


cek_objek = produk_1.validasi_kode_produk("ABC-999")
print(f"Validasi via Object (ABC-999): {cek_objek}")