import customtkinter

class navbarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

class canvasFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

class descriptionFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("AlgoVis")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=8)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)

        self.nav_frame = navbarFrame(master=self)
        self.nav_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nesw")

        self.canvas_frame = canvasFrame(master=self)
        self.canvas_frame.grid(row=1, column=0, padx=(20,0), pady=20, sticky= "nesw")

        self.desc_frame = descriptionFrame(master=self)
        self.desc_frame.grid(row=1, column=1, padx=(0,20), pady=20, sticky= "nse")

    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()