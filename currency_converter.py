import tkinter as tk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Mein Währungsrechner")

        # Label
        self.label = tk.Label(root, text="Gib einen Geldbetrag ein: (in Euro)")
        self.label.grid(row=0,column=1)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.grid(row=1,column=1)

        # Button
        self.button1 = tk.Button(root, text="EUR", command=self.anzeigen)
        self.button2 = tk.Button(root, text="USD", command=self.convert_in_usd)
        self.button3 = tk.Button(root, text="GBP", command=self.convert_in_gbp)
        self.button1.grid(row=2,column=0)
        self.button2.grid(row=2,column=1)
        self.button3.grid(row=2,column=2)
        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.grid(row=3,column=1)

    def anzeigen(self):
        zahl = int(self.entry.get())
        if self.button1:
            self.output_label.config(text=f"Dein Betrag in Euro: {zahl}!")
    def convert_in_usd(self):
        zahl = int(self.entry.get())
        Usd= zahl * 1.17
        self.output_label.config(text=f"Dein Betrag in USD: {Usd}!")
    def convert_in_gbp(self):
        zahl = int(self.entry.get())
        Gbp = zahl * 0.86
        self.output_label.config(text=f"Dein Betrag in GBP: {Gbp}!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()

