#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).

# Caesar Cipher. (Oct. 3 2015) Retrieved from: https://inventwithpython.com/chapter14.html


print('------------------')
print(' Caesar Encoding')
print('------------------')

num=int(input('Please enter an integer between 1 and 25: '))
alpha1=65

#display plaintext alphabet
for alpha1 in range(alpha1,91):
    print(chr(alpha1),end="") 
    alpha1=alpha1+1
print()
alpha2=65+num

#print new Ciphertext alphabet 
while alpha2 in range (alpha2,91): 
    print(chr(alpha2),end="")
    alpha2=alpha2+1 
alpha3=65 
alpha4=65+num 
for alpha3 in range (alpha3,alpha4): 
    print(chr(alpha3),end="") 
print()

#get word to encode and change it to uppercase
code=input('Please type a word to be encoded: ').upper()
#print uppercase word
print("plaintext: ",code)
length=len(code)
x=0; #initialize counter

#diplay encoded cipher text
print('ciphertext: ',end='') 
for x in range (x,length): 
   Newcodeval=(ord(code[x]))+num 
   if Newcodeval<=90:
       Newcode=chr(Newcodeval) 
       print(Newcode, end="") 
   if Newcodeval>90: 
       num2=num-26 
       Newcode=chr((ord(code[x]))+num2) 
       print(Newcode, end="") 
       x=x+1;num2=num2+1 

print()