""""
1.Hesabınıza anında 1.000.000 lira yatırılacak.
2.30 gün boyunca her gün ikiye katlanarak artan 0.01 TL
alacaksınız.
"""

seçim = int(input("Lütfen bir sayı giriniz:"))

if seçim == 1:
    print("Hesabınıza 1.000.000 tl yatırıldı")
if seçim == 2:
    print("30 gün sonra hesabınızda",int(0.01*(2**30)),'Lira olacak'  )
