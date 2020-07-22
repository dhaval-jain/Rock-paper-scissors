import tkinter
from PIL import ImageTk ,Image
import random

top = tkinter.Tk()
top.title("ROCK PAPER SCISSORS")
top.geometry("340x430")
count=0
frame1 = tkinter.Frame(top)


def display(result):
    '''output = tkinter.Text(top)
    var = result
    output.insert(tkinter.INSERT,var)
    output.pack()'''
    ##frame = tkinter.Frame(top)

    var = result
    msg = tkinter.Message(frame1,text = var,relief = tkinter.RAISED)
    #count += 1
    #var.set(result)
    msg.pack()
    #if count >= 10:
    #clear = tkinter.Button(frame,text="CLEAR SCREEN",command = msg.destroy).pack()
    frame1.pack()
    

def game(choice):
    computer = random.randint(0,2)
    print("user chose: ",choice)
    print('Computer choose : ', computer)
    result_matrix = [[0, 2, 1],
                    [1, 0, 2], 
                    [2, 1, 0],
                    [3, 3, 3]]
    result_idx = result_matrix[choice][computer]
    result_message = ['Tie!', 'You Win', 'You Lose!', 'Invalid!']
    result = result_message[result_idx]
    display(result)
    return result
    


r = ImageTk.PhotoImage(Image.open (r"C:\Users\global\Desktop\STONE_PAPER_SCISSORS\rock.PNG"))
p = ImageTk.PhotoImage(Image.open (r"C:\Users\global\Desktop\STONE_PAPER_SCISSORS\paper.PNG"))
s = ImageTk.PhotoImage(Image.open (r"C:\Users\global\Desktop\STONE_PAPER_SCISSORS\scissors.PNG"))


rock = tkinter.Button(top,text="ROCK",image = r,activebackground = "black",bd = 5,command = lambda : game(0))
rock.pack()

paper = tkinter.Button(top,text="PAPER",image = p,activebackground = "black",bd = 5,command = lambda : game(1))
paper.pack()

scissors = tkinter.Button(top,text="SCISSORS",image = s,activebackground = "black",bd = 5,command = lambda : game(2))
scissors.pack()

close = tkinter.Button(top,text="EXIT",activebackground = "black",activeforeground = "white",bd = 5,width = 20,command = top.destroy)
close.pack()

tensai = tkinter.Button(frame1,text = "clear frame",command = frame1.destroy).pack()

top.mainloop()





'''   text1.delete('1.0', END)
text1.update() '''