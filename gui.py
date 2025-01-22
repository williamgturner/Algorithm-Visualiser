import customtkinter
import tkinter as tk
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