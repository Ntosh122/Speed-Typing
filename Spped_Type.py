import time
import random
import tkinter as tk
import threading


class SpeedTypeGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Speed Typing Application Demo")
        self.root.geometry("800x600")

        self.texts = open("text.txt", "r").read().split("\n")  # read file

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Poppins", 14))
        # the gui label is going to load with the random text from the file
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        #         entry of text
        self.input_entry = tk.Entry(self.frame, width=40, font=("Open-Sans", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        #         speed output
        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPS",
                                    font=("Poppins", 20))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font=("Poppins", 20))
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                threading.Thread(target=self.time_thread).start()
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPS")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)


SpeedTypeGui()
