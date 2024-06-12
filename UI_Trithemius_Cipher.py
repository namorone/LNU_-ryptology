import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, scrolledtext
from trithemius_cipher import *
from Attack import *
import time
from PIL import Image
class TrithemiusCipherApp:
    def __init__(self, master ):
        self.language = "ukr"
        self.type_action = "encrypt"
        self.shift_variant =""
        self.text_value = ""
        self.file_content = ""
        self.master = master
        self.master.title("TrithemiusCipher")
        self.master.geometry("800x500")

        self.master.grid_columnconfigure(0, weight=8)  # Перша колонка
        self.master.grid_columnconfigure(1, weight=2)  # Друга колонка
        self.master.grid_rowconfigure(0, weight=15)  # Перший рядок
        self.master.grid_rowconfigure(1, weight=33)  # Другий рядок
        self.master.grid_rowconfigure(2, weight=33)  # Третій рядок
        self.master.grid_rowconfigure(3, weight=19)
        self.create_menu()
        self.create_shift_controls()
        self.create_action_batton()
        self.create_input_text()
        self.create_output_text()
        self.create_language_and_action_selectors()


    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Відкрити файл", command=self.open_file)
        file_menu.add_command(label="Зберегти файл", command=self.save_file)
        file_menu.add_command(label="Зберегти як", command=self.save_as)
        file_menu.add_command(label="Вихід", command=self.master.quit)
        self.menu.add_cascade(label="Файл", menu=file_menu)

        cipher_menu = tk.Menu(self.menu, tearoff=0)
        cipher_menu.add_command(label="Зашифрувати файл", command=self.encrypt_file)
        cipher_menu.add_command(label="Розшифрувати файл", command=self.decrypt_file)
        cipher_menu.add_command(label="Зашифрувати зображення", command=self.encrypt_image)
        cipher_menu.add_command(label="Розшифрувати зображення", command=self.decrypt_image)
        self.menu.add_cascade(label="Шифрування", menu=cipher_menu)

        attack_menu = tk.Menu(self.menu, tearoff=0)
        attack_menu.add_command(label="Атака ", command=self.perform_brute_force)
        self.menu.add_cascade(label="Атака", menu=attack_menu)

        help_menu = tk.Menu(self.menu, tearoff=0)
        help_menu.add_command(label="Про розробника", command=self.about)
        self.menu.add_cascade(label="Допомога", menu=help_menu)

        frequency_menu = tk.Menu(self.menu, tearoff=0)
        frequency_menu.add_command(label="Частотна таблиця", command=self.frequency_table)
        self.menu.add_cascade(label="Частотна таблиця", menu=frequency_menu)


    def create_shift_controls(self):
        self.shift_frame = tk.Frame(self.master)
        self.shift_frame.grid(row=0, column=1,pady=10, sticky="nsew")
        self.shift_framel = tk.Frame(self.master)
        self.shift_framel.grid(row=0, column=0, pady=10, sticky="nsew")

        self.shift_label = tk.Label(self.shift_framel, text="Введіть 2 або 3 вимірний вектор черз кому або гасло :", font=('Helvetica', 12))
        self.shift_label.pack()

        self.entry_var = tk.StringVar()
        self.shift_spinbox = tk.Entry(self.shift_frame, textvariable=self.entry_var)

        self.shift_spinbox.grid(row=0, column=1, sticky="nsew")

    def get_shift(self):
        print(self.shift_spinbox.get())
        print(type(self.shift_spinbox.get()))
        print(len(self.shift_spinbox.get()))
        # Розбити рядок на числа
        numbers = self.shift_spinbox.get().split(',')
        print(len(numbers))
        # Перевірити кількість чисел у вхідному рядку
        if len(numbers) == 2:
            self.shift_variant = "2D"
            return [int(numbers[0]), int(numbers[1])]
        elif len(numbers) == 3:
            self.shift_variant = "3D"
            return [int(numbers[0]), int(numbers[1]), int(numbers[2])]


        else:
            self.shift_variant = "str"
            print("гасло :", self.shift_spinbox.get())
            return self.shift_spinbox.get()



    def create_language_and_action_selectors(self):

        selector_frame = tk.Frame(self.master)
        selector_frame.grid(row=1, column=1, columnspan=2, padx=3, pady=5, sticky="w")

        # language_frame = tk.Frame(selector_frame)
        # language_frame.pack(padx=2, pady=(0, 20), anchor="w")
        #
        # self.selected_language = tk.StringVar()
        # self.selected_language.set("ukr")
        #
        # tk.Radiobutton(language_frame, text="Українська", variable=self.selected_language, value="ukr",
        #                command=lambda: self.update_language("ukr")).pack(anchor="w")
        # tk.Radiobutton(language_frame, text="English", variable=self.selected_language, value="eng",
        #                command=lambda: self.update_language("eng")).pack(anchor="w")


        action_frame = tk.Frame(selector_frame)
        action_frame.pack(padx=2, pady=(0, 10), anchor="w")

        self.selected_type_action = tk.StringVar()
        self.selected_type_action.set("encrypt")

        tk.Radiobutton(action_frame, text="Зашифрувати", variable=self.selected_type_action, value="encrypt",
                       command=lambda: self.update_type_action("encrypt")).pack(anchor="w")
        tk.Radiobutton(action_frame, text="Розшифрувати", variable=self.selected_type_action, value="decrypt",
                       command=lambda: self.update_type_action("decrypt")).pack(anchor="w")

    # def update_language(self, language):
    #     self.language = language

    def update_type_action(self, type_action):
        self.type_action = type_action

    def create_input_text(self):
        self.input_text =tk.Text(self.master, height=10,  wrap="word")
        self.input_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.input_text.bind("<KeyRelease>", self.save_text_value)
        # self.input_text.bind("<Key>", self.check_paste)

    def save_text_value(self, event=None):
        self.text_value = self.input_text.get("1.0", "end-1c")

    # def check_paste(self, event=None):
    #     if event.keysym.lower() == 'v' and event.state == 4:
    #         clipboard_content = self.master.clipboard_get()
    #         self.input_text.insert(tk.INSERT, clipboard_content)

    def create_output_text(self):
        self.output_text = tk.Text(self.master, height=10, width=50, wrap="word")
        self.output_text.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.output_text.config(state="disabled")

    def insert_text(self, text):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", text)
        self.output_text.config(state="disabled")



    def create_action_batton(self):
        button_frame = tk.Frame(self.master)
        button_frame.grid(row=2, column=1, padx=3, pady=5, sticky="n")

        # Перша кнопка
        button1 = tk.Button(button_frame, text="Вирішити", command=lambda: self.button_clicked())
        button1.pack(pady=(0, 5), anchor="w")

        # Друга кнопка
        button2 = tk.Button(button_frame, text="Вирішити для файлу", command=lambda: self.button_file_clicked())
        button2.pack(pady=(0, 5), anchor="w")



    def button_clicked(self):
        print("Значення text_value:", self.text_value)
        print("Отримане значення через get_shift():", self.get_shift())
        print("Значення entry_var:", self.entry_var.get())

        if self.text_value == "":
            messagebox.showwarning("Увага", "Введіть текст для шифрування.")
        else :
            if self.type_action == "encrypt":

                self.cipher = TrithemiusCipher(self.get_shift())

                self.insert_text(self.cipher.encrypt(self.text_value))
            else:
                self.cipher = TrithemiusCipher(self.get_shift())
                self.insert_text(self.cipher.decrypt(self.text_value))

    def button_file_clicked(self):
        if self.file_content == "":
            messagebox.showwarning("Увага", "Виберіть файл")
        else:
            if self.type_action == "encrypt":
                self.cipher = TrithemiusCipher(self.get_shift())
                self.encrypt_file()
                self.insert_text(self.file_content)
            else:
                self.cipher = TrithemiusCipher(self.get_shift())
                self.decrypt_file()
                self.insert_text(self.file_content)

    def open_file(self):
        filename = filedialog.askopenfilename(title="Відкрити файл", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                self.file_content = file.read()
                messagebox.showinfo("Файл відкрито", "Файл успішно відкрито.")

    def save_file(self):
        if not hasattr(self, 'file_content'):
            messagebox.showwarning("Увага", "Немає відкритого файлу для збереження.")
            return
        filename = filedialog.asksaveasfilename(title="Зберегти файл", defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.file_content)
                messagebox.showinfo("Файл збережено", "Файл успішно збережено.")

    def encrypt_file(self):
        if not self.cipher:
            messagebox.showwarning("Увага", "Спочатку створіть шифр.")
            return
        if not hasattr(self, 'file_content'):
            messagebox.showwarning("Увага", "Немає відкритого файлу для шифрування.")
            return
        encrypted_text = self.cipher.encrypt(self.file_content)
        self.file_content = encrypted_text
        messagebox.showinfo("Шифрування", "Файл успішно зашифровано.")

    def decrypt_file(self):
        if not self.cipher:
            messagebox.showwarning("Увага", "Спочатку створіть шифр.")
            return
        if not hasattr(self, 'file_content'):
            messagebox.showwarning("Увага", "Немає відкритого файлу для розшифрування.")
            return
        decrypted_text = self.cipher.decrypt(self.file_content)
        self.file_content = decrypted_text
        messagebox.showinfo("Розшифрування", "Файл успішно розшифровано.")

    def brute_force_decrypt(self,original_text, encrypted_text,len):
        start_time = time.time()

        self.attack = FrequencyAttack(original_text)
        self.k = self.attack.active_attack(original_text, encrypted_text)
        if self.shift_variant == "2D":
            return self.k[:2], time.time() - start_time
        elif self.shift_variant == "3D":
            return self.k[:3], time.time() - start_time
        else:
            return ''.join([chr(num) for num in self.k[:len]]), time.time() - start_time




        return None, time.time() - start_time

    def perform_brute_force(self):
        if self.input_text.get("1.0", "end-1c") == "" or self.output_text.get("1.0", "end-1c") == "":
            messagebox.showwarning("Увага", "Зашифруйте спочатку повідомлення.")
            return
        shift, execution_time = self.brute_force_decrypt(self.text_value, self.output_text.get("1.0", "end-1c"),len(self.get_shift()))
        if shift is not None:
            result_message = f"Зсув: {shift}\nЧас роботи алгоритму: {execution_time:.5f} сек"
        else:
            result_message = "Не вдалося знайти правильний зсув."


        messagebox.showinfo("Результат атаки", result_message)

    def build_frequency_table(self):
        ukrainian_frequency = {}
        total_characters = len(self.text_value)
        for char in self.text_value:
            frequency = self.text_value.count(char) / total_characters
            ukrainian_frequency[char] = round(frequency,4)
        return ukrainian_frequency

    def frequency_table(self):
        table_window = tk.Toplevel(self.master)
        table_window.title("Частотна таблиця")


        text_widget = tk.Text(table_window, wrap="word", font=('Helvetica', 12))
        text_widget.grid(row=0, column=0, sticky="nsew")


        scrollbar = tk.Scrollbar(table_window, orient="vertical", command=text_widget.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        text_widget.config(yscrollcommand=scrollbar.set)
        frequency_table = self.build_frequency_table()

        for char, frequency in sorted(frequency_table.items()):
            text_widget.insert(tk.END, f"{char}: {frequency * 100}%\n")


        text_widget.config(state="disabled")

    def encrypt_image(self):

        file_path = filedialog.askopenfilename(title="Select Image File", filetypes=(
        ("Image files", "*.jpg;*.jpeg;*.png;*.bmp"), ("All files", "*.*")))
        if not file_path:
            return

        image = Image.open(file_path)
        self.cipher = CaesarCipher(int(self.shift_spinbox.get()), self.language)
        encrypted_image = self.cipher.caesar_cipher_image(image, int(self.shift_spinbox.get()))  # Приклад шифрування за допомогою шифру Цезаря

        encrypted_image.save("encrypted_image.png")
        messagebox.showinfo("Encryption", "Image encrypted successfully.")

    def decrypt_image(self):

        file_path = filedialog.askopenfilename(title="Select Encrypted Image File",
                                               filetypes=(("Image files", "*.png"), ("All files", "*.*")))
        if not file_path:
            return


        encrypted_image = Image.open(file_path)
        self.cipher = CaesarCipher(int(self.shift_spinbox.get()), self.language)
        decrypted_image = self.cipher.caesar_cipher_image(encrypted_image,
                                                   -int(self.shift_spinbox.get()))
        decrypted_image.save("decrypted_image.png")
        messagebox.showinfo("Decryption", "Image decrypted successfully.")

    def save_as(self):
        i_text = self.input_text.get("1.0", "end-1c")
        o_text = self.output_text.get("1.0", "end-1c")
        text_to_print = f"Вхідний текст:\n{i_text}\nЧисло зсуву: {self.shift_spinbox.get()}\nДія:{self.type_action}\nВихідний текст:\n{o_text}"
        with open("temp_print_file.txt", "w") as file:
            file.write(text_to_print)
        messagebox.showinfo("", "Збережено в temp_print_file.txt")
    def about(self):
        messagebox.showinfo("Про розробника", """
        Ця програма була розроблена користувачем для демонстрації системи симетричного шифрування.\n
        Розробив її студент групи Пмі31 Боровець Роман\n 
        Для зв'язку з розробником пишіть на пошту: help.ceaser.rb@gmail.com 
        """)
