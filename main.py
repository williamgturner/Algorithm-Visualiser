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
        self.grid_rowconfigure(1, weight=100)

        self.nav_frame = navbarFrame(master=self)
        self.nav_frame.grid(row=0, column=0, padx=(20,0), pady=(20,0), sticky="ew")

        self.canvas_frame = canvasFrame(master=self)
        self.canvas_frame.grid(row=1, column=0, padx=(20, 0), pady=(5,20), sticky= "nesw")

        self.desc_frame = descriptionFrame(master=self)
        self.desc_frame.grid(row=1, column=1, padx=(5,20), pady=(5,20), sticky= "nsew")
        self.desc_frame.grid_rowconfigure(0, weight=0)
        self.desc_frame.grid_rowconfigure(1, weight=1)
        self.desc_frame.grid_rowconfigure(2, weight=0)
        self.desc_frame.grid_columnconfigure(0, weight=1)

        self.startVisButton = customtkinter.CTkButton(self.desc_frame, text="Start Visualisation", command=self.start_vis)
        self.startVisButton.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.title_label = customtkinter.CTkLabel(self.desc_frame, text="Lorem Ipsum")
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.desc_text = customtkinter.CTkTextbox(self.desc_frame, wrap="word")
        self.desc_text.insert(0.0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis pellentesque lectus. Duis maximus augue a nisi egestas, id vehicula sapien fringilla. Sed porta dui vulputate turpis malesuada, quis venenatis neque maximus. Phasellus efficitur tellus in risus ultrices lobortis. Mauris sed justo hendrerit eros convallis rutrum. Aliquam fringilla tellus a velit efficitur, a volutpat lectus imperdiet. In non tempus nulla. Praesent in massa vel erat sollicitudin fermentum. Nam consectetur nunc leo, et viverra quam maximus quis. Praesent id elit urna. Morbi non lorem blandit, placerat leo et, cursus erat. Suspendisse vestibulum, dolor a cursus sagittis, ipsum mi feugiat justo, sit amet condimentum augue dui vitae urna. Suspendisse condimentum, lectus quis porttitor ornare, lectus eros faucibus leo, vitae semper dui ligula nec leo. Nulla consectetur tellus ac maximus interdum. Nulla facilisi.")
        self.desc_text.grid(row=1, column=0, padx=5, pady=5, sticky="nesw")

        self.binSearchButton = customtkinter.CTkButton(self.nav_frame, text = "BinarySearch", command=self.button_callback)
        self.binSearchButton.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        
        self.focus_force()

    def start_vis(self):
        print("Visualisation Started")
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()