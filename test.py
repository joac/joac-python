import Tkinter as tk
 
def key(event):
    if event.keysym == 'Escape':
        root.destroy()
    print event.char
    print event
    print event.keysym
         
root = tk.Tk()
print "Press a key (Escape key to exit):"
root.bind_all('<Key>', key)
#don't show the tk window
root.mainloop()
