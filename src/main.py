import customtkinter
import gui as gui
import searches as searches
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set window properties
        self.title("AlgoVis")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=8)
        self.grid_rowconfigure(0, weight=1)
        customtkinter.set_appearance_mode("dark")

        # init first vis
        self.gui = gui.gui(master=self)
        self.vis = searches.LinearSearch(time.time())
        self.gui.canvas.init_plot(self.vis)
        self.gui.description.update_text()
        self.focus_force() # bring window into focus on app open

    def start_vis(self, vis):
        """Recursive function to step through given visualisation
        and update GUI.
        args:
            vis:
                vis object that contains a step() function and complete flag"""
        self.gui.canvas.update_plot(vis)
        if (not vis.complete):
            vis.step()

            # different speeds for different vis
            if type(self.vis) == searches.LinearSearch:
                delay = 100
            elif type(self.vis) == searches.BinarySearch:
                delay = 1500
            # run in background so GUI remains responsive
            self.after(delay, self.start_vis, vis)
        else: # enable button once finished
            self.gui.description.toggle_button_enable()
    
    def vis_button_click(self):
        if self.vis.complete: # Only create new vis if previous is complete
            self.vis = type(self.vis)(time.time())

        self.gui.canvas.init_plot(self.vis)
        self.gui.description.toggle_button_enable()
        self.start_vis(self.vis)
    
    def navbar_button_command(self, state):
        self.vis.complete = True
        match state:
            case "Linear Search":
                self.vis = searches.LinearSearch(time.time())
            case "Binary Search":
                self.vis = searches.BinarySearch(time.time())
        # init new vis
        self.gui.canvas.init_plot(self.vis)
        self.gui.description.update_text()
        self.gui.canvas.update_plot(self.vis)

app = App()
app.mainloop()