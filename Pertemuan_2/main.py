class Laptop:
   
    def __init__(self, merek, prosesor, ram):
        self.merek = merek          
        self.prosesor = prosesor    
        self.ram = ram              
    
    def tampilkan_info(self):
        return f"Laptop {self.merek} | Prosesor: {self.prosesor} | RAM: {self.ram} GB"


laptop_a = Laptop("Asus ROG", "Intel i7", 16)
laptop_b = Laptop("MacBook Air", "Apple M2", 8)


print(laptop_a.tampilkan_info())
print(laptop_b.tampilkan_info())