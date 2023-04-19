import tkinter as tk
from tkinter import messagebox

# function to display frame
def display_frame():
    global header_frame, body_frame, footer_frame
    header_frame = tk.LabelFrame(window, borderwidth=0)
    body_frame = tk.LabelFrame(window, borderwidth=0)
    footer_frame = tk.LabelFrame(window, borderwidth=0)
    header_frame.grid(row=0, column=0, padx=25, pady=15)
    body_frame.grid(row=0, column=1, padx=25, pady=15)
    footer_frame.grid(row=0, column=2, padx=25, pady=15)
    
    
# function to display the top banner
def header_banner():
    global player, player2
    player = tk.Label(
        header_frame, text=f'Player1 Score: {player1_score}', font=('Papyrus', 12, 'bold'))
    player2 = tk.Label(
        header_frame, text=f'Player2 Score: {player2_score}', font=('Papyrus', 12, 'bold'))
    player.grid(row=0, column=0)
    player2.grid(row=1, column=0)



# function to take player's turn
def button_clicked(b):
    global clicking, count
    if b['text'] == '-' and clicking == True:
        b['text'] = 'X'
        count += 1
        clicking = False
        winner_check()
        
    elif b['text'] == '-' and clicking == False:
        b['text'] = 'O'
        count += 1
        clicking = True
        winner_check()
        
    else:
        messagebox.showerror(
            'Samson Tic Tac Toe Design', ' This position has already been taken \n Choose another position')
        
        
#disalbe buttons when there is a winner
def disable_all_buttons():
    button1.config(state='disabled')
    button2.config(state='disabled')
    button3.config(state='disabled')
    button4.config(state='disabled')
    button5.config(state='disabled')
    button6.config(state='disabled')
    button7.config(state='disabled')
    button8.config(state='disabled')
    button9.config(state='disabled')
        
        
#checking if there is a winner
def winner_check():
    global winner, player1_score, player2_score, player, player2
    #checking if X has won
    winner = False
    if button1['text'] =='X' and button2['text']=='X' and button3['text']=='X':
        button1.config(bg='green')
        button2.config(bg='green')
        button3.config(bg='green')
        winner = True
        player1_score += 1
        player.config(text=f'Player1 Score: {player1_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'X won! CONGRATULATION')
        disable_all_buttons()        
    elif button4['text'] =='X' and button5['text']=='X' and button6['text']=='X':
        button4.config(bg='green')
        button5.config(bg='green')
        button6.config(bg='green')
        winner = True
        player1_score += 1
        player.config(text=f'Player1 Score: {player1_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'X won! CONGRATULATION')
        disable_all_buttons()
    elif button7['text'] =='X' and button8['text']=='X' and button9['text']=='X':
        button7.config(bg='green') 
        button8.config(bg='green')
        button9.config(bg='green')
        winner = True
        player1_score += 1
        player.config(text=f'Player1 Score: {player1_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'X won! CONGRATULATION')
        disable_all_buttons()
    elif button1['text'] =='X' and button5['text']=='X' and button9['text']=='X':
        button1.config(bg='green')
        button5.config(bg='green')
        button9.config(bg='green')
        winner = True
        player1_score += 1
        player.config(text=f'Player1 Score: {player1_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'X won! CONGRATULATION')
        disable_all_buttons()
    elif button3['text'] =='X' and button5['text']=='X' and button7['text']=='X':
        button3.config(bg='green')
        button5.config(bg='green')
        button7.config(bg='green')
        winner = True
        player1_score += 1
        player.config(text=f'Player1 Score: {player1_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'X won! CONGRATULATION')
        disable_all_buttons()
    elif button1['text'] =='X' and button4['text']=='X' and button7['text']=='X':
        button1.config(bg='green')
        button4.config(bg='green')
        button7.config(bg='green')
        winner = True
        player1_score += 1
        messagebox.showinfo('Samson Tic Tac Toe Design', 'X won! CONGRATULATION')
        disable_all_buttons()
    elif button2['text'] =='X' and button5['text']=='X' and button8['text']=='X':
        button2.config(bg='green')
        button5.config(bg='green')
        button8.config(bg='green')
        winner = True
        player1_score += 1
        messagebox.showinfo('Samson Tic Tac Toe Design', 'X won! CONGRATULATION')
        disable_all_buttons()
    elif button3['text'] =='X' and button6['text']=='X' and button9['text']=='X':
        button3.config(bg='green')
        button6.config(bg='green')
        button9.config(bg='green')
        winner = True
        player1_score += 1
        player.config(text=f'Player1 Score: {player1_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'X won! CONGRATULATION')
        disable_all_buttons()   
    # Checking if O has won
    elif button1['text'] =='O' and button2['text']=='O' and button3['text']=='O':
        button1.config(bg='green')
        button2.config(bg='green')
        button3.config(bg='green')
        winner = True
        player2_score += 1
        player2.config(text=f'Player2 Score: {player2_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'O won! CONGRATULATION')
        disable_all_buttons()        
    elif button4['text'] =='O' and button5['text']=='O' and button6['text']=='O':
        button4.config(bg='green')
        button5.config(bg='green')
        button6.config(bg='green')
        winner = True
        player2_score += 1
        player2.config(text=f'Player2 Score: {player2_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'O won! CONGRATULATION')
        disable_all_buttons()
    elif button7['text'] =='O' and button8['text']=='O' and button9['text']=='O':
        button7.config(bg='green')
        button8.config(bg='green')
        button9.config(bg='green')
        winner = True
        player2_score += 1
        player2.config(text=f'Player2 Score: {player2_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'O won! CONGRATULATION')
        disable_all_buttons()
    elif button1['text'] =='O' and button5['text']=='O' and button9['text']=='O':
        button1.config(bg='green')
        button5.config(bg='green')
        button9.config(bg='green')
        winner = True
        player2_score += 1
        player2.config(text=f'Player2 Score: {player2_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'O won! CONGRATULATION')
        disable_all_buttons()
    elif button3['text'] =='O' and button5['text']=='O' and button7['text']=='O':
        button3.config(bg='green')
        button5.config(bg='green')
        button7.config(bg='green')
        winner = True
        player2_score += 1
        player2.config(text=f'Player2 Score: {player2_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'O won! CONGRATULATION')
        disable_all_buttons()
    elif button1['text'] =='O' and button4['text']=='O' and button7['text']=='O':
        button1.config(bg='green')
        button4.config(bg='green')
        button7.config(bg='green')
        winner = True
        player2_score += 1
        player2.config(text=f'Player2 Score: {player2_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'O won! CONGRATULATION')
        disable_all_buttons()
    elif button2['text'] =='O' and button5['text']=='O' and button8['text']=='O':
        button2.config(bg='green')
        button5.config(bg='green')
        button8.config(bg='green')
        winner = True
        player2_score += 1
        player2.config(text=f'Player2 Score: {player2_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'O won! CONGRATULATION')
        disable_all_buttons()
    elif button3['text'] =='O' and button6['text']=='O' and button9['text']=='O':
        button3.config(bg='green')
        button6.config(bg='green')
        button9.config(bg='green')
        winner = True
        player2_score += 1
        player2.config(text=f'Player2 Score: {player2_score}')
        messagebox.showinfo('Samson Tic Tac Toe Design', 'O won! CONGRATULATION')
        disable_all_buttons()
    else:
        if count == 9 and winner == False:
            messagebox.showinfo('Samson Tic Tac Toe Design', 'There is a tie\nThe game will restart')
            restart() 


# function to create and display the buttons
def buttons_play():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    
    button1 = tk.Button(body_frame, text='-', font=('montserat', 15), width=6, padx=10, pady=10, height=3,
                        bg='#36454F', fg='white', command=lambda: button_clicked(button1))
    button2 = tk.Button(body_frame, text='-', font=('montserat', 15), width=6, padx=10, pady=10, height=3,
                        bg='#36454F', fg='white', command=lambda: button_clicked(button2))
    button3 = tk.Button(body_frame, text='-', font=('montserat', 15), width=6, padx=10, pady=10, height=3,
                        bg='#36454F', fg='white', command=lambda: button_clicked(button3))
    button4 = tk.Button(body_frame, text='-', font=('montserat', 15), width=6, padx=10, pady=10, height=3,
                        bg='#36454F', fg='white', command=lambda: button_clicked(button4))
    button5 = tk.Button(body_frame, text='-', font=('montserat', 15), width=6, padx=10, pady=10, height=3,
                        bg='#36454F', fg='white', command=lambda: button_clicked(button5))
    button6 = tk.Button(body_frame, text='-', font=('montserat', 15), width=6, padx=10, pady=10, height=3,
                        bg='#36454F', fg='white', command=lambda: button_clicked(button6))
    button7 = tk.Button(body_frame, text='-', font=('montserat', 15), width=6, padx=10, pady=10, height=3,
                        bg='#36454F', fg='white', command=lambda: button_clicked(button7))
    button8 = tk.Button(body_frame, text='-', font=('montserat', 15), width=6, padx=10, pady=10, height=3,
                        bg='#36454F', fg='white', command=lambda: button_clicked(button8))
    button9 = tk.Button(body_frame, text='-', font=('montserat', 15), width=6, padx=10, pady=10, height=3,
                        bg='#36454F', fg='white', command=lambda: button_clicked(button9))
    # first row display
    button1.grid(row=1, column=0, padx=1, pady=1)
    button2.grid(row=1, column=1, padx=1, pady=1)
    button3.grid(row=1, column=2, padx=1, pady=1)
    # second row display
    button4.grid(row=2, column=0, padx=1, pady=1)
    button5.grid(row=2, column=1, padx=1, pady=1)
    button6.grid(row=2, column=2, padx=1, pady=1)
    # third row display
    button7.grid(row=3, column=0, padx=1, pady=1)
    button8.grid(row=3, column=1, padx=1, pady=1)
    button9.grid(row=3, column=2, padx=1, pady=1)
    
    
#function to restart the game
def restart():
    global count
    header_banner()
    buttons_play()
    footer_displaying()
    count = 0

def menu():
    header_banner()
    buttons_play()
    footer_displaying()

# function for footer display
def footer_displaying():
    button10 = tk.Button(footer_frame, text='Restart', width=12, pady=15, bg='black', fg='white', font=('montserat', 12), command=restart)
    # button display
    button10.grid(row=3, column=0)


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry('700x400')
    window.resizable(0, 0)
    window.title("Tic_Tac_Toe Game Samson's Design")
    window.config(bg='#98AFC7')
    
    
    # checking for first player to play and keeping track of counts
    clicking = True
    count = 0
    player1_score = 0
    player2_score = 0



    display_frame()
    menu()
    

    window.mainloop()
