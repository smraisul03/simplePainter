# Importing important packages for functions
from tkinter import *
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageDraw
import PIL

# Initializing window and the canvas
WIDTH, HEIGHT = 500, 500
CENTER = WIDTH // 2
WHITE = (255, 255, 255)


# Main class for the program
class PaintGUI:

    def __init__(self):

        # Setting title, initial colors for brush and canvas, buttons and their respective frames, and deleting protocol
        self.root = Tk()
        self.root.title(" ")

        self.brush_width = 15
        self.current_color = "#000000"

        self.cnv = Canvas(self.root, width=WIDTH - 10, height=HEIGHT - 10, bg="white")
        self.cnv.pack()
        self.cnv.bind("<B1-Motion>", self.paint)

        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = ImageDraw.Draw(self.image)

        self.button_frame = Frame(self.root)
        self.button_frame.pack(fill=X)

        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)

        self.clear_button = Button(self.button_frame, text="CLEAR", command=self.clear)
        self.clear_button.place()
        self.clear_button.grid(row=1, column=1, sticky=W + E)

        self.save_button = Button(self.button_frame, text="SAVE", command=self.save)
        self.save_button.grid(row=1, column=2, sticky=W + E)

        self.brushplus_button = Button(self.button_frame, text="B+", command=self.brushplus)
        self.brushplus_button.grid(row=0, column=0, sticky=W + E)

        self.brushminus_button = Button(self.button_frame, text="B-", command=self.brushminus)
        self.brushminus_button.grid(row=1, column=0, sticky=W + E)

        self.color_Button = Button(self.button_frame, text="CHANGE COLOR", command=self.color)
        self.color_Button.grid(row=0, column=1, sticky=W + E)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes("-topmost", True)
        self.root.mainloop()

    # Setting up the painting function of the program
    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.cnv.create_rectangle(x1, y1, x2, y2, outline=self.current_color, fill=self.current_color,
                                  width=self.brush_width)
        self.draw.rectangle([x1, y1, x2 + self.brush_width, y2 + self.brush_width], outline=self.current_color,
                            fill=self.current_color, width=self.brush_width)

    # Setting up the clearing function of the program
    def clear(self):
        self.cnv.delete("all")
        self.draw.rectangle([0, 0, 1000, 1000], fill="white")

    # Initializing the saving function of the program
    def save(self):
        filename = filedialog.asksaveasfilename(initialfile="untitled.png", defaultextension="png",
                                                filetypes=[("PNG", ".png"), ("JPG", ".jpg")])

        if filename != "":
            self.image.save(filename)

    # Setting up the function for increasing brush size
    def brushplus(self):
        self.brush_width += 1

    # Setting up the function for decreasing brush size
    def brushminus(self):
        if self.brush_width > 1:
            self.brush_width -= 1

    # Setting up the function for color coordination
    def color(self):
        _, self.current_color = colorchooser.askcolor(title="Color")

    # Setting up the function for closing protocol, by asking users whether they want to save, close, or cancel closing
    def on_closing(self):
        answer = messagebox.askyesnocancel("Quit", "Save Your Work?", parent=self.root)
        if answer is not None:
            if answer:
                self.save()
            self.root.destroy()
            exit(0)


# Initialize the program to run
PaintGUI()
