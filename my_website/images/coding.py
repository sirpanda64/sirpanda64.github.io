def play ():
    print "You wake up from a bad dream"
    choice = raw_input("Go to the bathroom? yes/no")
    while choice != 'yes' and choice !='no':
        choice = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice == "yes":
        print "You do your business and leave the bathroom."
    elif choice == "no":
        print "You pee your self. Game Over"
        return
    choice2 = raw_input("Where will you go next? bathroom/kitchen")
    while choice2 != 'bathroom' and choice2 !='kitchen':
        choice2 = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice2 == "bathroom":
        print "You already went to the bathroom so you walk to the kitchen"
    elif choice2 == "kitchen":
        print "You go to the kitchen"
    choice3 = raw_input("Eat breakfast or go outside? breakfast/outside")
    while choice3 != 'breakfast' and choice3 !='outside':
        choice3 = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice3 == "breakfast":
        print "you eat breakfast and walk outside. It's freezing"
    elif choice3 == "outside":
        print "You go outside. It's freezing"
    choice4 = raw_input("Continue? yes/no")
    while choice4 != 'yes' and choice4 !='no':
        choice4 = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice4 == "yes":
        print "You step on the cold snow and you realize you forgot your shoes"
    elif choice4 == "no":
        print "You go back to bed. Game Over"
        return
    choice5 = raw_input("Continue? yes/no")
    while choice5 != 'yes' and choice5 !='no':
        choice5 = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice5 == "yes":
        print "You step forward and step on a poop. You realize you have not picked up the poops since spring so its a giant mind field of poop."
    elif choice5 == "no":
        print "You head back home but slip. Game Over"
        return
    choice6 = raw_input("Continue? yes/no")
    while choice6 != 'yes' and choice6 !='no':
        choice6 = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice6 == "yes":
        print "You made it past your lawn and your chihuahua barks at you. you pick up your chihuahua. (Chihuahua added to your pokedex.)"
    elif choice6 == "no":
        print "you go home and go to bed. Game Over"
        return
    choice7 = raw_input("You take a step forward and encounter a wild pidgey. You send out your Chihuahua. Fight or Run? fight/run")
    while choice7 != 'run' and choice7 !='fight':
        choice7 = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice7 == "fight":
        print "Your chihuahua sratches. Your attack missed. Pidgey used gust. Your Chihuahua fainted. You black out. Game Over"
        return
    elif choice7 == "run":
        print "you run over the pidgey. Pidgey fainted. Gained 124 xp."
    choice8 = raw_input("Continue? yes/no")
    while choice8 != 'yes' and choice8 !='no':
        choice8 = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice8 == "yes":
        print "You walk to the next town"
    elif choice8 == "no":
        print "You go back to bed. Game Over"
        return
    choice9 = raw_input("Go to the Gym or the Pokemon Center? gym/pokemoncenter")
    while choice9 != 'gym' and choice9 !='pokemoncenter':
        choice9 = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice9 == "gym":
        print "You walk into Inshape and start working out. The dumbbells are to heavy. You black out."
        return
    elif choice9 == "pokemoncenter":
        print "You go to the front desk. The Nurse ask \'How are you out of your bed?!\' You are confused. Nurse says \'You have been in a coma for three months!\' You are still confused. Everything goes black. You wake up in the hospital after being in a coma for three months. Your family is there happy you finally woke up. You win."
    choice10 = raw_input("The End? yes/no")
    while choice10 != 'yes' and choice10 !='no':
        choice10 = raw_input('Answer correctly! You uncultured, uneducated swine!')
    if choice10 == "yes":
        print "you right."
    elif choice10 == "no":
        print " you wrong. Go away!"