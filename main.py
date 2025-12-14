#Stwórz formularz do opisu książki w bazie danych (bez zapisu)
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Rejestr wolontariusza")
# Etykiety i pola tekstowe
label_name = tk.Label(root, text="Imię:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root, width=40)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_surname = tk.Label(root, text="Nazwisko:")
label_surname.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_surname = tk.Entry(root, width=40)
entry_surname.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Adres e-mail:")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_phonenumber = tk.Label(root, text="Numer telefonu:")
label_phonenumber.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_phonenumber = tk.Entry(root, width=40)
entry_phonenumber.grid(row=3, column=1, padx=10, pady=5)

label_city = tk.Label(root, text="Miasto:")
label_city.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_city = tk.Entry(root, width=40)
entry_city.grid(row=4, column=1, padx=10, pady=5)

label_country = tk.Label(root, text="Kraj:")
label_country.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_country = tk.Entry(root, width=40)
entry_country.grid(row=5, column=1, padx=10, pady=5)

label_dateofbirth = tk.Label(root, text="Data urodzenia:")
label_dateofbirth.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_dateofbirth = tk.Entry(root, width=40)
entry_dateofbirth.grid(row=6, column=1, padx=10, pady=5)


label_pesel = tk.Label(root, text="Pesel:")
label_pesel.grid(row=7, column=0, padx=10, pady=5, sticky="w")
entry_pesel = tk.Entry(root, width=40)
entry_pesel.grid(row=7, column=1, padx=10, pady=5)

label_education = tk.Label(root, text="Wykształcenie:")
label_education.grid(row=8, column=0, padx=10, pady=5, sticky="w")
entry_education = tk.Entry(root, width=40)
entry_education.grid(row=8, column=1, padx=10, pady=5)

label_voluneer_experience = tk.Label(root, text="Doświadczenie wolontariackie:")
label_voluneer_experience.grid(row=9, column=0, padx=10, pady=5, sticky="w")
entry_voluneer_experience = tk.Entry(root, width=40)
entry_voluneer_experience.grid(row=9, column=1, padx=10, pady=5)

label_foreign_language = tk.Label(root, text="Języki obce:")
label_foreign_language.grid(row=10, column=0, padx=10, pady=5, sticky="w")
entry_foreign_language = tk.Entry(root, width=40)
entry_foreign_language.grid(row=10, column=1, padx=10, pady=5)

# Przycisk zapisu
button_save = tk.Button(root, text="!!! Zapisz !!!", command=lambda x:x, )
button_save.grid(row=11, column=0, columnspan=2, pady=10)
# Uruchomienie pętli głównej
root.mainloop()