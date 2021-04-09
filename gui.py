from content_based import *
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

def similar_movie():
    
    sim_str = ''
    sim_list = []
    try:
        movie_name = str(user_id.get())
        if(len(movie_name)<1):
            messagebox.showinfo('Try Again','No Matched Movie Found')
        else:
            sim_list = recommend(movie_name)
            sim_str = '\n'.join(sim_list)
            lbl['text'] = sim_str
        
    except:
        messagebox.showinfo('Try Again','No Matched Movie Found')


omk = Tk()  
omk.title("Movie Recommendation System")
omk.resizable(height = None, width = None)


# Label 1
lbl = Label(omk, text = "Movie Recommender System",font=("Times New Roman", 20))
lbl.grid(row=0,column=0,padx=(10, 10),pady=(10 ,10))

# Frame
frame = ttk.Frame(omk, padding=10)
frame.grid(row=3,column=0)

global user_id


user_id = None

# Label 2
lbl1 = Label(frame, text = "Enter Movie Name",font=("Times New Roman", 15))
lbl1.grid(row=2,column=0,padx=(10, 0))

# Input Box
entry = Entry(frame, width=30)
entry.grid(row=4,column=0,padx=(10, 0))
user_id = entry

# Button
btn2 = ttk.Button(frame,text = 'Similar Movies', command=similar_movie)
btn2.grid(row=5,column=0,padx=(10,0))


omk.mainloop() 