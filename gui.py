import customtkinter
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class navbarFrame(customtkinter.CTkFrame):
    """Frame that holds buttons to select algorithm"""
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid(row=0, column=0, padx=20,pady=(20,0),columnspan=2,sticky="ew")
        # init navbar and nav buttons
        algos = ["Linear Search", "Binary Search", "Quick Sort", "Insertion Sort", "Bubble Sort", "Selection Sort", "Bogo Sort"]
        self.segmented_button = customtkinter.CTkSegmentedButton(self, values=algos)
        self.segmented_button.grid(row=0, column=0, padx=5, pady=5, columnspan=2,sticky = "ew")
        self.segmented_button.set("Binary Search")

class canvasFrame(customtkinter.CTkFrame):
    """Frame that holds the matplotlib figure"""
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid(row=1, column=0, padx=(20, 0), pady=(5,20), sticky= "nesw")

        canvas_height = self.winfo_height()
        canvas_width = self.winfo_width()

        figure = Figure(figsize=(canvas_width, canvas_height))
        self.plot = figure.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.get_tk_widget().grid(row=0, column = 0, padx=5, pady=5, sticky="nesw")

        self.plot.set_xticklabels([])
    
    def update_plot(self, search):
        colours = ["skyblue"] * len(search.array)
        colours[search.index] = "red"
        self.plot.clear()
        self.plot.bar(range(len(search.array)), search.array, color= colours)
        self.plot.set_title(f"Target: {search.search_val}")
        self.plot.set_xticklabels([])
        self.plot.set_xlabel(f"Current Index: {search.index}")
        self.canvas.draw()

class descriptionFrame(customtkinter.CTkFrame):
    """Frame that holds the description text for given algorithm"""
    def __init__(self, master):
        super().__init__(master)
         # set pos
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid(row=1, column=1, padx=(5,20), pady=(5,20), sticky= "nsew")

        # init description frame, text and button
        self.title_label = customtkinter.CTkLabel(self, text="Lorem Ipsum")
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.desc_text = customtkinter.CTkTextbox(self, wrap="word")
        self.desc_text.grid(row=1, column=0, padx=5, pady=5, sticky="nesw")
        text = master.master.load_text_from_file("./resources/lorem_ipsum.txt")
        self.desc_text.delete(1.0, customtkinter.END)
        self.desc_text.insert(0.0, text)
        self.startVisButton = customtkinter.CTkButton(self, text="Start Visualisation", command=master.master.button_click)
        self.startVisButton.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

class gui(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, padx=0,pady=0,sticky="nesw")
        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(1, weight=1)    # Canvas frame should expand vertically to fill the rest of the space
        self.navbar = navbarFrame(master=self)
        self.canvas = canvasFrame(master=self)
        self.description = descriptionFrame(master=self)
        # self.navbar.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="ew")