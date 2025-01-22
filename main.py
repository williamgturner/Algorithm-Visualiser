import customtkinter
import tkinter as tk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import gui

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("AlgoVis")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=8)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=100)
        plt.axis('off')

        # init navbar and nav buttons
        self.nav_frame = gui.navbarFrame(master=self)
        self.nav_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=(20,0), sticky="ew")
        algos = ["Linear Search", "Binary Search", "Quick Sort", "Insertion Sort", "Bubble Sort", "Selection Sort", "Bogo Sort"]
        self.segmented_button = customtkinter.CTkSegmentedButton(self.nav_frame, values=algos, command=self.button_callback)
        self.segmented_button.grid(row=0, column=0, padx=5, pady=5, sticky = "ew")
        self.segmented_button.set("Binary Search")

        # init visualisation frame
        self.canvas_frame = gui.canvasFrame(master=self)
        self.canvas_frame.grid(row=1, column=0, padx=(20, 0), pady=(5,20), sticky= "nesw")

        # init description frame, text and button
        self.desc_frame = gui.descriptionFrame(master=self)
        self.desc_frame.grid(row=1, column=1, padx=(5,20), pady=(5,20), sticky= "nsew")
        self.desc_frame.grid_rowconfigure(0, weight=0)
        self.desc_frame.grid_rowconfigure(1, weight=1)
        self.desc_frame.grid_rowconfigure(2, weight=0)
        self.desc_frame.grid_columnconfigure(0, weight=1)

        self.title_label = customtkinter.CTkLabel(self.desc_frame, text="Lorem Ipsum")
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.desc_text = customtkinter.CTkTextbox(self.desc_frame, wrap="word")
        self.desc_text.grid(row=1, column=0, padx=5, pady=5, sticky="nesw")
        self.load_text_from_file("./resources/lorem_ipsum.txt")
        self.startVisButton = customtkinter.CTkButton(self.desc_frame, text="Start Visualisation", command=self.start_vis)
        self.startVisButton.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # init seaborn plot
        self.plot_data = sns.load_dataset("penguins")
        self.plot = sns.barplot(data=self.plot_data, x="species", y="bill_length_mm")
        self.canvas_frame.embed_plot(self.plot)
        
        self.focus_force() # bring window into focus on app open


    def load_text_from_file(self, file_path):
        try:
            # Open the file and read its content
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            # Insert the file content into the textbox
            self.desc_text.delete(1.0, customtkinter.END)  # Clear any existing text
            self.desc_text.insert(0.0, file_content)  # Insert the file content at the end
        except Exception as e:
            print(f"Error: {e}")
        
    def start_vis(self):
        print("Visualisation Started")
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()