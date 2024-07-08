import tkinter as tk
from tkinter import ttk

class AnimatedProgressBar:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Progress Bar with Gradient Color")
        
        self.canvas_width = 300
        self.canvas_height = 50
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(pady=20)
        
     
        self.start_color = "#ff6347" 
        self.end_color = "#00bfff"    
        
        self.progress = 0
        self.animation_speed = 20 
        self.animate_progress()
    
    def draw_progress_bar(self):
        self.canvas.delete("progress_bar")
        
        bar_width = int(self.canvas_width * (self.progress / 100))
        
        color = self.calculate_gradient_color()
        
        self.canvas.create_rectangle(0, 0, bar_width, self.canvas_height, fill=color, width=0, tags="progress_bar")
    
    def animate_progress(self):
        if self.progress < 100:
            self.progress += 1
            self.draw_progress_bar()
            self.root.after(self.animation_speed, self.animate_progress)
        else:
            print("Progress Complete")
    
    def calculate_gradient_color(self):
        r1, g1, b1 = self.hex_to_rgb(self.start_color)
        r2, g2, b2 = self.hex_to_rgb(self.end_color)
        
        r = int(r1 + (r2 - r1) * (self.progress / 100))
        g = int(g1 + (g2 - g1) * (self.progress / 100))
        b = int(b1 + (b2 - b1) * (self.progress / 100))
        
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.strip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2 ,4))

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedProgressBar(root)
    root.mainloop()
