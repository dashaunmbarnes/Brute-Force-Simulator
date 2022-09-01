import replit
import random
digits=0
guess=""
guessc=0
lcl=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ucl=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ln=["1","2","3","4","5","6","7","8","9","0"]
sc1=["!","@","#","$","%","^","&","*","(",")"]
#list of everything
loa=[]
for item in lcl:
	loa.append(item)
for item in ucl:
	loa.append(item)
for item in ln:
	loa.append(item)
for item in sc1:
	loa.append(item)
#lower case letters and numbers
lcan=[]
for item in lcl:
	lcan.append(item)
for item in ln:
	lcan.append(item)
#all letters and numbers
laan=[]
for item in lcl:
	laan.append(item)
for item in ln:
	laan.append(item)
for item in ucl:
	laan.append(item)

#Set password level 1
while digits>1 or digits<1:
	print("Level 1 All Lower Case Letters 1 digit")
	password=input("")
	digits=len(password)
	replit.clear()
#Attempt to crack password level 1
while guess != password:
	
	guess=lcl[random.randint(0,25)]
	guessc=guessc+1
print("Level 1 took",guessc,"guesses")
print("Inputted Password:","",password)
print("Guessed Password:","",guess)
pause=input("Enter To Continue")
replit.clear()
#Set password level 2
while digits>2 or digits<2:
	print("Level 1 All Lower Case Letters 2 digits")
	password=input("")
	digits=len(password)
	replit.clear()
	guessc=0
#Attempt to crack password level 2
while guess != password:
	guess1dg=lcl[random.randint(0,25)]
	guess2dg=lcl[random.randint(0,25)]
	guess=guess1dg+guess2dg
	guessc=guessc+1
print("Level 2 took",guessc,"guesses")
print("Inputted Password:","",password)
print("Guessed Password:","",guess)
pause=input("Enter To Continue")
replit.clear()
#Set password level 3
while digits>3 or digits<3:
	print("Level 1 All Lower Case Letters 3 digits")
	password=input("")
	digits=len(password)
	replit.clear()
	guessc=0
#Attempt to crack password level 3
while guess != password:
	guess1dg=lcl[random.randint(0,25)]
	guess2dg=lcl[random.randint(0,25)]
	guess3dg=lcl[random.randint(0,25)]
	guess=guess1dg+guess2dg+guess3dg
	guessc=guessc+1
print("Level 3 took",guessc,"guesses")
print("Inputted Password:","",password)
print("Guessed Password:","",guess)
pause=input("Enter To Continue")
replit.clear()
#Set password level 4
digits=0
while digits>3 or digits<3:
	print("Level 4 All Lower Case Letters or numbers[0-9] 3 digits")
	password=input("")
	digits=len(password)
	replit.clear()
	guessc=0
#Attempt to crack password level 4
while guess != password:
	
	guess1dg=lcan[random.randint(0,35)]
	guess2dg=lcan[random.randint(0,35)]
	guess3dg=lcan[random.randint(0,35)]
	guess=guess1dg+guess2dg+guess3dg
	
	guessc=guessc+1
	if guessc<100001:
		if guessc%10000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>100000 and guessc<1000000:
		if guessc%100000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>999999 and guessc<1000001:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>1000000 and guessc<10000000:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)
replit.clear()
print("Level 4 took",guessc,"guesses")
print("Inputted Password:","",password)
print("Guessed Password:","",guess)
pause=input("Enter To Continue")
replit.clear()
#Set password level 5
digits=0
while digits>3 or digits<3:
	print("Level 5 All Letters or numbers[0-9] 3 digits")
	password=input("")
	digits=len(password)
	replit.clear()
	guessc=0
#Attempt to crack password level 5
while guess != password:
	guess1dg=laan[random.randint(0,61)]
	guess2dg=laan[random.randint(0,61)]
	guess3dg=laan[random.randint(0,61)]
	guess=guess1dg+guess2dg+guess3dg
	
	guessc=guessc+1
	if guessc<100001:
		if guessc%10000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>100000 and guessc<1000000:
		if guessc%100000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>999999 and guessc<1000001:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>1000000 and guessc<10000000:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)
replit.clear()

#Recap Level 5
print("Level 5 took",guessc,"guesses")
print("Inputted Password:","",password)
print("Guessed Password:","",guess)
pause=input("Enter To Continue")
replit.clear()
#Set password level 6
digits=0
while digits>3 or digits<3:
	print("Level 6 All Letters or numbers[0-9],special characters[0-9] 3 digits")
	password=input("")
	digits=len(password)
	replit.clear()
	guessc=0
#Attempt to crack password level 6
while guess != password:
	
	guess1dg=loa[random.randint(0,71)]
	guess2dg=loa[random.randint(0,71)]
	guess3dg=loa[random.randint(0,71)]
	guess=guess1dg+guess2dg+guess3dg
	
	
	guessc=guessc+1
	if guessc<100001:
		if guessc%10000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>100000 and guessc<1000000:
		if guessc%100000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>999999 and guessc<1000001:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>1000000 and guessc<10000000:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)
replit.clear()
#recap level 6
print("Level 6 took",guessc,"guesses")
print("Inputted Password:","",password)
print("Guessed Password:","",guess)
pause=input("Enter To Continue")
replit.clear()
#Set password level 7
digits=0
while digits>4 or digits<4:
	print("Level 7 All Letters or numbers[0-9],special characters[0-9] 4 digits")
	password=input("")
	digits=len(password)
	replit.clear()
	guessc=0
#Attempt to crack password level 7
while guess != password:
	
	guess1dg=loa[random.randint(0,71)]
	guess2dg=loa[random.randint(0,71)]
	guess3dg=loa[random.randint(0,71)]
	guess4dg=loa[random.randint(0,71)]
	guess=guess1dg+guess2dg+guess3dg+guess4dg
	
	
	guessc=guessc+1
	
	if guessc<100001:
		if guessc%10000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>100000 and guessc<1000000:
		if guessc%100000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>999999 and guessc<1000001:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>1000000 and guessc<10000000:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)

replit.clear()
#recap level 7
print("Level 7 took",guessc,"guesses")
print("Inputted Password:","",password)
print("Guessed Password:","",guess)
pause=input("Enter To Continue")
replit.clear()
#Set Password Level 8
digits=0
while digits>5 or digits<5:
	print("Level 8 All Letters or numbers[0-9],special characters[0-9] 5 digits")
	password=input("")
	digits=len(password)
	replit.clear()
	guessc=0
#Attempt to crack password level 8
while guess != password:
	
	guess1dg=loa[random.randint(0,71)]
	guess2dg=loa[random.randint(0,71)]
	guess3dg=loa[random.randint(0,71)]
	guess4dg=loa[random.randint(0,71)]
	guess5dg=loa[random.randint(0,71)]
	guess=guess1dg+guess2dg+guess3dg+guess4dg+guess5dg
	
	
	guessc=guessc+1
	
	if guessc<100001:
		if guessc%10000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>100000 and guessc<1000000:
		if guessc%100000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>999999 and guessc<1000001:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)
	if guessc>1000000 and guessc<10000000:
		if guessc%500000==0:
			print("Guess#","",guessc,"",guess)
replit.clear()
#recap level 8
print("Level 8 took",guessc,"guesses")
print("Inputted Password:","",password)
print("Guessed Password:","",guess)
pause=input("Enter To Continue")
replit.clear()