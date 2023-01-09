# Necessary imports for pseudo-randomness, and User Interface creation
import random
import tkinter
import tkinter as tk

# Functions

# L represents the 6 possible dice values
L = [1, 2, 3, 4, 5, 6]


# Binomial coefficient formula
def binomcoef(n, k):
    if 0 <= k <= n:
        a = 1
        b = 1
        for t in range(1, min(k, n - k) + 1):
            a *= n
            b *= t
            n -= 1
        return a // b
    else:
        return 0


# Event function
def chanceev(n, k):
    return (binomcoef(n, k)) * ((1 / 6) ** k) * ((5 / 6) ** (n - k))


# Function for pressing the "Enter" button
def enter_data():
    data_one = dice_one.get()
    data_two = dice_two.get()
    data_three = dice_three.get()
    data_four = dice_four.get()
    data_five = dice_five.get()
    R = [data_one, data_two, data_three, data_four, data_five]

    # counts values from extracted data
    amountone = R.count("1")
    amounttwo = R.count("2")
    amountthree = R.count("3")
    amountfour = R.count("4")
    amountfive = R.count("5")
    amountsix = R.count("6")

    # adds up all specific events into their sums
    sublist = []
    k = 1
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALone = sum(sublist)

    sublist = []
    k = 2
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALtwo = sum(sublist)

    sublist = []
    k = 3
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALthree = sum(sublist)

    sublist = []
    k = 4
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALfour = sum(sublist)

    sublist = []
    k = 5
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALfive = sum(sublist)

    sublist = []
    k = 6
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALsix = sum(sublist)

    sublist = []
    k = 7
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALseven = sum(sublist)

    sublist = []
    k = 8
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALeight = sum(sublist)

    sublist = []
    k = 9
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALnine = sum(sublist)

    sublist = []
    k = 10
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALten = sum(sublist)

    sublist = []
    k = 11
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALeleven = sum(sublist)

    sublist = []
    k = 12
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALtwelve = sum(sublist)

    sublist = []
    k = 13
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALthirteen = sum(sublist)

    sublist = []
    k = 14
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALfourteen = sum(sublist)

    sublist = []
    k = 15
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALfifteen = sum(sublist)

    # function responsible for printing the correct values
    def countingblock(amount, dicenum):
        if amount == 0:
            print("one", dicenum, ":", ALone)
        if amount >= 1:
            print("one", dicenum, ":", 1)

        if amount == 0:
            print("two", dicenum, "'s:", ALtwo)
        if amount == 1:
            print("two", dicenum, "'s:", ALone)
        if amount >= 2:
            print("two", dicenum, "'s:", 1)

        if amount == 0:
            print("three", dicenum, "'s:", ALthree)
        if amount == 1:
            print("three", dicenum, "'s:", ALtwo)
        if amount == 2:
            print("three", dicenum, "'s:", ALone)
        if amount >= 3:
            print("three", dicenum, "'s:", 1)

        if amount == 0:
            print("four", dicenum, "'s:", ALfour)
        if amount == 1:
            print("four", dicenum, "'s:", ALthree)
        if amount == 2:
            print("four", dicenum, "'s:", ALtwo)
        if amount == 3:
            print("four", dicenum, "'s:", ALone)
        if amount >= 4:
            print("four", dicenum, "'s:", 1)

        def display1(x, a, b, c, d, e, f):
            if amount == 0:
                print(x, dicenum, "'s:", f)
            if amount == 1:
                print(x, dicenum, "'s:", e)
            if amount == 2:
                print(x, dicenum, "'s:", d)
            if amount == 3:
                print(x, dicenum, "'s:", c)
            if amount == 4:
                print(x, dicenum, "'s:", b)
            if amount >= 5:
                print(x, dicenum, "'s:", a)

        display1("five", 1, ALone, ALtwo, ALthree, ALfour, ALfive)
        display1("six", ALone, ALtwo, ALthree, ALfour, ALfive, ALsix)
        display1("seven", ALtwo, ALthree, ALfour, ALfive, ALsix, ALseven)
        display1("eight", ALthree, ALfour, ALfive, ALsix, ALseven, ALeight)
        display1("nine", ALfour, ALfive, ALsix, ALseven, ALeight, ALnine)
        display1("ten", ALfive, ALsix, ALseven, ALeight, ALnine, ALten)
        display1("eleven", ALsix, ALseven, ALeight, ALnine, ALten, ALeleven)
        display1("twelve", ALseven, ALeight, ALnine, ALten, ALeleven, ALtwelve)
        display1("thirteen", ALeight, ALnine, ALten, ALeleven, ALtwelve, ALthirteen)
        display1("fourteen", ALnine, ALten, ALeleven, ALtwelve, ALthirteen, ALfourteen)
        display1("fifteen", ALten, ALeleven, ALtwelve, ALthirteen, ALfourteen, ALfifteen)
        display1("sixteen", ALeleven, ALtwelve, ALthirteen, ALfourteen, ALfifteen, 0)
        display1("seventeen", ALtwelve, ALthirteen, ALfourteen, ALfifteen, 0, 0)
        display1("eighteen", ALthirteen, ALfourteen, ALfifteen, 0, 0, 0)
        display1("nineteen", ALfourteen, ALfifteen, 0, 0, 0, 0)
        display1("twenty", ALfifteen, 0, 0, 0, 0, 0)

    # dice roll display
    rstr = str(R)
    display = tkinter.Label(your_dice, text=rstr)
    display.grid(row=2, column=2)

    # adds titles and spaces
    def printsol(amount, dicenum):
        print("======= Chance of rolling", dicenum, "'s =======")
        countingblock(amount, dicenum)
        print("")

    printsol(amountone, 1)
    printsol(amounttwo, 2)
    printsol(amountthree, 3)
    printsol(amountfour, 4)
    printsol(amountfive, 5)
    printsol(amountsix, 6)


# function responsible for the "Randomize" button (very similar to the "Enter" button function)
def random_data():
    E = [random.choice(L), random.choice(L), random.choice(L), random.choice(L), random.choice(L)]

    amountone = E.count(1)
    amounttwo = E.count(2)
    amountthree = E.count(3)
    amountfour = E.count(4)
    amountfive = E.count(5)
    amountsix = E.count(6)

    sublist = []
    k = 1
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALone = sum(sublist)

    sublist = []
    k = 2
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALtwo = sum(sublist)

    sublist = []
    k = 3
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALthree = sum(sublist)

    sublist = []
    k = 4
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALfour = sum(sublist)

    sublist = []
    k = 5
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALfive = sum(sublist)

    sublist = []
    k = 6
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALsix = sum(sublist)

    sublist = []
    k = 7
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALseven = sum(sublist)

    sublist = []
    k = 8
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALeight = sum(sublist)

    sublist = []
    k = 9
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALnine = sum(sublist)

    sublist = []
    k = 10
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALten = sum(sublist)

    sublist = []
    k = 11
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALeleven = sum(sublist)

    sublist = []
    k = 12
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALtwelve = sum(sublist)

    sublist = []
    k = 13
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALthirteen = sum(sublist)

    sublist = []
    k = 14
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALfourteen = sum(sublist)

    sublist = []
    k = 15
    while k < 15:
        sublist.append(chanceev(15, k))
        k += 1

    ALfifteen = sum(sublist)

    def countingblock(amount, dicenum):
        if amount == 0:
            print("one", dicenum, ":", ALone)
        if amount >= 1:
            print("one", dicenum, ":", 1)

        if amount == 0:
            print("two", dicenum, "'s:", ALtwo)
        if amount == 1:
            print("two", dicenum, "'s:", ALone)
        if amount >= 2:
            print("two", dicenum, "'s:", 1)

        if amount == 0:
            print("three", dicenum, "'s:", ALthree)
        if amount == 1:
            print("three", dicenum, "'s:", ALtwo)
        if amount == 2:
            print("three", dicenum, "'s:", ALone)
        if amount >= 3:
            print("three", dicenum, "'s:", 1)

        if amount == 0:
            print("four", dicenum, "'s:", ALfour)
        if amount == 1:
            print("four", dicenum, "'s:", ALthree)
        if amount == 2:
            print("four", dicenum, "'s:", ALtwo)
        if amount == 3:
            print("four", dicenum, "'s:", ALone)
        if amount >= 4:
            print("four", dicenum, "'s:", 1)

        def display1(x, a, b, c, d, e, f):
            if amount == 0:
                print(x, dicenum, "'s:", f)
            if amount == 1:
                print(x, dicenum, "'s:", e)
            if amount == 2:
                print(x, dicenum, "'s:", d)
            if amount == 3:
                print(x, dicenum, "'s:", c)
            if amount == 4:
                print(x, dicenum, "'s:", b)
            if amount >= 5:
                print(x, dicenum, "'s:", a)

        display1("five", 1, ALone, ALtwo, ALthree, ALfour, ALfive)
        display1("six", ALone, ALtwo, ALthree, ALfour, ALfive, ALsix)
        display1("seven", ALtwo, ALthree, ALfour, ALfive, ALsix, ALseven)
        display1("eight", ALthree, ALfour, ALfive, ALsix, ALseven, ALeight)
        display1("nine", ALfour, ALfive, ALsix, ALseven, ALeight, ALnine)
        display1("ten", ALfive, ALsix, ALseven, ALeight, ALnine, ALten)
        display1("eleven", ALsix, ALseven, ALeight, ALnine, ALten, ALeleven)
        display1("twelve", ALseven, ALeight, ALnine, ALten, ALeleven, ALtwelve)
        display1("thirteen", ALeight, ALnine, ALten, ALeleven, ALtwelve, ALthirteen)
        display1("fourteen", ALnine, ALten, ALeleven, ALtwelve, ALthirteen, ALfourteen)
        display1("fifteen", ALten, ALeleven, ALtwelve, ALthirteen, ALfourteen, ALfifteen)
        display1("sixteen", ALeleven, ALtwelve, ALthirteen, ALfourteen, ALfifteen, 0)
        display1("seventeen", ALtwelve, ALthirteen, ALfourteen, ALfifteen, 0, 0)
        display1("eighteen", ALthirteen, ALfourteen, ALfifteen, 0, 0, 0)
        display1("nineteen", ALfourteen, ALfifteen, 0, 0, 0, 0)
        display1("twenty", ALfifteen, 0, 0, 0, 0, 0)

    # Dice Roll Display
    estr = str(E)
    display = tkinter.Label(your_dice, text=estr)
    display.grid(row=2, column=2)

    def printsol(amount, dicenum):
        print("======= Chance of rolling", dicenum, "'s =======")
        countingblock(amount, dicenum)
        print("")

    printsol(amountone, 1)
    printsol(amounttwo, 2)
    printsol(amountthree, 3)
    printsol(amountfour, 4)
    printsol(amountfive, 5)
    printsol(amountsix, 6)


# GUI Design beginning
window = tk.Tk()
window.title("Liar's Dice Calculator")

frame = tkinter.Frame(window)
frame.pack()

# Intro row
intro_box = tkinter.LabelFrame(frame, foreground="#582ad8", text="Probability Calculator")
intro_box.grid(row=0, column=0)

intro = tkinter.Label(intro_box, text="Please enter your preferred dice values, to calculate"
                                      " ideal bets below.")
intro.grid(row=0, column=0)
intro2 = tkinter.Label(intro_box, text="Or press the Randomize button to generate random dice values.")
intro2.grid(row=1, column=0)

# Your Dice row
your_dice = tkinter.LabelFrame(frame, foreground="#582ad8", text="Your dice roll")
your_dice.grid(row=1, column=0, padx=10, pady=10)

dice_one_label = tkinter.Label(your_dice, text="Dice 1")
dice_one = tkinter.Spinbox(your_dice, from_=1, to=6)
dice_one_label.grid(row=0, column=0)
dice_one.grid(row=1, column=0)

dice_two_label = tkinter.Label(your_dice, text="Dice 2")
dice_two = tkinter.Spinbox(your_dice, from_=1, to=6)
dice_two_label.grid(row=0, column=1)
dice_two.grid(row=1, column=1)

dice_three_label = tkinter.Label(your_dice, text="Dice 3")
dice_three = tkinter.Spinbox(your_dice, from_=1, to=6)
dice_three_label.grid(row=0, column=2)
dice_three.grid(row=1, column=2)

dice_four_label = tkinter.Label(your_dice, text="Dice 4")
dice_four = tkinter.Spinbox(your_dice, from_=1, to=6)
dice_four_label.grid(row=0, column=3)
dice_four.grid(row=1, column=3)

dice_five_label = tkinter.Label(your_dice, text="Dice 5")
dice_five = tkinter.Spinbox(your_dice, from_=1, to=6)
dice_five_label.grid(row=0, column=4)
dice_five.grid(row=1, column=4)

for widget in your_dice.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# buttons
buttons = tkinter.LabelFrame(frame)
buttons.grid(row=2, column=0, pady=10)

enter = tk.Button(buttons, foreground="#582ad8", text="Enter", command=lambda: enter_data())
enter.grid(row=0, column=0)

random_values = tk.Button(buttons, foreground="#582ad8", text="Randomize", command=lambda: random_data())
random_values.grid(row=0, column=1)

# GUI design end
window.mainloop()
