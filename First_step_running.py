import os
import shutil

# A fájlok listája, amelyeket át szeretnénk helyezni
files = ['script/gitscript.py', 'script/send_gpt1.py', 'script/send_gpt2.py', 'script/config.ini']

# Az új mappa neve
new_folder = '.git/script'

# Ellenőrizzük, hogy létezik-e már az új mappa, ha nem, akkor hozzuk létre
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Menjünk végig a fájlokon, és helyezzük át őket az új mappába
for file in files:
    # Csak akkor helyezzük át a fájlt, ha létezik
    if os.path.exists(file):
        shutil.move(file, new_folder)
    else:
        print(f"A {file} fájl nem létezik.")

# A fájl, amit át szeretnél helyezni
file = 'script/prepare-commit-msg'

# A mappa neve
folder = '.git/hooks'

# Áthelyezzük a fájlt a mappába
if os.path.exists(file):
    shutil.move(file, folder)
else:
    print(f"A {file} fájl nem létezik.")

# A mappa, amit törölni szeretnél
folder = 'script'

# A fájl, amit törölni szeretnél
file = 'First_step_running.py'

# Töröljük a mappát és annak tartalmát
if os.path.exists(folder):
    shutil.rmtree(folder)
else:
    print(f"A {folder} mappa nem létezik.")

# Töröljük a fájlt
if os.path.exists(file):
    os.remove(file)
else:
    print(f"A {file} fájl nem létezik.")
