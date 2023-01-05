import tkinter as tk
# DON'T WORRY ABOUT ANY OF THIS CODE
root = tk.Tk()#=====================
frame = tk.Frame(root)#=============
frame.pack()#=======================
# DON'T WORRY ABOUT ANY OF THIS CODE

# Don't need this function if we use a lambda 
# def say_hi():
#     print("HELLO!")

button = tk.Button(frame, 
                    text="CLICK ME", 
                    fg="red",
                    command=lambda: print("Hello"))



# DON'T WORRY ABOUT ANY OF THIS CODE
button.pack(side=tk.LEFT) #=========
root.mainloop() #===================
# DON'T WORRY ABOUT ANY OF THIS CODE

# Above is instructors notes
# My notes: the lambda eliminates the need to write the function on lines 8-10.  Instead of "command= say_hi()" on line 15, the lambda syntax can be used instead as shown.