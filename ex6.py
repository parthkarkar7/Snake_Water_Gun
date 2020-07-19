import random

max=10
troops=["Snake","Water","Gun"]
troops_dic={"S":"Snake","W":"Water","G":"Gun"}

Com_win=0
User_win=0

Tie=0
Win_keyword=""

def com_rnd_data():
    return random.choice(troops)

print("\n\t\tTotal Play 10 Rounds Game\n")

try:
    i=0
    while i < max:

        Answer={}
        Win_keyword=""
        Com_troops=""
        User_troops=""

        print(f"\n\t\tRound : {i+1}")

        User_input=input("\n\t Press S For Snake \n\t Press W For Water \n\t Press G For Gun \n\n\tEnter Your Choice : ")
        User_troops=troops_dic[User_input.capitalize()]

        Com_troops=com_rnd_data()

        Answer={"Com":Com_troops,"User":User_troops}

        if Com_troops=="Snake" and User_troops=="Water" or Com_troops=="Water" and User_troops=="Snake":
            Win_keyword="Snake"

        elif Com_troops=="Gun" and User_troops=="Water" or Com_troops=="Water" and User_troops=="Gun":
            Win_keyword="Water"
        
        elif Com_troops=="Gun" and User_troops=="Snake" or Com_troops=="Snake" and User_troops=="Gun":
            Win_keyword="Gun"

        elif Com_troops=="Snake" and User_troops=="Snake":
            Tie=Tie+1
            print(f"\n\t\t\t Tie ! this Round")
        
        elif Com_troops=="Water" and User_troops=="Water":
            Tie=Tie+1
            print(f"\n\t\t\t Tie ! this Round")
        
        elif Com_troops=="Gun" and User_troops=="Gun":
            Tie=Tie+1
            print(f"\n\t\t\t Tie ! this Round")

        if Win_keyword != "":
            for keys,values in Answer.items():
               if values==Win_keyword:

                    if keys=="Com":
                        Com_win=Com_win+1
                        print(f"\n\t\t\tYou Lose ! this Round")

                    else:
                        User_win=User_win+1
                        print(f"\n\t\t\tYou Win ! this Round")
                            
        i=i+1

        Win_keyword=""

except User_input:
    print("Invalid Input!")

print(f"\n\n\t Total Round : 10 \n\n\t\t You Win : {User_win } \n\n\t\t You Lose : {Com_win } \n\n\t\t Tie : {Tie } \n\n")