                                                    # rock paper scissors game
d=input("Welcome to rock, paper, scissor game.\nPress enter to continue:")
up=0
cp=0
rock=r"""
   ___
  /   \
 |     |
 |     |
  \___/
"""
scissors=r"""
 \   /
  \ /
   x
  0 0
"""
paper=r"""
 _________
|         |
|         |
|         |
|_________|
"""
i=[0,1,2]
s=[rock,paper,scissors]
while up>=0:
    a=int(input("enter the following for your turn: enter 0 for rock. enter 1 for paper. enter 2 for sciccor\nenter your input: "))
    if a==0 or a==1 or a==2:
        import random
        b=random.randint(0,2)
        print(s[a])
        print(s[b])
        if a==b:
            up=up+1
            cp=cp+1
            print(f"both of us will get a point.\nyour total points was {up}.\nmy total points was {cp}")
            if up==3:
                print("you won the game.")
                break
            elif cp==3:
                print("you lost the game.")
                break
            elif up==3 and cp==3:
                print("DRAW")
            else:
                continue
        elif a==0 and b==1:
            cp=cp+1
            print(f"I will get one point.\nMy total points was {cp}.\nyour total points was {up}.")
            if cp==3:
                print("you lost the game.")
                break
            else:
                continue
        elif a==0 and b==2:
            up=up+1
            print(f"you will get one point.\nYour total points was {up}.\nmy total points was {cp}.")
            if up==3:
                print("you won the game.")
                break
            else:
                continue
        elif a==1 and b==0:
            up=up+1
            print(f"you will get one point.\nYour total points was {up}.\nmy total points was {cp}.")
            if up==3:
                print("you won the game.")
                break
            else:
                continue
        elif a==1 and b==2:
            cp=cp+1
            print(f"I will get one point.\nMy total points was {cp}.\nyour total points was {up}.")
            if cp==3:
                print("you lost the game.")
                break
            else:
                continue
        elif a==2 and b==0:
            cp=cp+1
            print(f"I will get one point.\nMy total points was {cp}.\nyour total points was {up}.")
            if cp==3:
                print("you lost the game.")
                break
            else:
                continue
        else:
            up=up+1
            print(f"you will get one point.\nYour total points was {up}.\nmy total points was {cp}.")
            if up==3:
                print("you won the game.")
                break
            else:
                continue
    else:
        print("YOU LOST!\nBecause you entered an invalid number.")
        break