import random
def main():
    sums=0
    dice_rolls= int(input("Number of dice rolls:"))
    for i in range (0, dice_rolls):
        roll= random.randint(1,6)
        print(f'You rolled a die: {roll}')
        sums+=roll
    print(f"sum of dice rolls: {sums}")

if __name__== "__main__":
  main()