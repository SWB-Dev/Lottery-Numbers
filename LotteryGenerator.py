#Steven Barnes 10/28/18
#Simple script to generate a powerball ticket.  You can pass Odds and Evens parameters into the Lottery() function
#if you wanted a specific number of odds or a specific number of evens.  Not 100% function as it doesn't handle if
#odds and evens add up to more than 6.

from random import randint

def Lottery(Odds=None,Evens=None):

	picks = []

	def NumGen(Type=None):
		number = randint(1,71)

		if Type == "Even":
			while number % 2 != 0:
				number = randint(1,71)
		elif Type =="Odd":
			while number % 2 == 0:
				number = randint(1,71)
		elif Type == None:
			number = randint(1,71)
		return number

	
	if Odds != None:
		pick = NumGen("Odd")
		for x in range(Odds):
			while pick in picks:
				pick = NumGen("Odd")
			print(f'{x} - {pick}')
			picks.append(pick)

	if Evens != None:
		pick = NumGen("Even")
		for x in range(Evens):
			while pick in picks:
				pick = NumGen("Even")
			print(f'{x} - {pick}')
			picks.append(pick)

	while len(picks) < 6:
		pick = NumGen()
		while pick in picks:
			pick = NumGen()
		picks.append(pick)

	picks.sort()
	lotteryPicks = {"Picks": picks,"PowerBall":randint(1,26)}
	return lotteryPicks

if __name__ == "__main__":

	picks = Lottery()
	print(picks)

