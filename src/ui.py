# src/ui.py
import tkinter as tk
from tkinter import filedialog

class App(tk.Tk):
    def __init__(self, on_file_selected, on_start, on_stop):
        super().__init__()
        self.title("VIGIL Logwatch")
        self.geometry("760x480")

        top = tk.Frame(self); top.pack(fill="x", pady=8)
        tk.Button(top, text="Open CSV",
                  command=lambda: self._pick_file(on_file_selected)).pack(side="left", padx=6)

        tk.Label(top, text="Z-score threshold").pack(side="left", padx=6)
        self.threshold = tk.DoubleVar(value=3.0)
        tk.Entry(top, textvariable=self.threshold, width=8).pack(side="left")

        tk.Button(top, text="Start",
                  command=lambda: on_start(self.threshold.get())).pack(side="left", padx=6)
        tk.Button(top, text="Stop", command=on_stop).pack(side="left", padx=6)

        self.log = tk.Text(self, height=22)
        self.log.pack(fill="both", expand=True, padx=8, pady=8)

    def _pick_file(self, cb):
        path = filedialog.askopenfilename(
            title="Select CSV (timestamp,value)",
            filetypes=[("CSV", "*.csv"), ("All files", "*.*")]
        )
        if path:
            cb(path)

    def show_alert(self, text: str):
        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.update_idletasks()
