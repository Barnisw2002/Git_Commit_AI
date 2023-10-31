import tkinter as tk
from tkinter import messagebox,  ttk
import configparser


def save_config():
    config = configparser.ConfigParser()
    config['GPT'] = {'version': gpt_version_entry.get()}
    config['API'] = {'key': api_key_entry.get()}
    config['TMT'] = {'temperature': temperature_entry.get()}
    config['VAR'] = {'variant': variant_combobox.get()}

    with open('config.ini',  'w') as configfile:
        config.write(configfile)
    
    messagebox.showinfo("Info",  "Config saved successfully!")

#textbox hossz
w = 45
top = 3
button = 8

root = tk.Tk()
root.title("Config Editor")
root.geometry("350x300")  # Fix window size

gpt_version_label = tk.Label(root,  text="GPT Version:")
gpt_version_label.pack(pady=(10, 0))

gpt_version_entry = ttk.Combobox(root,  values=["gpt-3.5-turbo", "gpt-4"],  width=w)
gpt_version_entry.pack(ipady=2,  pady=(top, button))

api_key_label = tk.Label(root,  text="API Key:")
api_key_label.pack()

api_key_entry = tk.Entry(root,  width=w+3,  show="✱")
api_key_entry.pack(ipady=2,  pady=(top, button))

temperature_label = tk.Label(root,  text="Temperature:")
temperature_label.pack()

temperature_entry = ttk.Combobox(root,  values=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],  width=w)
temperature_entry.pack(ipady=2, pady=(top, button))

variant_label = tk.Label(root,  text="Variant:")
variant_label.pack()

variant_combobox = ttk.Combobox(root,  values=["0",  "1"],  width=w)
variant_combobox.pack(ipady=2,  pady=(top, button+10))

save_button = tk.Button(root,  text="Save Config",  command=save_config)
save_button.pack()

root.mainloop()