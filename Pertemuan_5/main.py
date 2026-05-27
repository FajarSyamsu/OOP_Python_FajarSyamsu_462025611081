class DompetDigital:
    def __init__(self, pemilik, nomor_akun, saldo_awal, pin_rahasia):
        self.__pemilik = pemilik         
        self.__saldo = saldo_awal        
        self.__pin = pin_rahasia         

    def get_pemilik(self):
        """Getter untuk mengambil nama pemilik tanpa perlu validasi ketat"""
        return self.__pemilik

    def lihat_saldo(self, input_pin):
        """Metode validasi PIN sebelum menampilkan data saldo privat"""
        if input_pin == self.__pin:
            return f"Verifikasi Berhasil. Saldo {self.__pemilik}: Rp{self.__saldo:,}"
        else:
            return "Verifikasi Gagal: PIN yang Anda masukkan salah!"

    def transfer_dana(self, jumlah, input_pin):
        """Metode validasi PIN sebelum memodifikasi data saldo privat"""
        if input_pin != self.__pin:
            return "Verifikasi Gagal: PIN salah! Transaksi dibatalkan."
        
        if jumlah > self.__saldo:
            return "Transaksi Gagal: Saldo tidak mencukupi."
        
        if jumlah <= 0:
            return "Transaksi Gagal: Jumlah transfer harus lebih dari 0."
        
        self.__saldo -= jumlah
        return f"Transfer Berhasil! Rp{jumlah:,} telah dikirim. Sisa saldo: Rp{self.__saldo:,}"

dompet_kamu = DompetDigital("Andi Wijaya", "9901-2345-6789", 500000, "123456")

print("=== PENGUJIAN DATA PRIVAT (ENCAPSULATION) ===")

print("Akses aman nama pemilik (via Getter):", dompet_kamu.get_pemilik())
print("\n" + "="*40 + "\n")

print("=== PENGUJIAN METODE VALIDASI (PIN SALAH) ===")
print(dompet_kamu.lihat_saldo("111111"))
print(dompet_kamu.transfer_dana(100000, "000000"))
print("\n" + "="*40 + "\n")

print("=== PENGUJIAN METODE VALIDASI (PIN BENAR) ===")
print(dompet_kamu.lihat_saldo("123456"))
print(dompet_kamu.transfer_dana(150000, "123456"))