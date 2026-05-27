class AlatPembayaran:
    def proses_bayar(self, jumlah):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini!")

class KartuKredit(AlatPembayaran):
    def __init__(self, nomor_kartu):
        self.nomor_kartu = nomor_kartu

    def proses_bayar(self, jumlah):
        return f"Mengosongkan limit Kartu Kredit [XXXX-{self.nomor_kartu[-4:]}] sebesar Rp{jumlah:,}. Transaksi Berhasil!"

class EWallet(AlatPembayaran):
    def __init__(self, nomor_hp):
        self.nomor_hp = nomor_hp

    def proses_bayar(self, jumlah):
        return f"Memotong saldo E-Wallet ({self.nomor_hp}) sebesar Rp{jumlah:,}. Kode QR Berhasil Dipindai!"

def jalankan_transaksi(objek_pembayaran, jumlah):
    print("--- Memulai Proses Verifikasi Gateway ---")
    Sinyal_proses = objek_pembayaran.proses_bayar(jumlah)
    print(Sinyal_proses)
    print("--- Transaksi Selesai Dicatat oleh Sistem ---\n")

pembayaran_via_kartu = KartuKredit("1234567890123456")
pembayaran_via_ewallet = EWallet("0812-3456-7890")

print("=== PENGUJIAN POLYMORPHISM & DUCK TYPING ===\n")

jalankan_transaksi(pembayaran_via_kartu, 500000)

jalankan_transaksi(pembayaran_via_ewallet, 75000)

class QrisDonasi:
    def proses_bayar(self, jumlah):
        return f"Donasi via QRIS sebesar Rp{jumlah:,} diterima. Terima kasih orang baik!"

objek_donasi = QrisDonasi()
print("=== BUKTI DUCK TYPING (Tanpa Inheritance) ===")
jalankan_transaksi(objek_donasi, 10000)