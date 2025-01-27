import customtkinter
import gui
import searches
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set window properties
        self.title("AlgoVis")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=8)
        self.grid_rowconfigure(0, weight=1)
        self._set_appearance_mode("dark")

        self.gui = gui.gui(master=self)
        self.focus_force() # bring window into focus on app open

    def load_text_from_file(self, file_path):
        """Loads and returns text string from given file
        args:
            file_path:
                string file path to retrieve text from"""
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            return file_content
        except Exception as e:
            print(f"Error: {e}")

    def start_vis(self, vis):
        """Recursive function to step through given visualisation
        and update GUI.
        args:
            vis:
                vis object that contains a step() function and complete flag

        """
        self.gui.canvas.update_plot(vis)
        if (not vis.complete):
            vis.step()
            # run in background so GUI remains responsive
            self.after(500, self.start_vis, vis)
        else:
            self.gui.description.set_button_enable()
    
    def vis_button_click(self):
        vis = searches.linear_search(time.time())
        self.gui.description.set_button_enable()
        self.start_vis(vis)
    
    def navbar_button_command(self, state):
        self.gui.description.update_text()

app = App()
app.mainloop()