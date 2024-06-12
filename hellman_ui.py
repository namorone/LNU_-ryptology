import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, scrolledtext
from Hellman import *

class HellmanCipherApp:
    def __init__(self, master ):

        self.type_action = "encrypt"
        self.key = ""
        self.text_value = ""
        self.file_content = ""
        self.public_key = tk.StringVar(value="")
        self.private_key = tk.StringVar(value="")
        self.master = master
        self.master.title("Hellman Cryptosystem")
        self.master.geometry("800x500")

        self.master.grid_columnconfigure(0, weight=8)  # Перша колонка
        self.master.grid_columnconfigure(1, weight=2)  # Друга колонка
        self.master.grid_rowconfigure(0, weight=15)  # Перший рядок
        self.master.grid_rowconfigure(1, weight=33)  # Другий рядок
        self.master.grid_rowconfigure(2, weight=33)  # Третій рядок
        self.master.grid_rowconfigure(3, weight=19)
        self.create_menu()
        self.create_action_batton()
        #self.create_input_text()
        self.create_output_text()




    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Зберегти як", command=self.save_as)
        file_menu.add_command(label="Вихід", command=self.master.quit)
        self.menu.add_cascade(label="Файл", menu=file_menu)

        help_menu = tk.Menu(self.menu, tearoff=0)
        help_menu.add_command(label="Про розробника", command=self.about)
        self.menu.add_cascade(label="Допомога", menu=help_menu)

        frequency_menu = tk.Menu(self.menu, tearoff=0)
        frequency_menu.add_command(label="Частотна таблиця", command=self.frequency_table)
        self.menu.add_cascade(label="Частотна таблиця", menu=frequency_menu)


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
        self.output_text.grid(row=1, column=0,rowspan=2, padx=10, pady=10, sticky="nsew")
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



    def button_clicked(self):

        self.insert_text(main())

    def button_file_clicked(self):
        if self.file_content == "":
            messagebox.showwarning("Увага", "Виберіть файл")
        else:

            if self.type_action == "encrypt":
                self.encrypt_file()
                self.insert_text(self.file_content)
            else:
                self.decrypt_file()
                self.insert_text(self.file_content)





    def save_file(self):
        if not hasattr(self, 'file_content'):
            messagebox.showwarning("Увага", "Немає відкритого файлу для збереження.")
            return
        filename = filedialog.asksaveasfilename(title="Зберегти файл", defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.file_content)
                messagebox.showinfo("Файл збережено", "Файл успішно збережено.")


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

    def save_as(self):
        i_text = self.input_text.get("1.0", "end-1c")
        o_text = self.output_text.get("1.0", "end-1c")
        text_to_print = f"Вхідний текст:\n{i_text}\nКлюч: {self.key}\nДія:{self.type_action}\nТип шифру:{self.language}Вихідний текст:\n{o_text}"
        with open("temp_print_file.txt", "w") as file:
            file.write(text_to_print)
        messagebox.showinfo("", "Збережено в temp_print_file.txt")
    def about(self):
        messagebox.showinfo("Про розробника", """
        Ця програма була розроблена користувачем для демонстрації системи симетричного шифрування.\n
        Розробив її студент групи Пмі31 Боровець Роман\n 
        Для зв'язку з розробником пишіть на пошту: help.ceaser.rb@gmail.com 
        """)
