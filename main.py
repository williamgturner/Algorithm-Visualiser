import customtkinter
import tkinter as tk
import seaborn as sns
import matplotlib.pyplot as plt
import gui
import time
import threading

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("AlgoVis")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=8)
        self.grid_rowconfigure(0, weight=1)
        plt.axis('off')

        self.gui = gui.gui(master=self)
        # init seaborn plot
        self.plot_data = sns.load_dataset("penguins")
        self.plot = sns.barplot(data=self.plot_data, x="species", y="bill_length_mm")
        self.gui.canvas.embed_plot(self.plot)
        self.focus_force() # bring window into focus on app open


    def load_text_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            return file_content
        except Exception as e:
            print(f"Error: {e}")
    

    def start_vis(self):
        print("Sleep Over")
    
    def button_click(self):
        print("Visualisation Started")
        self.after(5000, self.start_vis)
    
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()