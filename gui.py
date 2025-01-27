import customtkinter
import tkinter as tk
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class navbarFrame(customtkinter.CTkFrame):
    """Frame that holds buttons to select algorithm"""
    def __init__(self, master):
        super().__init__(master)
        # init navbar and nav buttons
        algos = ["Linear Search", "Binary Search", "Quick Sort", "Insertion Sort", "Bubble Sort", "Selection Sort", "Bogo Sort"]
        self.segmented_button = customtkinter.CTkSegmentedButton(self, values=algos)
        self.segmented_button.grid(row=0, column=0, padx=5, pady=5, columnspan=2,sticky = "ew")
        self.segmented_button.set("Binary Search")
        self.grid_columnconfigure(0, weight=1)

class canvasFrame(customtkinter.CTkFrame):
    """Frame that holds the matplotlib figure"""
    def __init__(self, master):
        super().__init__(master)
    
    def embed_plot(self, plot):
        """Embeds plot into frame
        
        Creates a regular tk canvas which then holds the matplotlib
        figure. The figure is adjusted to fit within the viewport."""
        fig = plot.get_figure()
        fig.tight_layout()

        fig.patch.set_facecolor('none')
        frame_width = self.winfo_width()
        frame_height = self.winfo_height()
        
        aspect_ratio = frame_width / frame_height
        fig_width = frame_width * 0.6
        fig_height = fig_width / aspect_ratio
        
        fig.set_size_inches(fig_width / 100, fig_height / 100)  # Convert pixels to inches (100 dpi)
        

        canvas =FigureCanvasTkAgg(fig, master = self)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas.get_tk_widget().pack(padx=5, pady=(50,0), fill=tk.BOTH, expand=True)
        canvas_widget.config(bg='lightgray')
    
    def update_plot(self, search):
        self.plot_data = search.array
        self.plot = sns.barplot(x=range(len(self.plot_data)), y=self.plot_data)
        self.embed_plot(self.plot)

class descriptionFrame(customtkinter.CTkFrame):
    """Frame that holds the description text for given algorithm"""
    def __init__(self, master):
        super().__init__(master)
        master.grid(row=0, column=0, padx=0,pady=0,sticky="nesw") # set pos
        # init description frame, text and button
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)

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
        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(0, weight=0)    # Navbar doesn't need to take too much height, so set weight 0
        self.grid_rowconfigure(1, weight=1)    # Canvas frame should expand vertically to fill the rest of the space
        self.navbar = navbarFrame(master=self)
        self.navbar.grid(row=0, column=0, padx=20,pady=(20,0),columnspan=2,sticky="ew")
        self.canvas = canvasFrame(master=self)
        self.canvas.grid(row=1, column=0, padx=(20, 0), pady=(5,20), sticky= "nesw")

        self.description = descriptionFrame(master=self)
        self.description.grid(row=1, column=1, padx=(5,20), pady=(5,20), sticky= "nsew")
        # self.navbar.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="ew")