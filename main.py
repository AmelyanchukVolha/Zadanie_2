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


button_save = tk.Button(root, text="Zapisz !", command=lambda x:x, )
button_save.grid(row=10, column=0, columnspan=2, pady=10)
# Uruchomienie pętli głównej
root.mainloop()