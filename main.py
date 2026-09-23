# Program Cek Stat Roblox Sederhana
print("=== ROBLOX PLAYER STATS ===")

username = input("Masukkan Username Roblox: ")
level = int(input("Masukkan Level Character: "))
robux = int(input("Masukkan Total Robux: "))

print("\n--- DATA PLAYER ---")
print("Username :", username)
print("Level    :", level)
print("Robux    :", robux)

if level >= 50:
    print("Status   : Pro Player")
else:
    print("Status   : Beginner / Novice")