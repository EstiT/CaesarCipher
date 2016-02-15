#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).


print('------------------')
print(' Caesar Decoding')
print('------------------')


string=input("Please type the string to be decoded: ").upper()
ques=input("Do you know the integer that was used to encode this? ('yes'/'no' )")
x=0 ;w=0#initialize counters
y=ord(string[0])#get value of first letter in string
length=len(string)

#if user knows integer that text was shifted by
if ques=="yes": 
    num=int(input("Please enter the integer: "))#get the integer 
    #if the integer is outside of valid range
    if num <=0 or num>=26:
        print("That is not possible; a Caesar cipher requires an integer between 1 and 25")#display error
        num=int(input("Please enter the integer: ")) #have user try again
        print("The decrypted text must be: ", end="")
        while (x<length): #run through as long as there are letters left in the text
            letter=string[x]#each letter in the text
            letrval=ord(letter)-num #change the letter to its number value then subtract the integer inputed
            letr=chr(letrval) #change that value to a letter
            print(letr,end="") #print the decoded letter
            x=x+1 #increase counter for next letter
            if x==length: #once reached end of word, youre done
                print()
                break
    #if the number that the user entered is within the possible range  
    else: 
        print("The decrypted text must be: ", end="")
        while (x<length):#run through as long as there are letters left in the text
            letter=string[x]#each letter in the text
            letrval=ord(letter)-num#change the letter to its number value then subtract the integer inputed
            if letrval< 65: #check if the letters shifted value is changed to a symbol that is not a letter
                diff= 65- letrval
                letrval=90-diff + 1
            letr=chr(letrval)#change that value to a letter
            print(letr,end="")#print the decoded letter
            x=x+1#increase counter for next letter
            if x==length:#once reached end of word, youre done
                print()
                break

#if the user does not know the integer used to shift the text              
if ques=="no": 
    x=0 ;y=1; w=0#initialize counters
    print("The text must be one of the following: ") 
    #run for all letters of the alphabet  
    while w<=25: 
        while x in range (x,length): #run for every letter in the text
            letrval=ord(string[x])+y #convert to ascii value
            if letrval>90: #check if the value is greater than 'Z' value
                z = -26 + y #if it is then the new counter brings it back to "A"
                letrval=ord(string[x])+z #change to value and bring back to "A" and shift
            letter2=chr(letrval) #convert to letter
            print(letter2,end="") #print letter
            x=x+1; #increase counter for next letter
            
        w=w+1;y=y+1;x=0 #increase counters for next possibility 
        print()
    
if ques!="no" and ques!="yes": #if the user typed neither yes or no 
    print("Error. That was not one of the options.") # display error messege
                
                
	
	