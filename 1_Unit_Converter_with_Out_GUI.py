while True:

    # =================================================================================    
    # =================================================================================      
    # ==================================Jokes-Section====================================
    # =================================================================================    
    # =================================================================================    

    import random

    length = [
    "Bro, you just stretched those units farther than my patience.",
    "Converted length? Now go stretch your legs, you’ve been sitting too long.",
    "Bro’s measuring game is stronger than my WiFi signal.",
    "That’s longer than the line at Taco Bell on a Friday night.",
    "You just made meters jealous of centimeters, bro.",
    ]

    mass = [
    "You converted mass like you’re bench-pressing math problems.",
    "Bro, that conversion’s heavier than my Sunday regrets.",
    "Mass to mega mass? You just leveled up to ‘Hulk Mode.’",
    "You just turned grams into gains, bro. Flex those numbers!",
    "Bro’s so heavy on conversions, he’s practically a black hole."
    ]

    time = [
    "You just converted time faster than my excuses for skipping gym.",
    "Bro, time’s ticking and so is your conversion skill.",
    "That took less time than me deciding what to eat.",
    "You just made seconds jealous of minutes, bro.",
    "You converted time better than I convert bad vibes to good."
    ]

    temperature = [
    "You just turned up the heat and froze the haters.",
    "Bro, your conversions are fire — literally and figuratively.",
    "That temperature conversion? Cooler than my ex’s heart.",
    "Bro’s Celsius to Fahrenheit skills are hotter than summer.",
    "You just made Kelvin look basic, bro."
    ]

    current = [
    "Bro, you just powered up like an electric superhero.",
    "Your conversion is so lit, even Tesla’s texting you.",
    "You’ve got more amps than my party playlist.",
    "Bro just shocked the system — no outlet needed.",
    "That conversion’s got more juice than my morning coffee."
    ]

    currency = [
    "Bro just made it rain… numbers, that is.",
    "You converted cash like you’re the CEO of the digital bank.",
    "Bro’s currency game is so strong, even Scrooge McDuck is jealous.",
    "That conversion’s more profitable than my fantasy football team.",
    "You just leveled up to ‘Currency Conqueror.’"
    ]






    # =================================================================================    
    # =================================================================================      
    # ==================================Jokes-Section====================================
    # =================================================================================    
    # =================================================================================    











    print("==========================WELCOME TO UNIT CONVERTER==========================")
    print("======Which Unit you want to convert?======")
    print("1.Length")
    print("2.Mass")
    print("3.Time")
    print("4.Temperature")
    print("5.Current")
    print("6.Currency")
    print("7.Exit")


    main_unit = int(input("Which one 1/2/3/4/5/6 : "))

    # ================================================================================
    # ==================================Length-Start==================================
    # ================================================================================

    if main_unit==1:
     while True:
        print("=====Which One Standerd=====")
        print("1.CentiMeter(cm) to Meter(m)")
        print("2.Meter(m) to KiloMeter(km)")
        print("3.KiloMeter(km) to MegaMeter(Mm)")
        print("4.MegaMeter(Mm) to GigaMeter(Gm)")
        print("5.Exit")

    # ==================================Sub-Units==================================
        sub_unit = int(input("Which one 1/2/3/4/5 : "))


        if sub_unit==1:
            cm = float(input("Enter the CentiMeter(cm) :"))
            m = cm / 100
            print(f"This is the {cm}cm to : {m}m") 

        elif sub_unit==2:
            m = float(input("Enter the Meter(m) :"))
            km = m / 1000
            print(f"This is the {m}m to : {km}km")

        elif sub_unit==3:
            km = float(input("Enter the KiloMeter(km) :"))
            Mm = km / 1000
            print(f"This is the {km}km to : {Mm}Mm")

        elif sub_unit==4:
            Mm = float(input("Enter the MegaMeter(Mm) :"))
            Gm = Mm / 1000
            print(f"This is the {Mm}Mm to : {Gm}Gm")

        elif sub_unit==5:
            print(random.choice(length))
            break

        else:
            print("Enter the Valid Digit")    
    # ==============================================================================        
    # ==================================Length-End==================================
    # ==============================================================================






    # ==============================================================================
    # ==================================Mass-Start==================================
    # ==============================================================================
    elif main_unit==2:
     while True:
        print("=====Which One Standerd=====")
        print("1.MilliGram(mg) to Gram(g)")
        print("2.Gram(g) to KiloGram(kg)")
        print("3.KiloGram(kg) to Tonne(t)")
        print("4.Tonne(t) to MegaTonne(Mt)")
        print("5.Exit")
        
    # ==================================Sub-Units==================================
        sub_unit = int(input("Which one 1/2/3/4/5 : "))


        if sub_unit==1:
            mg = float(input("Enter the MilliGram(mg) :"))
            g = mg / 1000
            print(f"This is the {mg}mg to : {g}g") 

        elif sub_unit==2:
            g = float(input("Enter the Gram(g) :"))
            kg = g / 1000
            print(f"This is the {g}g to : {kg}kg")

        elif sub_unit==3:
            kg = float(input("Enter the KiloGram(kg) :"))
            t = kg / 1000
            print(f"This is the {kg}kg to : {t}t")

        elif sub_unit==4:
            t = float(input("Enter the Tonne(t) :"))
            Mt = t / 1000000
            print(f"This is the {t}t to : {Mt}Mt")

        elif sub_unit==5:
            print(random.choice(mass))
            break

        else:
            print("Enter the Valid Digit")    
    # ==============================================================================        
    # ==================================Mass-End====================================
    # ==============================================================================






    # ==============================================================================
    # ==================================Time-Start==================================
    # ==============================================================================
    elif main_unit==3:
     while True:
        print("=====Which One Standerd=====")
        print("1.MilliSecond(ms) to Second(s)")
        print("2.Second(s) to Minutes(min)")
        print("3.Minutes(min) to Hour(h)")
        print("4.Hour(h) to Day(d)")
        print("5.Exit")
        
    # ==================================Sub-Units==================================
        sub_unit = int(input("Which one 1/2/3/4/5 : "))


        if sub_unit==1:
            ms = float(input("Enter the MilliSecond(ms) :"))
            s = ms / 1000
            print(f"This is the {ms}ms to : {s}s") 

        elif sub_unit==2:
            s = float(input("Enter the Second(s) :"))
            min = s / 60
            print(f"This is the {s}s to : {min}min")

        elif sub_unit==3:
            min = float(input("Enter the Minute(min) :"))
            h = min / 60
            print(f"This is the {min}min to : {h}h")

        elif sub_unit==4:
            h = float(input("Enter the Hour(h) :"))
            d = h / 24
            print(f"This is the {h}h to : {d}d")

        elif sub_unit==5:
            print(random.choice(time))
            break

        else:
            print("Enter the Valid Digit")    
    # ==============================================================================        
    # ==================================Time-End====================================
    # ==============================================================================






    # =====================================================================================
    # ==================================Temperature-Start==================================
    # =====================================================================================
    elif main_unit==4:
      while True:
        print("=====Which One Standerd=====")
        print("1.Celsius(°C) to Fahrenheit(°F)")
        print("2.Fahrenheit(°F) to Kelvin(K)")
        print("3.Kelvin(K) to Celsius(°C)")
        print("4.Fahrenheit(°F) to Celsius(°C)")
        print("5.Exit")
        
    # ==================================Sub-Units==================================
        sub_unit = int(input("Which one 1/2/3/4/5 : "))


        if sub_unit==1:
            c = float(input("Enter the Celsius(°C) :"))
            f = (c * 9/5) + 32
            print(f"This is the {c}°C to : {f}°F") 

        elif sub_unit==2:
            f = float(input("Enter the Fahrenheit(°F) :"))
            k = (f - 32) * 5/9 + 273.15
            print(f"This is the {f}°F to : {k}k")

        elif sub_unit==3:
            k = float(input("Enter the Kelvin(K) :"))
            c = k - 273.15
            print(f"This is the {k}k to : {c}°C")

        elif sub_unit==4:
            f = float(input("Enter the Fahrenheit(°F) :"))
            c = (f - 32) * 5/9
            print(f"This is the {f}°F to : {c}°C")

        elif sub_unit==5:
            print(random.choice(temperature))
            break

        else:
            print("Enter the Valid Digit")    
    # =====================================================================================       
    # ==================================Temperature-End====================================
    # =====================================================================================





    # =================================================================================
    # ==================================Current-Start==================================
    # =================================================================================
    elif main_unit==5:
      while True:  
        print("=====Which One Standerd=====")
        print("1.Milliampere(mA) to Ampere(A) ")
        print("2.Ampere(A) to KiloAmpere(kA)")
        print("3.KiloAmpere(kA) to MegaAmpere(MA)")
        print("4.MegaAmpere(MA) to GigaAmpere(GA)")
        print("5.Exit")
        
    # ==================================Sub-Units======================================
        sub_unit = int(input("Which one 1/2/3/4/5 : "))


        if sub_unit==1:
            mA = float(input("Enter the Milliampere(mA) :"))
            A =  mA / 1000
            print(f"This is the {mA}mA to : {A}A") 

        elif sub_unit==2:
            A = float(input("Enter the Ampere(A) :"))
            kA =  A / 1000
            print(f"This is the {A}A to : {kA}kA")

        elif sub_unit==3:
            kA = float(input("Enter the KiloAmpere(KA) :"))
            MA = kA / 1000
            print(f"This is the {kA}kA to : {MA}MA")

        elif sub_unit==4:
            MA = float(input("Enter the MegaAmpere(MA) :"))
            GA = MA / 1000
            print(f"This is the {MA}MA to : {GA}GA")

        elif sub_unit==5:
            print(random.choice(current))
            break

        else:
            print("Enter the Valid Digit")    
    # =================================================================================      
    # ==================================Current-End====================================
    # =================================================================================





    # =================================================================================
    # ==================================Currency-Start==================================
    # =================================================================================
    elif main_unit==6:
      while True:  
        print("=====Which One Standerd=====")
        print("1.USD to PKR")
        print("2.SAR to PKR")
        print("3.INR to PKR")
        print("4.KWD to PKR")
        print("5.AFN to PKR")
        print("6.Exit")
        
    # ==================================Sub-Units======================================
        sub_unit = int(input("Which one 1/2/3/4/5 : "))


        if sub_unit==1:
            USD = float(input("Enter the USD :"))
            PKR =  USD * 281.55
            print(f"This is the ${USD} to : Rs.{PKR}") 

        elif sub_unit==2:
            SAR = float(input("Enter the SAR :"))
            PKR =  SAR * 75.05
            print(f"This is the {SAR}SR to : Rs.{PKR}")

        elif sub_unit==3:
            INR = float(input("Enter the INR :"))
            PKR = INR * 3.19
            print(f"This is the ₹{INR} to : Rs.{PKR}")

        elif sub_unit==4:
            KWD = float(input("Enter the KWD :"))
            PKR = KWD * 922.12
            print(f"This is the {KWD}د.ك to : Rs.{PKR}")

        elif sub_unit==5:
            AFN = float(input("Enter the AFN :"))
            PKR = AFN * 4.08
            print(f"This is the {AFN}؋ to : Rs.{PKR}")

        elif sub_unit==6:
            print(random.choice(currency))
            break

        else:
            print("Enter the Valid Digit")    
    # =================================================================================      
    # ==================================Currency-End====================================
    # =================================================================================


    elif main_unit==7:
        print("جزاک اللہ")
        print("Unit Converter signing off... May your measurements always be accurate!")
        break

    else:
        print("Enter the correct Digit")    
        




