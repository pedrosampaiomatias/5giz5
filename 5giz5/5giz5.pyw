# 5giz5 app
# Dev by Pedro S. Matias

import itertools
from tkinter import *

from isort import file

# Global variables
Players = {}
PlayersPlaying = []
Team_A = ('', '', '', '', '')
Team_B = ('', '', '', '', '')

# Funtion do edit registered players data - UNUSED FOR NOW
def EditPlayers(playerName, operation, rank = 500):

    # Add player
    if operation == 0:
        Players[playerName] = rank

    # Remove player
    elif operation == 1:
        if playerName in Players.keys():
            del Players[playerName]
        else:
            print('Error 404, player not found')

    # Edit player's rank
    elif operation == 2:
        if playerName in Players.keys():
            Players[playerName] = rank
        else:
            print('Error 404, player not found')

def SortTeams():
    global Team_A
    global Team_B
    global PlayersPlaying
    combinationEloDif = {}
    teamCombinations = []
    combinationID = 0
    goalRank = 0
    totalRank = 0
    teamBTmp = []

    # Pulling players list from GUI
    Players[inPlayer1.get()] = int(inRank1.get())
    Players[inPlayer2.get()] = int(inRank2.get())
    Players[inPlayer3.get()] = int(inRank3.get())
    Players[inPlayer4.get()] = int(inRank4.get())
    Players[inPlayer5.get()] = int(inRank5.get())
    Players[inPlayer6.get()] = int(inRank6.get())
    Players[inPlayer7.get()] = int(inRank7.get())
    Players[inPlayer8.get()] = int(inRank8.get())
    Players[inPlayer9.get()] = int(inRank9.get())
    Players[inPlayer10.get()] = int(inRank10.get())

    PlayersPlaying = Players.keys()
    
    # Calculating the goal rank sum for each team
    for player in PlayersPlaying:
        goalRank = goalRank + Players[player]

    goalRank = goalRank / 2

    # Creating all teams possibilities and calculating their ranks
    for subset in itertools.combinations(PlayersPlaying, 5):
        teamCombinations.append(subset)

    for combination in teamCombinations:
        totalRank = 0
        for player in combination:
            totalRank = totalRank + Players[player]
        combinationEloDif[combinationID] = abs(goalRank - totalRank)
        combinationID = combinationID + 1

    # Creating team A using the combination most close to the goal rank
    Team_A = teamCombinations[min(combinationEloDif, key=combinationEloDif.get)]

    # Creating team B using the remaing plaers
    for player in PlayersPlaying:
        if player not in Team_A:
            teamBTmp.append(player)
    
    Team_B = tuple(teamBTmp[:])

    # Updating labels
    lbPlayer1.config(text=Team_A[0])
    lbRank1.config(text=Players[Team_A[0]])
    lbPlayer2.config(text=Team_A[1])
    lbRank2.config(text=Players[Team_A[1]])
    lbPlayer3.config(text=Team_A[2])
    lbRank3.config(text=Players[Team_A[2]])
    lbPlayer4.config(text=Team_A[3])
    lbRank4.config(text=Players[Team_A[3]])
    lbPlayer5.config(text=Team_A[4])
    lbRank5.config(text=Players[Team_A[4]])

    lbPlayer6.config(text=Team_B[0])
    lbRank6.config(text=Players[Team_B[0]])
    lbPlayer7.config(text=Team_B[1])
    lbRank7.config(text=Players[Team_B[1]])
    lbPlayer8.config(text=Team_B[2])
    lbRank8.config(text=Players[Team_B[2]])
    lbPlayer9.config(text=Team_B[3])
    lbRank9.config(text=Players[Team_B[3]])
    lbPlayer10.config(text=Team_B[4])
    lbRank10.config(text=Players[Team_B[4]])

def PrintMatchup():
    global Team_A
    global Team_B

    print('\nTeam A:')
    print(str(Team_A))
    print('\nTeam_B:')
    print(str(Team_B) + '\n\n')

# Gui ==========================================================================================================================================

root = Tk()
root.title("5giz5")
root.geometry("1200x600")
root.resizable(True, True)
root.configure(background='#cacaca')
#root.iconbitmap('D:\\Codes\\Python\\Match up\\Images\\5giz5.ico')


# Teams title =================================================================

lbTeamA = Label(root, text="Team A", font=("Halvetica", 14, "bold"), background='#cacaca')
lbTeamA.place(x=300, y=20, anchor=NE)

lbTeamB = Label(root, text="Team B", font=("Halvetica", 14, "bold"), background='#cacaca')
lbTeamB.place(x=360, y=20)


# Team A players ==============================================================

lbPlayer1 = Label(root, text=Team_A[0], font=("Halvetica", 14, "bold"), background='#cacaca')
lbPlayer1.place(x=300, y=70, anchor=NE)

lbPlayer2 = Label(root, text=Team_A[1], font=("Halvetica", 14, "bold"), background='#cacaca')
lbPlayer2.place(x=300, y=120, anchor=NE)

lbPlayer3 = Label(root, text=Team_A[2], font=("Halvetica", 14, "bold"), background='#cacaca')
lbPlayer3.place(x=300, y=170, anchor=NE)

lbPlayer4 = Label(root, text=Team_A[3], font=("Halvetica", 14, "bold"), background='#cacaca')
lbPlayer4.place(x=300, y=220, anchor=NE)

lbPlayer5 = Label(root, text=Team_A[4], font=("Halvetica", 14, "bold"), background='#cacaca')
lbPlayer5.place(x=300 ,y=270, anchor=NE)

# Team A rank =================================================================

lbRank1 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank1.place(x=50, y=70)

lbRank2 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank2.place(x=50, y=120)

lbRank3 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank3.place(x=50, y=170)

lbRank4 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank4.place(x=50, y=220)

lbRank5 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank5.place(x=50, y=270)

# Team B players ==============================================================

lbPlayer6 = Label(root, text=Team_B[0], font=("Halvetica", 14, "bold"), justify='right', background='#cacaca')
lbPlayer6.place(x=360, y=70)

lbPlayer7 = Label(root, text=Team_B[0], font=("Halvetica", 14, "bold"), justify='right', background='#cacaca')
lbPlayer7.place(x=360, y=120)

lbPlayer8 = Label(root, text=Team_B[0], font=("Halvetica", 14, "bold"), justify='right', background='#cacaca')
lbPlayer8.place(x=360, y=170)

lbPlayer9 = Label(root, text=Team_B[0], font=("Halvetica", 14, "bold"), justify='right', background='#cacaca')
lbPlayer9.place(x=360, y=220)

lbPlayer10 = Label(root, text=Team_B[0], font=("Halvetica", 14, "bold"), justify='right', background='#cacaca')
lbPlayer10.place(x=360 ,y=270)

# Team B ranks ================================================================

lbRank6 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank6.place(x=570, y=70)

lbRank7 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank7.place(x=570, y=120)

lbRank8 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank8.place(x=570, y=170)

lbRank9 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank9.place(x=570, y=220)

lbRank10 = Label(root, text='', font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank10.place(x=570, y=270)

# Players list ================================================================

lbPlayers = Label(root, text="Player", font=("Halvetica", 14, "bold"), background='#cacaca')
lbPlayers.place(x=880, y=20)

lbRank = Label(root, text="Rank", font=("Halvetica", 14, "bold"), background='#cacaca')
lbRank.place(x=1080, y=20)

inPlayer1 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer1.place(x=880, y=70)

inRank1 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank1.place(x=1080, y=70)

inPlayer2 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer2.place(x=880, y=120)

inRank2 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank2.place(x=1080, y=120)

inPlayer3 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer3.place(x=880, y=170)

inRank3 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank3.place(x=1080, y=170)

inPlayer4 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer4.place(x=880, y=220)

inRank4 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank4.place(x=1080, y=220)

inPlayer5 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer5.place(x=880, y=270)

inRank5 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank5.place(x=1080, y=270)

inPlayer6 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer6.place(x=880, y=320)

inRank6 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank6.place(x=1080, y=320)

inPlayer7 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer7.place(x=880, y=370)

inRank7 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank7.place(x=1080, y=370)

inPlayer8 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer8.place(x=880, y=420)

inRank8 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank8.place(x=1080, y=420)

inPlayer9 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer9.place(x=880, y=470)

inRank9 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank9.place(x=1080, y=470)

inPlayer10 = Entry(root, font=("Halvetica", 14, "bold"), width=15)
inPlayer10.place(x=880, y=520)

inRank10 = Entry(root, font=("Halvetica", 14, "bold"), width=4)
inRank10.place(x=1080, y=520)

# Match making buttom =========================================================

btMatchMaking = Button(root, text='Match', font=("Halvetica", 14, "bold"), background='#cacaca', command=SortTeams)
btMatchMaking.place(x=330, y=340, anchor=CENTER)

root.mainloop()