import tkinter
from PIL import Image, ImageFilter, ImageTk
import PIL

window = tkinter.Tk()

window.geometry("500x500")  # Set window width and height 

window.title("My First GUI Program")

#Go image
def run(event):  # Define a function to be called when the label is clicked
    tkinter.Label(window, text="run").pack()

#icon = tkinter.PhotoImage(file="stupid.png")
icon = ImageTk.PhotoImage(Image.open("stupid.png").resize((50, 50)))

label = tkinter.Label(window, image=icon)
label.bind("<Button-1>", run)  # Bind the function, not the function call
label.pack()


#####
def left_click(event):
    tkinter.Label(window, text = "left click").pack()
def right_click(event):
    tkinter.Label(window, text = "right click").pack()

window.bind("<Button-3>", left_click)
window.bind("<Button-1>", right_click)


# create function
def say_hi(event):  # Add 'event' parameter
    tkinter.Label(window, text="Hi").pack()
def say_hello():
    tkinter.Label(window, text="Hello World").pack()
    pil()
tkinter.Button(window, text="click me", command=say_hello).pack()
#these 3 btn below same fuction ass 1 line above
btn = tkinter.Button(window, text="click me 2")
btn.bind("<Button-1>", say_hi)
btn.pack()

def pil():
    # Opens a image in RGB mode
    im = Image.open(r"stupid.png")
    # Blurring the image
    im1 = im.filter(ImageFilter.BLUR)
    im1 = im1.rotate(90, PIL.Image.NEAREST, expand = 1)
    # Shows the image in image viewer
    im1.show()
# #create 2 text labels and input labels
# tkinter.Label(window, text="Username").grid(row=0) # this is placed in 0 0
# tkinter.Entry(window).grid(row=0, column=1) # this is placed in 0 1
# tkinter.Label(window, text="Password").grid(row=1,column=0) # this is placed in 0 1
# tkinter.Entry(window).grid(row=1, column=1) # this is placed in 1 1
# tkinter.Checkbutton(window,text="Keep Me Logged In").grid(columnspan=2) # this is placed in 0 0


# #width
# tkinter.Label(window, text="Hello World",fg="red",bg="yellow").pack()
# tkinter.Label(window, text="top",fg="red",bg="purple").pack(fill="x")
# tkinter.Label(window, text="bottom",fg="blue",bg="yellow").pack(side="left", fill="y")


#create 2 frame
# top_frame = tkinter.Frame(window).pack()
# bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# btn1 = tkinter.Button(top_frame, text="Button 1", fg="red").pack()
# btn2 = tkinter.Button(top_frame, text="Button 2", fg="green").pack()

# btn3 = tkinter.Button(bottom_frame, text="Button 3", fg="blue").pack(side=tkinter.LEFT)
# btn4 = tkinter.Button(bottom_frame, text="Button 4", fg="purple").pack(side=tkinter.LEFT)




window.mainloop()