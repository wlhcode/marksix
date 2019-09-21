import random
import time
import os

print("Mark Six Similator")
print("Guess six integers from 1 to 49 each game. $10 per bet.\n")
p = [15000000, 3000000, 1000000, 9600, 640, 320, 40]

if os.path.isfile("./save.txt") == 0:
	f = open("save.txt", "w")
	f.write("1\n0")
	f.close()
f = open("save.txt", "r")
t = int(f.readline())
b = int(f.readline())
c = bool(1)
f.close()

while c == 1:
	print("Round", t)
	print("Balance: $", round(b, 2), sep = '')
	
	print("Mark Six Guesses: ", sep = '', end = '')
	g = str(input())
	l = []
	i = 0
	for x in range(6):
		while g[i] == ' ': i += 1
		if i >= len(g): break
		l.append(int(ord(g[i]) - ord('0')))
		i += 1
		if i >= len(g): break
		if g[i] != ' ':
			l[x] *= 10
			l[x] += int(ord(g[i]) - ord('0'))
			i += 1
		i += 1
		continue
	l.sort()
	print("Your guesses are: ", end = '')
	for x in l: print(x, "", end = '')
	b -= 10
	
	print("\n")
	time.sleep(1)
	
	r = []
	z = int(0)
	for x in range(8):
		if x == 0: continue
		
		if x == 1: print("1st", end = '')
		elif x == 2: print("2nd", end = '')
		elif x == 3: print("3rd", end = '')
		elif x < 7: print(x, "th", sep = '', end = '')
		else: print("Special", end = '')
		print(" Number: ", end = '')
		
		m = bool(1)
		k = int(0)
		while m == 1:
			random.seed(time.time())
			k = random.randint(1, 49)
			for y in r:
				if k == y:
					m = 0
					break
			if m == 0: m = 1
			else: m = 0
		r.append(k)
		time.sleep(1)
		print(k)
		
		for y in l:
			if k == y:
				if x < 6: z += 10
				else: z += 5
				break
	
	print("\nYou got", z / 10, "numbers correct.")
	if z < 30: print("You did not win any prizes.")
	else:
		print("You have won the ", end = '')
		if z == 60: print("1st prize: $15M")
		elif z == 55: print("2nd prize: $3M")
		elif z == 50: print("3rd prize: $1M")
		elif z == 45: print("4th prize: $9600")
		elif z == 40: print("5th prize: $640")
		elif z == 35: print("6th prize: $320")
		else: print("7th prize: $40")
		
		b += p[-0.2 * z + 12]
	
	t += 1
	print("\nContinue? (y/n) ", end = '')
	v = str(input())
	if v == "n":
		c = 0
		f = open("save.txt", "w")
		f.write(str(t))
		f.write("\n")
		f.write(str(b))
		f.close()
		break
	else:
		c = 1
		print("\n-----\n")