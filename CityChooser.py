#imported module for later in the program
from tkinter import*
#ideal city lists that should be compared to 
Bangkok = ['HISTORIC', 'SHOPPING', 'NIGHTLIFE', 'TRANSPORT']
Budapest = ['CHEAP', 'HISTORIC', 'FOOD', 'HEALTH']
London = ['HISTORIC', 'SHOPPING', 'NIGHTLIFE', 'CULTURE', 'HEALTH']
Vienna = ['FOOD', 'HISTORIC', 'TRANSPORT', 'CULTURE', 'HEALTH']
Paris = ['FOOD', 'HISTORIC', 'SHOPPING', 'NIGHTLIFE']
Prague = ['HISTORIC', 'CHEAP', 'CULTURE', 'FAMILY', 'FOOD']
Dubai = ['SHOPPING', 'HEALTH', 'NIGHTLIFE', 'FOOD']
Singapore = ['HEALTH', 'SHOPPING', 'FOOD', 'NIGHTLIFE']
Tokyo = ['SHOPPING', 'FOOD', 'CULTURE', 'FAMILY', 'HISTORIC']
Seoul = ['CULTURE', 'FOOD', 'HISTORIC', 'NIGHTLIFE']
New_York = ['SHOPPING', 'HISTORIC', 'CULTURE', 'NIGHTLIFE']
Kuala_Lumpur = ['NIGHTLIFE', 'CHEAP', 'TRANSPORT', 'SHOPPING', 'FOOD']
Hong_Kong = ['CULTURE', 'SHOPPING', 'FOOD', 'NIGHTLIFE']
Istanbul = ['CULTURE', 'SHOPPING', 'HISTORIC', 'NIGHTLIFE']
Barcelona = ['HISTORIC', 'FOOD', 'CULTURE', 'NIGHTLIFE']
Amsterdam = ['HISTORIC', 'CULTURE', 'NIGHTLIFE', 'FOOD']
Milan = ['FOOD', 'SHOPPING', 'CULTURE', 'NIGHTLIFE']
Osaka = ['FOOD', 'CULTURE', 'SHOPPING', 'HISTORIC']
Moscow = ['HISTORIC', 'NIGHTLIFE', 'HEALTH', 'CULTURE']
Johannesburg = ['HEALTH', 'SHOPPING', 'HISTORIC', 'NIGHTLIFE']
print("This is a holiday comparison code which will choose a holiday destination city around the world based on either an input description or a list of set choices")
#function to restart the program when an unexpected input is put in 
def Restart():
    #input deciding wether the user wants to use a description or menu choices
    Choice = input("do you wish to write a description or choose from a list of set choices (Please write the word 'description' or the word 'choices' to get started)")
    #descriptions section of the program
    if Choice == "description" or Choice.title() == ("Description"):
        #empty array to place the order of the attributes that the user inputs
        Order=[]
        #empty array to decide what regions to input in the region selection process
        Regions=[]
        #input of the compared description
        Description = input("Please write a description of your perfect holiday destination this may be as long or short as needed longer descriptions will turn out more accurate in the end")
        #the user description split into a list to take out all attibutes the user doesnt want
        Des = Description.split()
        #attributes with the list of words being picked up on by the program
        Historic = ("history" , "sightseeing" , "old" , "ancient" ,  "past" , "tour" , "historic" , "historical" , "landmark")
        Shopping = ("retail" , "shopping" , "expendature" , "gift" , "merchandise" , "purchase" , "market" , "presents" , "shop" , "shops" )
        Nightlife = ("nightlife" , "clubs" , "clubbing" , "party" , "rave" , "dj" , "music" , "club" , "bar" , "bars" , "pub" , "drink" , "drinking","drinks")
        Transport = ("manoeuvre" , "move" , "travel" , "transport" , "bus" , "train" , "tram" , "plane" , "airport" , "station" , "coach" , "bike" , "bicycle" , "boat" , "ship" , "ferry" , "horse" , "donkey" , "metro" , "elephant")
        Cheap = ("cheap" , "budget" , "inexpensive" , "value" , "price" , "economical" , "affordable" , "sale" , "bargin" , "economy")
        Food = ("dining" , "cuisine" , "eat" , "food" , "meat" , "fish" , "taste" , "menu")
        Culture = ("cuture" , "people" , "religion" , "social" , "ethnic" , "custom" , "society")
        Health = ("health" , "recreation" , "life" , "environment" ,"football", "sport" , "park" , "cycling" , "walking" , "walk" , "leisure" , "beach" , "animal" , "wildlife" , "nature" , "plants" , "plant" , "animals")
        Family = ("family" , "child" , "kid" , "park" , "roller" , "friendly" , "young" )
        #regions with list of words to pick up on the certain regions
        Europe = ("Europe", "European", "europe")
        Africa = ("African", "Africa", "africa")
        North_America = ("America", "america", "Usa", "United States")
        Asia = ("Asian", "Asia", "asian", "asia")
        #List of negative words to decided weather an atribute or region should be removed from the description
        Not = ("no", "not in", "dont", "not", "Not", "don't")
        #For the length of the description list
        for at in range(len(Des)):
            #for the length of the negative words list
            for au in range(len(Not)):
                #if the current negative word is in the current position in the descriptions list
                if Not[au] in Des:
                    #set these values to 0 (this is just to set them to 0 initially)
                    if at == 0:
                        bi = 0
                        bj = 0
                        bk = 0
                        bl = 0
                        bm = 0
                        bn = 0
                        bo = 0
                        bp = 0
                        bq = 0
                        br = 0
                        bs = 0
                        bt = 0
                        bu = 0
                    #if a attribute has already been picked up on within the next 5 words after the negative word set the values to 0
                    if Not[au] == Des[at]:
                        bi = 0
                        bj = 0
                        bk = 0
                        bl = 0
                        bm = 0
                        bn = 0
                        bo = 0
                        bp = 0
                        bq = 0
                        br = 0
                        bs = 0
                        bt = 0
                        bu = 0
                    #give the index of the negative word picked up on   
                    num = Des.index(Not[au])
                    #count how many of that negative word there are in the description 
                    Count = Des.count(Not[au])
                    #if there are 5 remaining words do this
                    if len(Des)-num >= 6:
                        #create a list of the next 5 words
                        NextFew = [Des[num+1],Des[num+2],Des[num+3],Des[num+4],Des[num+5]]
                    #if there are 4 do this
                    elif len(Des)-num >= 5:
                        NextFew = [Des[num+1],Des[num+2],Des[num+3],Des[num+4]]
                    #3 do this
                    elif len(Des)-num >= 4:
                        NextFew = [Des[num+1],Des[num+2],Des[num+3]]
                    #2 do this
                    elif len(Des)-num >= 3:
                        NextFew = [Des[num+1],Des[num+2]]
                    #1 do this
                    elif len(Des)-num >= 2:
                        NextFew = [Des[num+1]]
                    #no more then exit the loop
                    else:
                        break
                    #for the length of the historic aspect keyword list
                    for av in range(len(Historic)):
                        Historic[av]
                        # and if the value of the variable is 0 
                        if bi == 0:
                            if Historic[av] in NextFew:
                                #remove the next historic attribute
                                Des.remove(Historic[av])
                                #replace the aspect with the word word to keep the list the same size
                                Des.insert(at+1,"word")
                                #change the value of the variable to equal not 0
                                bi = bi + 1
                    #Do the same as with all other attributes as done with historic
                    for aw in range(len(Shopping)):
                        Shopping[aw]
                        if bj == 0:
                            if Shopping[aw] in NextFew:
                                Des.remove(Shopping[aw])
                                Des.insert(at+1,"word")
                                bj = bj + 1
                    for ax in range(len(Nightlife)):
                        Nightlife[ax]
                        if bk == 0: 
                            if Nightlife[ax] in NextFew:   
                                Des.remove(Nightlife[ax])
                                Des.insert(at+1,"word")
                                bk = bk + 1
                    for ay in range(len(Transport)):
                        Transport[ay]
                        if bl == 0:
                            if Transport[ay] in NextFew:
                                Des.remove(Transport[ay])
                                Des.insert(at+1,"word")
                                bl = bl + 1
                    for az in range(len(Cheap)):
                        Cheap[az]
                        if bm == 0:
                            if Cheap[az] in NextFew:
                                Des.remove(Cheap[az])
                                Des.insert(at+1,"word")
                                bk = bk + 1
                    for ba in range(len(Food)):
                        Food[ba]
                        if bn == 0:
                            if Food[ba] in NextFew:
                                Des.remove(Food[ba])
                                Des.insert(at+1,"word")
                                bn = bn + 1
                    for bb in range(len(Culture)):
                        Culture[bb]
                        if bo == 0:
                            if Culture[bb] in NextFew:
                                Des.remove(Culture[bb])
                                Des.insert(at+1,"word")
                                bo = bo + 1
                    for bc in range(len(Health)):
                        Health[bc]
                        if bp == 0:
                            if Health[bc] in NextFew:
                                Des.remove(Health[bc])
                                Des.insert(at+1,"word")
                                bp = bp + 1
                    for bd in range(len(Family)):
                        Family[bd]
                        if bq == 0:
                            if Family[bd] in NextFew:
                                Des.remove(Nightlife[bd])
                                Des.insert(at+1,"word")
                                bq = bq + 1

                    #do the same with the regions too
                    for be in range(len(Europe)):
                        Europe[be]
                        if br == 0:
                            if Europe[be] in NextFew:
                                Des.remove(Europe[be])
                                Des.insert(at+1,"word")
                                br = br + 1                            
                    for bf in range(len(Africa)):
                        Africa[bf]
                        if bs == 0:
                            if Africa[bf] in NextFew:
                                Des.remove(Africa[bf])
                                Des.insert(at+1,"word")
                                bk = bk + 1
                    for bg in range(len(North_America)):
                        North_America[bg]
                        if bt == 0:
                            if North_America[bg] in NextFew:
                                Des.remove(North_America[bg])
                                Des.insert(at+1,"word")
                                bt = bt + 1
                    for bh in range(len(Asia)):
                        Asia[bh]
                        if bu == 0:
                            if Asia[bh] in NextFew:
                                Des.remove(Asia[bh])
                                Des.insert(at+1,"word")
                                bu = bu + 1
                    #recreate the descriptions string
                    Description = " ".join(Des)
                
                    
        #for the length of the historic keywords list 
        for a in range(len(Historic)):
            Historic[a]
            #check if the keyword is in the input and the aspects arent in the array Order yet
            if Historic[a] in Description and "Historic aspects" not in Order:
                #append the attribute
                Order.append("Historic aspects")
        #Do the same for all other aspects
        for b in range(len(Shopping)):
            Shopping[b]
            if Shopping[b] in Description and "Shopping" not in Order:
                Order.append("Shopping")
        for c in range(len(Nightlife)):
            Nightlife[c]
            if Nightlife[c] in Description and "Nightlife" not in Order:
                Order.append("Nightlife")
        for d in range(len(Transport)):
            Transport[d]
            if Transport[d] in Description and "Transport" not in Order:
                Order.append("Transport")
        for e in range(len(Cheap)):
            Cheap[e]
            if Cheap[e] in Description and "Cheap" not in Order:
                Order.append("Cheap")
        for f in range(len(Food)):
            Food[f]
            if Food[f] in Description and "Food" not in Order:
                Order.append("Food")
        for g in range(len(Culture)):
            Culture[g]
            if Culture[g] in Description and "Culture" not in Order:
                Order.append("Culture")
        for h in range(len(Health)):
            Health[h]
            if Health[h] in Description and "Health and recreation" not in Order:
                Order.append("Health and recreation")
        for i in range(len(Family)):
            Family[i]
            if Family[i] in Description and "Family" not in Order:
                Order.append("Family")
        #do the same as with the attribute as with the regions subbing in the regions array instead
        for ag in range(len(Europe)):
            Europe[ag]
            if Europe[ag] in Description and "Europe" not in Regions:
                Regions.append("Europe")
                
        for ah in range(len(Africa)):
            Africa[ah]
            if Africa[ah] in Description and "Africa" not in Regions:
                Regions.append("Africa")

        for ai in range(len(North_America)):
            North_America[ai]
            if North_America[ai] in Description and "North America" not in Regions:
                Regions.append("North America")

        for aj in range(len(Asia)):
            Asia[aj]
            if Asia[aj] in Description and "Asia" not in Regions:
                Regions.append("Asia")
        #if no attributes are picked up on
        if len(Order) == 0:
            print("The program struggled to pick up on any words from your description if you could please select from the given list so we can try and work out your perfect destination")
            #add every attribute to the order list
            Order = ["Historic aspects","Shopping","Nightlife","Transport","Affordability","Food","Culture","Health and recreation","Family"]
        #make the user input the order of their attributes
        print("please now type how important these aspects are for your holiday by typing each of these items in the order from most to least important:" , Order)
        print("please input the objects one at a time (If there is a feature picked up on that you dont want included in the search please input the last feature twice)")
        #empty array of the newlist the user makes with the correct order
        NewList = []
        length = len(Order)
        Check = [] 
        for u in range (len(Order)):
            Check.append(Order[u].upper())
        #for the length of the order list
        for j in range (length):
            print("input the object you consider to be in position", j+1, "of importance")
            def again():
                Userlist = input()
                #check the value in the order table
                if Userlist.upper() not in Check:
                    print("Please put in one of the items in", Order)
                    again()
                #split the words in the input by the spaces
                Userlist = Userlist.partition(' ')[0]
                Userlist = Userlist.upper()
                #add to the new list
                NewList.append(Userlist)
            again()
        #create a blank table of the cities needed to compare with
        Cities= []
        #if european cities are selected append all european cities
        if "Europe" in Regions:
            City = [Budapest, London, Vienna, Paris, Prague, Istanbul, Barcelona, Amsterdam, Milan, Moscow]
            for AM in range(len(City)):
                Cities.append(City[AM])
        #do the same for all other regions
        if "Africa" in Regions:
            Cities.append(Johannesburg)
        if "North America" in Regions:
            Cities.append(New_York)
        if "Asia" in Regions:
            City = [Bangkok, Dubai, Singapore, Tokyo, Seoul, Kuala_Lumpur, Hong_Kong, Istanbul, Osaka]
            for AN in range(len(City)):
                Cities.append(City[AN])
        #if no regions are put in place all cities in the list
        if len(Regions) == 0:
            Cities = [Bangkok , Budapest , London , Vienna , Paris , Prague , Dubai , Singapore , Tokyo , Seoul , New_York , Kuala_Lumpur , Hong_Kong , Istanbul , Barcelona , Amsterdam , Milan , Osaka , Moscow , Johannesburg]
        #for the number of cities in the list create a scorelist with score 0
        ScoreList = [0]*len(Cities)
        #for how many cities there are on the cities list
        for k in range(len(Cities)):
            #and how many items are in the created list
            for l in range(len(NewList)):
                #for the current item in the cities list
                for m in range(len(Cities[k])):
                    #if the items in the user ideal cities list is in the cities ideal cities list compare their indexes negatively so 5 is the value of index 0 and do that for every value
                    if NewList[l] == Cities[k][m]:
                        ScoreList[k] += (len(NewList)-l+1)*(5-m+1)
        #go through  the scorelist
        IterScore = iter(ScoreList)
        #find the highest value in the scorelist
        City = max(ScoreList)
        #set the value of this variable to minus 1 so that when 1 is added it gives 0 for the first position as this is the first index
        o = -1
         
        #make the value of the options list blank
        Options = []
        #for all the items in the score list
        for n in range(0, len(ScoreList)):
            #go though each item
            NextItem = next(IterScore)
            
            o = o+1
            #if the value searched for is in the city list it will be the highest one so it get appended to
            if NextItem == City:
                
                Options.append(o)
        #turn each city into a list of strings
        StrCities = []
        #add only the amount of cities as the amount of cities in each selected region
        if "Europe" in Regions:
            StrCity = ["Budapest", "London", "Vienna", "Paris", "Prague", "Istanbul", "Barcelona", "Amsterdam", "Milan", "Moscow"]
            for AO in range(len(StrCity)):
                StrCities.append(StrCity[AO])
        if "Africa" in Regions:
            StrCities.append ("Johannesburg")
        if "North America" in Regions:
            StrCities.append("New_York")
        if "Asia" in Regions:
            StrCity = ["Bangkok", "Dubai", "Singapore", "Tokyo", "Seoul", "Kuala_Lumpur", "Hong_Kong", "Istanbul", "Osaka"]
            for AP in range(len(StrCity)):
                StrCities.append(StrCity[AP])
        #if no regions are selected add all regions
        if len(Regions) == 0:
            StrCities = ["Bangkok", "Budapest" , "London" , "Vienna" , "Paris", "Prague", "Dubai", "Singapore", "Tokyo","Seoul", "New_York" , "Kuala_Lumpur", "Hong_Kong","Istanbul","Barcelona","Amsterdam","Milan","Osaka","Milan","Johannesburg"]
        #print all the regions with the highest score
        print("The program has discovered", len(Options), "ideal destination(s) for your holiday")
        print("These are the cities we have picked up on:")
        for p in range(len(Options)):
            print(StrCities[Options[p]])
        #ask the user if they are happy witht the answers given
        def Ask():
            Result = input("Are you happy with the result? If you're not we can try and provide you with a second option if available.")
            #if they are happy exit the program
            if Result == "yes" or Result.title() == "YES":
                print("Please enjoy your holiday.")
                exit()
            #otherwise try and offer the second choice
            elif Result == "no" or Result.title() == "NO":
                
                
                print("we will offer the next option we have picked up on")
                IterScore = iter(ScoreList)
                
                #order the score list and reverse it
                City = sorted(ScoreList,key=int, reverse=True)
                #count the value of the first index to find the number of the highest score that exist
                FirstNumber = ScoreList.count(City[0])
                r= FirstNumber
                #set the new values of options to empty
                Options = []
                #if there are no more values found then tell them none exist
                if FirstNumber >= len(ScoreList):
                    print("We could not find any secondary cities. This program is a work in progress and does not contain all cities just yet.")
                    exit()
                
                for q in range(0, len(ScoreList)):
                    NextItem = next(IterScore)
                    #append all the second highest values to options
                    if NextItem == City[r]:
                        Options.append(StrCities[q])
                

                #print the options to the user and exit
                print("The program has discovered", len(Options), "ideal destination(s) for your holiday on its second run through")
                print("These are the cities we have picked up on:")
                for t in range (len (Options)):
                    print(Options[t])
                print("Please enjoy your holiday. We hope this program could be helpful.")
                exit()
                    

            else:
                print("we could not understand the given answer please say yes or no")
                Ask()
        Ask()
            

            
    elif Choice == "choices" or Choice.title() == ("Choices"):
        #create a window
        master = Tk()
        #put the window in from of all other windows on your desktop
        master.lift()
        master.attributes("-topmost",True)
        #turn the values of the tickboxes to 1 or 0 depending on yes or no answers
        EuropeVar = IntVar()
        AfricaVar = IntVar()
        North_AmericaVar = IntVar()
        AsiaVar = IntVar()
        #give the users instructions
        VTitle = Label (master, text="Please give a score from 1 to 5 stars based on \nhow important each aspect is to your holiday and we \nwill find a city perfect for you based on the outcome given.\n")
        VTitle.config(font=("Arial", 10))
        VTitle.pack()

        #create slider values for each attribute
        VHistoric = Label(master, text="Historic aspects")
        VHistoric.config(font=("Arial", 10))
        VHistoric.pack()
        #set the values of each slider interval
        SHistoric =Scale(master, from_=1, to=5, tickinterval=1, resolution = 0.5, length= 500, orient=HORIZONTAL, width=10)
        SHistoric.pack()
        
        
        VShopping = Label(master, text="Shopping")
        VShopping.config(font=("Arial", 10))
        VShopping.pack()
        
        SShopping =Scale(master, from_=1, to=5, tickinterval=1, resolution = 0.5, length= 500, orient=HORIZONTAL, width=10)
        SShopping.pack()

        VNightlife = Label(master, text="Nightlife")
        VNightlife.config(font=("Arial", 10))
        VNightlife.pack()
        
        SNightlife =Scale(master, from_=1, to=5, tickinterval=1, resolution = 0.5, length= 500, orient=HORIZONTAL, width=10)
        SNightlife.pack()
        
        VTransport = Label(master, text="Transport")
        VTransport.config(font=("Arial", 10))
        VTransport.pack()
        
        STransport =Scale(master, from_=1, to=5, tickinterval=1, resolution = 0.5, length= 500, orient=HORIZONTAL, width=10)
        STransport.pack()

        VCheap = Label(master, text="Affordability")
        VCheap.config(font=("Arial", 10))
        VCheap.pack()
        
        SCheap =Scale(master, from_=1, to=5, tickinterval=1, resolution = 0.5, length= 500, orient=HORIZONTAL, width=10)
        SCheap.pack()

        VFood = Label(master, text="Food")
        VFood.config(font=("Arial", 10))
        VFood.pack()
        
        SFood =Scale(master, from_=1, to=5, tickinterval=1, resolution = 0.5, length= 500, orient=HORIZONTAL, width=10)
        SFood.pack()

        VCulture = Label(master, text="Culture")
        VCulture.config(font=("Arial", 10))
        VCulture.pack()
        
        SCulture =Scale(master, from_=1, to=5, tickinterval=1, resolution = 0.5, length= 500, orient=HORIZONTAL, width=10)
        SCulture.pack()

        VHealth = Label(master, text="Health and recreation")
        VHealth.config(font=("Arial", 10))
        VHealth.pack()
                       
        SHealth =Scale(master, from_=1, to=5, tickinterval=1, resolution = 0.5, length= 500, orient=HORIZONTAL, width=10)
        SHealth.pack()

        VFamily = Label(master, text="Family")
        VFamily.config(font=("Arial", 10))
        VFamily.pack()
                       
        SFamily =Scale(master, from_=1, to=5, tickinterval=1, resolution = 0.5, length= 500, orient=HORIZONTAL, width=10)
        SFamily.pack()
        
        #create a frame to put the checkbuttons in
        frame = Frame(width=800, height=600,)
        #orient the check buttons
        frame.pack(side=TOP)
        #create the check buttons in the frames for each region
        AKEurope = Checkbutton(frame, text = "Europe", onvalue = 1, offvalue = 0, variable = EuropeVar)
        AKEurope.pack(side = LEFT, padx = 20)

        AKAfrica = Checkbutton(frame, text = "Africa", onvalue = 1, offvalue = 0, variable = AfricaVar)
        AKAfrica.pack(side = LEFT, padx = 20)

        AKNorth_America = Checkbutton(frame, text = "North_America", onvalue = 1, offvalue = 0, variable = North_AmericaVar)
        AKNorth_America.pack(side = LEFT, padx = 20)

        AKAsia = Checkbutton(frame, text = "Asia", onvalue = 1, offvalue = 0, variable = AsiaVar)
        AKAsia.pack(side = LEFT, padx = 20)


        #create a funtion to manipulate all the slider values
        def get():
            #obtain all the values in the menu
            WHistoric = SHistoric.get()
            WShopping = SShopping.get()
            WNightlife = SNightlife.get()
            WTransport = STransport.get()
            WCheap = SCheap.get()
            WFood = SFood.get()
            WCulture = SCulture.get()
            WHealth = SHealth.get()
            WFamily = SFamily.get()

            ALEurope = EuropeVar.get()
            ALAfrica = AfricaVar.get()
            ALNorth_America = North_AmericaVar.get()
            ALAsia = AsiaVar.get()
            #order by size each of the slider values changing the string list in the same way
            Answers = ["HISTORIC","SHOPPING","NIGHTLIFE","TRANSPORT","CHEAP","FOOD","CULTURE","HEALTH","FAMILY"]
            Options = [WHistoric, WShopping, WNightlife, WTransport, WCheap, WFood, WCulture, WHealth, WFamily]
            Solution = [Answers for _,Answers in sorted(zip(Options,Answers),reverse = True )]
            # create a list of each city depending on the regions
            Cities = []
            if ALEurope == 1:
                City = [Budapest, London, Vienna, Paris, Prague, Istanbul, Barcelona, Amsterdam, Milan, Moscow]
                for AQ in range(len(City)):
                    Cities.append(City[AQ])

            if ALAfrica == 1:
                Cities.append(Johannesburg)

            if ALNorth_America == 1:
                Cities.append(New_York)

            if ALAsia == 1:
                City = [Bangkok, Dubai, Singapore, Tokyo, Seoul, Kuala_Lumpur, Hong_Kong, Istanbul, Osaka]
                for AR in range(len(City)):
                    Cities.append(City[AR])
            #if nothing if picked up on include all the regions
            if ALEurope == 0 and ALAfrica == 0 and ALNorth_America == 0 and ALAsia == 0:
                Cities = [Bangkok , Budapest , London , Vienna , Paris , Prague , Dubai , Singapore , Tokyo , Seoul , New_York , Kuala_Lumpur , Hong_Kong , Istanbul , Barcelona , Amsterdam , Milan , Osaka , Moscow , Johannesburg]
            #create a scorelist in the same way as before
            ScoreList = [0]*len(Cities)
            for x in range(len(Cities)):
                for y in range(len(Solution)):
                    for z in range(len(Cities[x])):
                        if Solution[y] == Cities[x][z]:
                            ScoreList[x] += (len(Solution)-y+1)*(5-z+1)
            #create a list of regions that are strings
            StrCities = []
            if ALEurope == 1:
                StrCity = ["Budapest", "London", "Vienna", "Paris", "Prague", "Istanbul", "Barcelona", "Amsterdam", "Milan", "Moscow"]
                for cit in range(len(StrCity)):
                    StrCities.append(StrCity[cit])
            if ALAfrica == 1:
                StrCities.append("Johannesburg")
            if ALNorth_America == 1:
                StrCities.append("New_York")
            if ALAsia == 1:
                StrCities = ["Bangkok", "Dubai", "Singapore", "Tokyo", "Seoul", "Kuala_Lumpur", "Hong_Kong", "Istanbul", "Osaka"]
                for city in range(len(StrCity)):
                    StrCities.append(StrCity[city])
            #if nothing is picked up on inclue all of them
            if ALEurope == 0 and ALAfrica == 0 and ALNorth_America == 0 and ALAsia == 0:
                StrCities = ["Bangkok", "Budapest" , "London" , "Vienna" , "Paris", "Prague", "Dubai", "Singapore", "Tokyo","Seoul", "New_York" , "Kuala_Lumpur", "Hong_Kong","Istanbul","Barcelona","Amsterdam","Milan","Osaka","Milan","Johannesburg"]

            #find each maximum value of the score list
            IterScore = iter(ScoreList)
            City = max(ScoreList)
            ab = -1
         
            #find which cities these relate to and append this to a new list called options
            Options = []
            for aa in range(0, len(ScoreList)):
                NextItem = next(IterScore)
                ab = ab+1
                if NextItem == City:
                    Options.append(ab)
            #print each of the options obtained
            print("The program has discovered", len(Options), "ideal destination(s) for your holiday")
            print("These are the cities we have picked up on:")
            for ac in range(len(Options)):
                    print(StrCities[Options[ac]])
            #ask the user if they are happy with the results
            def Ask():
                #if yes exit the program
                Result = input("Are you happy with the result? If you're not we can try and provide you with a second option if available.") 
                if Result == "yes" or Result.title() == "YES":
                    print("Please enjoy your holiday.")
                    exit()
                #otherwise find the second highest value
                elif Result == "no" or Result.title() == "NO":
                    
                    print("we will offer the next option we have picked up on")
                    IterScore = iter(ScoreList)
                    
                    #order the scorelist and reverse the order
                    City = sorted(ScoreList,key=int, reverse=True)
                    #add the number of the first index that exist
                    FirstNumber = ScoreList.count(City[0])
                    ad = FirstNumber
                    Options = []
                    #if no second options are found tell the users why
                    if FirstNumber >= len(ScoreList):
                        print("We could not find any secondary cities. This program is a work in progress and does not contain all cities just yet.")
                        exit()
                    #otherwise append each of the second value cities
                    for ae in range(0, len(ScoreList)):
                       if ScoreList[ae] == City[ad]:
                           Options.append(StrCities[ae])
                    

                    #print the options to the user
                    print("The program has discovered", len(Options), "ideal destination(s) for your holiday on its second run through")
                    print("These are the cities we have picked up on:")
                    for af in range (len (Options)):
                        print(Options[af])
                    print("Please enjoy your holiday. We hope this code could be helpful.")
                    exit()
                        

                else:
                    print("we could not understand the given answer please say yes or no")
                    Ask()
            Ask()
            #destroy the window       
            master.destroy()
            return WHistoric, WShopping, WNightlife, WTransport, WCheap, WFood, WCulture, WHealth, WFamily


        #run the function using the button   
        button = Button(master, text="Confirm Choices", command=get)
        button.pack()
        mainloop()
    else:
        print("The choice you have input is not valid please try again")
        Restart()
Restart()
