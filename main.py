from FileEncryptor import *

from ui import *
from trithemius_cipher import *
from Attack import *
from UI_Trithemius_Cipher import *
from backpack_ui import *
from gamma_Ui import *
from rsa_ui import *
from hellman_ui import *

from tkinter import ttk

# class MainApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Main App")
#         self.master.geometry("800x600")
#
#         self.tab_control = ttk.Notebook(master)
#
#         self.caesar_tab = CryptoApp(self.tab_control)
#         self.tab_control.add(self.caesar_tab, text="Caesar Cipher")
#
#         self.trithemius_tab = TrithemiusCipherApp(self.tab_control)
#         self.tab_control.add(self.trithemius_tab, text="Trithemius Cipher")
#
#         self.gamma_tab = GammaCipherApp(self.tab_control)
#         self.tab_control.add(self.gamma_tab, text="Gamma Cipher")
#
#         self.knapsack_tab = BackpackCipherApp(self.tab_control)
#         self.tab_control.add(self.knapsack_tab, text="Knapsack")
#
#
#         self.tab_control.pack(expand=1, fill="both")

def main():
    #root = tk.Tk()
    # root2 = tk.Tk()
    # root3 = tk.Tk()
    #root4 = tk.Tk()
    root5 = tk.Tk()
    root6 = tk.Tk()
    # app = CryptoApp(root)
    # app2 = TrithemiusCipherApp(root2)
    #app3 = GammaCipherApp(root3)
    #app4 = BackpackCipherApp(root4)
    app5 = RsaCipherApp(root5)
    app6 = HellmanCipherApp(root6)
    # root.mainloop()
    # root2.mainloop()
    #root3.mainloop()
    #root4.mainloop()
    root5.mainloop()
    root6.mainloop()



if __name__ == "__main__":
     main()
    # root = tk.Tk()
    # root.title("Knapsack Cryptosystem")
    # root.geometry("800x600")
    #
    # tab_control = ttk.Notebook(root)
    #
    # knapsack_tab = KnapSackTab(tab_control)
    # tab_control.add(knapsack_tab, text="Knapsack")
    #
    # tab_control.pack(expand=1, fill="both")
    #
    # root.mainloop()

