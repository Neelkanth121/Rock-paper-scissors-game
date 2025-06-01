y=input("Welcome to hangman game. click enter to continue: ")
def hangman_game(y):
    h0=r"""
    ___________
    | o     o |
    |    7    |
    |__-----__|
    """
    h1=r"""
___________
| o     o |
|    7    |
|__-----__|
     |
     |
     |
     |
     |
"""
    h2=r"""
___________
| o     o |
|    7    |
|__-----__|
     |
    /|
   / |
  /  |
     |
"""
    h3=r"""
___________
| o     o |
|    7    |
|__-----__|
     |
    /|\
   / | \
  /  |  \
     |
"""
    h4=r"""
___________
| o     o |
|    7    |
|__-----__|
     |
    /|\
   / | \
  /  |  \
     |
    / 
   /
  /
"""
    h5=r"""
___________
| o     o |
|    7    |
|__-----__|
     |
    /|\
   / | \
  /  |  \
     |
    / \
   /   \
  /     \
"""
    h=[h0,h1,h2,h3,h4,h5]
    s=["apple","banana","cherry","dragon","grape","guava","jack","mango","muskmelon","orange","pineapple","strawberry","watermelon"]
    import random
    a=random.choice(s)
    l=len(a)
    d=[]
    n=-1
    b="_ "*l
    print(b)
    for i in range(20):
        c=input("enter a small letter: ").lower()
        e=""
        if c in d:
            print("YOU HAVE ALREADY GUESSED THAT LETTER")
            continue
        else:
            if c in a:
                d.append(c)
                for x in a:
                    if x in d:
                        e=e+x+" "
                        if e.replace(" ","")==a:
                            print(f"YOU HAVE GUESSED THE CORRECT ONE. {a}")
                            return "YOU WON!"
                            break
                        else:
                            continue
                    else:
                        e=e+"_ "
                print(f"word: {e}")
            else:
                print("you have guessed the wrong one.")
                n=n+1
                if n==5:
                    print(h[n])
                    print("YOU HAVE LOST THE GAME.")
                    print(f"the correct one was {a}.")
                    break
                else:
                    print(h[n])
                    print(f"you have still {5-n} chances.")
print(hangman_game(y))


        

            
            


