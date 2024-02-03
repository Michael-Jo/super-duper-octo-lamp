# Kumpul di moodle, by Michael Jonathan Sandy
n = int(input("Masukan bilangan diantara 10-15 atau 20-25 atau 35-40 :"))
# while (10 > n > 15) or (20 > n > 25) or (35 > n > 40):
while (n <= 10) or (15 <= n <= 20) or (25 <= n <= 35) or (40 <= n):
    print("Bilangan salah !")
    n = int(input("Masukan bilangan diantara 10-15 atau 20-25 atau 35-40 :"))
else:
    print("Bilangan benar")