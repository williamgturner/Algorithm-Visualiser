import customtkinter
import tkinter as tk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class navbarFrame(customtkinter.CTkFrame):
    """Frame that holds buttons to select algorithm"""
    def __init__(self, master):
        super().__init__(master)

class canvasFrame(customtkinter.CTkFrame):
    """Frame that holds the matplotlib figure"""
    def __init__(self, master):
        super().__init__(master)
    
    def embed_plot(self, plot):
        """Embeds plot into frame
        
        Creates a regular tk canvas which then holds the matplotlib
        figure. The figure is adjusted to fit within the viewport."""
        fig = plot.get_figure()

        fig.patch.set_facecolor('none')
        frame_width = self.winfo_width()
        frame_height = self.winfo_height()
        
        aspect_ratio = frame_width / frame_height
        fig_width = frame_width * 0.6
        fig_height = fig_width / aspect_ratio
        
        fig.set_size_inches(fig_width / 100, fig_height / 100)  # Convert pixels to inches (100 dpi)
        
        fig.tight_layout()

        canvas =FigureCanvasTkAgg(fig, master = self)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas.get_tk_widget().pack(padx=5, pady=(50,0), fill=tk.BOTH, expand=True)
        canvas_widget.config(bg='lightgray')

class descriptionFrame(customtkinter.CTkFrame):
    """Frame that holds the description text for given algorithm"""
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
        self.nav_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=(20,0), sticky="ew")

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

        algos = ["Linear Search", "Binary Search", "Quick Sort", "Insertion Sort", "Bubble Sort", "Selection Sort", "Bogo Sort"]
        self.segmented_button = customtkinter.CTkSegmentedButton(self.nav_frame, values=algos, command=self.button_callback)
        self.segmented_button.grid(row=0, column=0, padx=5, pady=5, sticky = "ew")
        self.segmented_button.set("Binary Search")
        #self.binSearchButton = customtkinter.CTkButton(self.nav_frame, text = "Binary Search", command=self.button_callback)
        #self.binSearchButton.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # init seaborn plot
        self.plot_data = sns.load_dataset("penguins")
        self.plot = sns.barplot(data=self.plot_data, x="species", y="bill_length_mm")
        plt.axis('off')
        self.canvas_frame.embed_plot(self.plot)
        
        
        self.focus_force() # bring window into focus on app open

    def start_vis(self):
        print("Visualisation Started")
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()