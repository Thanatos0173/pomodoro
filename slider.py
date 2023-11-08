import tkinter as tk


class SliderApp:
    def __init__(self, master,color = "blue"):
        self.master = master
        self.master.title("Canvas Slider")
        self.color = color
        self.canvas = tk.Canvas(self.master, width=400, height=100, bg="white")


        self.border_height = 100  # Set a specific border width

        self.slider_width = 300
        self.slider_height = 20
        self.xCorner = 0
        self.yCorner = 0


        self.maxWidth = self.slider_width + 10 + self.xCorner
        self.maxHeight = self.yCorner + self.slider_height

        self.x = self.maxWidth

        self.canvas.config(width=self.maxWidth,height=self.maxHeight)

        self.border = self.canvas.create_rectangle(self.xCorner, self.yCorner+1, self.maxWidth, self.maxHeight + 1, fill="black")

        self.slider = self.canvas.create_rectangle(self.xCorner +1, self.yCorner+1 , self.maxWidth, self.maxHeight, fill=color)


        self.maxWidth_rect = self.canvas.create_rectangle(self.maxWidth-10, self.yCorner+1, self.maxWidth, self.maxHeight, fill="yellow")

        # Bind mouse events to functions
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # Initial slider positioncustom_function
        self.slider_position = 0.0
        self.bind_function = None


    def on_drag(self, event):
        self.x = event.x
        self.update_slider_position()

    def on_release(self, event):
        self.x = event.x
        self.update_slider_position()

    def calculatePercentage(self): #Doing some maths about lines
        xa = (self.xCorner + 11, 0)
        ya = (self.maxWidth, 100)

        m = (ya[1] - xa[1])/(ya[0] - xa[0])

        p = - m * xa[0]

        return int(m*self.x + p)

    def getXFromPercentage(self,percentage):
        xa = (self.xCorner + 11, 0)
        ya = (self.maxWidth, 100)

        m = (ya[1] - xa[1])/(ya[0] - xa[0])

        p = - m * xa[0]


        return int((percentage-p)/m)

    def update_slider_position(self):
        self.x = max(self.xCorner+11, min(self.maxWidth, self.x))
        self.canvas.coords(self.slider, self.xCorner , self.yCorner+1, self.x, self.maxHeight)
        self.canvas.coords(self.maxWidth_rect, self.x - 10, self.yCorner+1, self.x, self.maxHeight)
        if self.bind_function != None:
            self.bind_function(self.calculatePercentage())

    def bind(self, function):
        # Bind the given function and pass the result of calculatePercentage as an argument
        self.bind_function = function



if __name__ == "__main__":

    root = tk.Tk()
    app = SliderApp(root,"green")
    root.mainloop()
