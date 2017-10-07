quiz_ques1 = ["Paulo Coelho  is a Brazilian 1_____ and 2______.\n He was born in 3 ______ on 4______ ."] 
quiz_ques2 = ["His novel 1 ______ has been translated into 2____ languages.\nAccording to The 3_____ Post, Paulo Coelho has sold an estimated 4_____ million books."]
quiz_ques3 = ["In 1______ in the year 2_____, Paulo Coelho finished uploading around 3 _______ documents created a virtual Paulo Coelho Foundation which is based in 4______."]


ans1 = ["lyricist", "novelist" , "brazil" ,"august 24,1947"]
ans2 = ["the alchemist","81", "washington" , "350" ]
ans3 = ["november" ,"2014","80,000","geneva"]



def play():
    #takes input regarding the level of the quiz from user.
    print "Welcome to the literature world !! \n Are you ready for the quiz??"
    user_input=raw_input("select the level")
    print(choose_level(user_input))
    i = 0
    n = 4 #n is the length of the no. of iterations of the quiz.
    while i < n :
        submit = []
        ans_input = raw_input("Enter the ans for " +str(i+1) +"?")
        if ans_input == right(user_input)[i] :
            print ("Well done! Your ans is correct . Keep going")
        else :
            print ("OOPS! Try Again.")
            continue
        i = i + 1
    if i == n :
        print ("EXCELLENT! \n You have won ! ^_^ ")
        play()
    else :
               print ("Keep calm and try again.")
               play() 
               
    
        

def choose_level(input_level):
    #takes in the user input of the desired level.
    if input_level.lower() == "1" :
        return quiz_ques1
        

    elif input_level.lower() =="2" :
        return quiz_ques2
        

    elif input_level.lower() == "3" :
        return quiz_ques3
       

    else :
        play() 
       
    

def right(ans):
    #checks whether the ans entered by user is correct or not .
    if ans.lower() == "1":
        return ans1
    elif ans.lower() == "2":
        return ans2
    elif ans.lower() == "3":
        return ans3 

play()
