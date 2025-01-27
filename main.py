import customtkinter
import seaborn as sns
import matplotlib.pyplot as plt
import gui
import searches
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
        self.focus_force() # bring window into focus on app open


    def load_text_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            return file_content
        except Exception as e:
            print(f"Error: {e}")

    def start_vis(self, search):
        if (not search.complete):
            search.step()
            self.gui.canvas.update_plot(search)
            
            self.after(500, self.start_vis, search)
        else:
            print(search.index)
    
    def button_click(self):
        print("Visualisation Started")
        search = searches.linear_search()
        self.start_vis(search)
    
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()