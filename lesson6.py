class Hesab:
    def __init__(self, hesab_nomresi: int, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans
    
    def balansi_artir(self, miqdar):
        self.balans += miqdar
        print(f"Balansınız {miqdar} AZN artırıldı. Yeni balans: {self.balans} AZN")
    
    def pul_cixar(self, miqdar: float):
        if self.balans >= miqdar:
            self.balans -= miqdar
            print(f"{miqdar} AZN pul çıxarıldı. Yeni balans: {self.balans} AZN")
        else:
            print("Balansınızda kifayət qədər vəsait yoxdur.")
    
    def balansi_goster(self):
        print(f"Hesab nömrəsi: {self.hesab_nomresi}, Balans: {self.balans} AZN")
        
    
hesab1 = Hesab(1050106010191617, 10000.5)
hesab1.balansi_goster()

hesab1.balansi_artir(700)

hesab1.pul_cixar(100)


class Kredit(Hesab):
    def __init__(self, hesab_nomresi: int, balans, kredit_meblegi):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meblegi = kredit_meblegi
    
    def kredit_ver(self):
        self.balans += self.kredit_meblegi
        print(f"Kreditiniz {self.kredit_meblegi} AZN hesabınıza əlavə edildi. Yeni balans: {self.balans} AZN")
    
    def kredit_odenisi(self):
        aylıq_odenis = self.kredit_meblegi / 12
        self.balans -= aylıq_odenis
        print(f"Kredit ödənişi {aylıq_odenis} AZN oldu. Yeni balans: {self.balans} AZN")


kredit_hesabi = Kredit(6543210001030479, 2000, 1000)
kredit_hesabi.balansi_goster()

kredit_hesabi.kredit_ver()

kredit_hesabi.kredit_odenisi()




