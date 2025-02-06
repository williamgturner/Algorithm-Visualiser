import customtkinter
import algorithms
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import MultipleLocator
matplotlib.use('TkAgg')
class navbarFrame(customtkinter.CTkFrame):
    """Frame that holds buttons to select algorithm"""
    def __init__(self, master):
        super().__init__(master)

        # set pos
        self.grid_columnconfigure(0, weight=1)
        self.grid(row=0, column=0, padx=20,pady=(20,0),columnspan=2,sticky="ew")

        # init navbar and nav buttons
        algos = ["Linear Search", "Binary Search", "Quick Sort",
            "Insertion Sort", "Bubble Sort", "Selection Sort", "Bogo Sort"]
        self.segmented_button = customtkinter.CTkSegmentedButton(self, values=algos,
            command=master.master.navbar_button_command)
        self.segmented_button.grid(row=0, column=0, padx=5,
            pady=5, columnspan=2, sticky = "ew")
        self.segmented_button.set("Linear Search")
    
    def toggle_navbar_enable(self):
        """Toggles navbar buttons disabled state."""
        if self.segmented_button._state == "normal":
            self.segmented_button.configure(state = "disabled")
        else:
            self.segmented_button.configure(state = "normal")


class canvasFrame(customtkinter.CTkFrame):
    """Frame that holds the matplotlib figure"""
    def __init__(self, master):
        super().__init__(master)

        # set pos and configure size
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid(row=1, column=0, padx=(20, 0), pady=(5,20), sticky= "nesw")
        canvas_height = self.winfo_height()
        canvas_width = self.winfo_width()
        figure = Figure(figsize=(canvas_width, canvas_height))
        figure.patch.set_facecolor('none')
        self.plot = figure.add_subplot(1, 1, 1)

        # set plot aesthetics
        self.style_plot()

        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.get_tk_widget().grid(row=0, column = 0,
            padx=5, pady=5, sticky="nesw")
        self.canvas.get_tk_widget().config(bg=self['bg'])

    def style_plot(self):
        """Sets style for matplotlib plot"""
        self.plot.patch.set_facecolor('none')
        self.plot.spines['bottom'].set_color('white')
        self.plot.spines['top'].set_color('none') 
        self.plot.spines['right'].set_color('none')
        self.plot.spines['left'].set_color('white')
        self.plot.yaxis.set_major_locator(MultipleLocator(2))  # Step size 2
        self.plot.set_ylim(0, 20)  # Set y-axis limits
        self.plot.grid(True, axis='y', linestyle='--', color='gray', alpha=0.5)
        self.plot.tick_params(axis='y', labelcolor='white')
        self.plot.set_xticklabels([])

    def init_plot(self, search):
        """Initialise plot for given algorithm
        args:
            search:
                search object"""
        self.plot.clear()
        self.style_plot()
        if isinstance(search, algorithms.SearchAlgorithm):
            self.plot.set_title(f"Target Value: {search.search_val}", color = "white")
            if isinstance(search, algorithms.BinarySearch):
                self.plot.yaxis.set_major_locator(MultipleLocator(10))  # Step size 2
                self.plot.set_ylim(0, 50)  # Set y-axis limits
            
        colours = ["skyblue"] * len(search.array)
        self.plot.bar(range(len(search.array)), search.array, color= colours)
        self.plot.index_arrow = None
    
    def update_plot(self, search):
        """Update plot graphics.
        args:
            search:
                a search object that contains an array and index"""
        
        colours = ["skyblue"] * len(search.array)
        if isinstance(search, algorithms.SearchAlgorithm):
            colours[search.array.index(search.search_val)] = "gold"
        
        try:
            self.plot.index_arrow.remove()
        except AttributeError:
            pass
        except ValueError:
            pass

        if isinstance(search, algorithms.LinearSearch):
            self.plot.set_xlabel(
                "Current Index: " + str(search.index) +
                " | Comparisons: " + str(search.comparisons), color="white")

            if search.complete:
                colours[search.index] = "green"
            else:
                colours[search.index] = "red"

        elif isinstance(search, algorithms.BinarySearch):

            colours[search.index] = "red"
            colours[search.lower_index] = "blue"
            colours[search.upper_index] = "blue"

            if search.complete:
                colours = ["skyblue"] * len(search.array)
                colours[search.index] = "green"

            self.plot.set_xlabel(
                "Lower Index: " + str(search.lower_index) +
                " | Upper Index: " + str(search.upper_index) +
                " | Comparisons: " + str(search.comparisons), color="white")
            
        elif isinstance(search, algorithms.BubbleSort):
            colours[search.index] = "red"
            self.plot.set_xlabel(
                "Comparisons: " + str(search.comparisons), color="white")
            if search.complete:
                colours = ["green"] * len(search.array)
        
        elif isinstance(search, algorithms.InsertionSort):
            for i in range(search.index):
                colours[i] = "green"
            if search.position < 0:
                colours[0] = "red"
            else:
                colours[search.position] = "red"
            self.plot.set_xlabel(
                "Comparisons: " + str(search.comparisons), color="white")
            if search.complete:
                colours = ["green"] * len(search.array)

        elif isinstance(search, algorithms.SelectionSort):
            for i in range(search.index):
                colours[i] = "green"
            colours[search.index] = "red"
            self.plot.set_xlabel(
                "Comparisons: " + str(search.comparisons), color="white")

        
        for i, bar in enumerate(self.plot.patches): # set bar colours
                bar.set_color(colours[i])
                bar.set_height(search.array[i])
                if (i == search.index):
                    # annotate current index with red arrow
                    self.plot.index_arrow = self.plot.annotate('',
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5),
                        arrowprops=dict(facecolor='red', shrink=0.05)
                   )
        self.canvas.draw_idle()

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
        self.title_label = customtkinter.CTkLabel(self, 
            text=master.navbar.segmented_button.get())
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.desc_text = customtkinter.CTkTextbox(self, wrap="word")
        self.desc_text.grid(row=1, column=0, padx=5, pady=5, sticky="nesw")
        self.desc_text.delete(1.0, customtkinter.END)
        self.desc_text.configure(state="disabled")
        self.startVisButton = customtkinter.CTkButton(self,
            text="Start Visualisation", command=master.master.vis_button_click)
        self.startVisButton.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    
    def toggle_button_enable(self):
        """Toggles 'start visualisation' button."""
        if self.startVisButton.cget("state") == "normal":
            self.startVisButton.configure(state="disabled")
        else:
            self.startVisButton.configure(state="normal")
    
    def update_text(self):
        """Updates title & description text to current algorithm"""

        # set title text
        self.title_label.configure(text = self.master.navbar.segmented_button.get())
        
        # set description text
        self.desc_text.configure(state="normal")
        self.desc_text.delete(0.0, customtkinter.END)
        if self.master.navbar.segmented_button.get() == "Linear Search":
            text = load_text_from_file(
                "../resources/linear_search_desc.txt")
        elif self.master.navbar.segmented_button.get() == "Binary Search":
            text = load_text_from_file(
                "../resources/binary_search_desc.txt")
        elif self.master.navbar.segmented_button.get() == "Bubble Sort":
            text = load_text_from_file(
                "../resources/bubble_sort_desc.txt")
        elif self.master.navbar.segmented_button.get() == "Insertion Sort":
            text = load_text_from_file(
                "../resources/insertion_sort_desc.txt")
        elif self.master.navbar.segmented_button.get() == "Selection Sort":
            text = load_text_from_file(
                "../resources/selection_sort_desc.txt")
        self.desc_text.insert(0.0, text)
        self.desc_text.configure(state="disabled")

class gui(customtkinter.CTkFrame):
    """Frame that contains all GUI elements"""
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, padx=0,pady=0,sticky="nesw")
        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(1, weight=1)
        self.navbar = navbarFrame(master=self)
        self.canvas = canvasFrame(master=self)
        self.description = descriptionFrame(master=self)

def load_text_from_file(file_path):
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