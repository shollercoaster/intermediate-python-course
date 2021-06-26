import random
def main():
    sums=0
    dice_rolls= int(input("Number of dice rolls:"))
    for i in range (0, dice_rolls):
        roll= random.randint(1,6)
        print(f'You rolled a die: {roll}')
        if roll==1:
            print("Critical fail!")
        elif roll==6:
            print("Critical success!")
        else:
            pass

        sums+=roll
    print(f"sum of dice rolls: {sums}")
    


if __name__== "__main__":
  main()