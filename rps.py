import random
Cchoice=["Rock","Paper","Scissor"]
while True:
    print("Rock Paper Scissor Game:")
    youwin,computerwin=0,0
    for i in range(1,6):
        print("Round",i,"Start:")
        print("Please select one option:")
        print("1.Rock","2.Paper","3.Scissor",sep="\n")
        Yourchoice=int(input())
        if Yourchoice==1:
            print("You select Rock")
            Yourchoice="Rock"
        elif Yourchoice==2:
            print("You select Paper")
            Yourchoice="Paper"
        elif Yourchoice==3:
            print("You select Scissor")
            Yourchoice="Scissor"
        else:
            print("Invalid Choice")
            break
        Computerchoice=random.choice(Cchoice)
        print("Computer select:",Computerchoice)
        if Yourchoice==Computerchoice:
            youwin+=1
            computerwin+=1
            print("This Round is Drawn:")
        elif (Yourchoice=="Paper" and Computerchoice=="Rock") or (Yourchoice=="Rock" and Computerchoice=="Scissor") or (Yourchoice=="Scissor" and Computerchoice=="Paper"):
            youwin+=1
            print("You win this Round")
        else:
            computerwin+=1
            print("Computer win this Round")
    if youwin>computerwin:
        print("You win the game:")
        print("Score is :","Your score:",youwin,"Computer score:",computerwin,sep=" ")
    elif computerwin>youwin:
        print("You Lose the game, Computer win the game:")
        print("Score is:","Your score:",youwin,"Computer score:",computerwin,sep=" ")
    else:
        print("Match Drawn")
        print("Score is:","Your score:",youwin,"Computer score:",computerwin,sep=" ")
    user_choice=input("Want to play again??(Yes/Exit):")
    if user_choice=="yes" or user_choice=="Yes" or user_choice=="YES":
        continue
    else:
        break
    
