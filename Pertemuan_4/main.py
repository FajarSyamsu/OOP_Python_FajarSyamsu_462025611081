class SkorPemain:
    def __init__(self, username, skor):
        self.username = username
        self.skor = skor

    def __str__(self):
        return f"Pemain: {self.username} | Skor: {self.skor} Pts"

    def __eq__(self, other):
        if isinstance(other, SkorPemain):
            return self.skor == other.skor
        return False

    def __lt__(self, other):
        if isinstance(other, SkorPemain):
            return self.skor < other.skor
        return NotImplemented

    def __gt__(self, other):
        # __gt__ untuk operator lebih dari (>)
        if isinstance(other, SkorPemain):
            return self.skor > other.skor
        return NotImplemented

pemain_1 = SkorPemain("Alpha_Gamer", 2500)
pemain_2 = SkorPemain("Beta_Slayer", 3500)
pemain_3 = SkorPemain("Cyber_Ghost", 2500)

print("=== PENGUJIAN __str__ ===")
print(pemain_1)
print(pemain_2)
print(pemain_3)
print("\n" + "="*40 + "\n")

print("=== PENGUJIAN METODE PERBANDINGAN ===")
print(f"Apakah {pemain_1.username} > {pemain_2.username}? -> {pemain_1 > pemain_2}")
print(f"Apakah {pemain_2.username} > {pemain_1.username}? -> {pemain_2 > pemain_1}")
print("-" * 40)

print(f"Apakah {pemain_1.username} < {pemain_2.username}? -> {pemain_1 < pemain_2}")
print("-" * 40)

print(f"Apakah {pemain_1.username} == {pemain_3.username}? -> {pemain_1 == pemain_3}")
print(f"Apakah {pemain_2.username} == {pemain_3.username}? -> {pemain_2 == pemain_3}")
