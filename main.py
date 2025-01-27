import customtkinter
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
        self._set_appearance_mode("dark")
        plt.axis('off')

        self.gui = gui.gui(master=self)
        self.focus_force() # bring window into focus on app open


    def load_text_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            return file_content
        except Exception as e:
            print(f"Error: {e}")

    def start_vis(self, vis):
        if (not vis.complete):
            self.gui.canvas.update_plot(vis)
            vis.step()
            self.after(500, self.start_vis, vis)
    
    def button_click(self):
        vis = searches.linear_search(time.time())
        self.start_vis(vis)
    
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()