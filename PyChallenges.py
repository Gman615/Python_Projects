import itertools

numbers = [5, 8, 6, 3, 10, 15, 77, 66, 33]
string = "tiger"
string2 = "Maaaaaan"

# calulates the total number of odds in the array
def totalOdds(nums):
    
    sum_odds = sum(n for n in nums if n % 2)
    print(sum_odds)
# calculates the total of the numbers in the array
def totalNums(nums):
    sum_all = sum(n for n in nums)
    print(sum_all)
# prints the string in reverse
def reverseString(thing):
    reverse = thing[::-1]
    print(reverse)
# removes duplicate letters   
def duplicateLetters(thing):
    thing = ''.join(sorted(set(thing), key=thing.index))
    print(thing)
# another way of doing the same thing
def dupLets(thing):
    thing = ''.join(c[0] for c in itertools.groupby(thing))
    print(thing)

totalOdds(numbers)
totalNums(numbers)
reverseString(string)
duplicateLetters(string2)
dupLets(string2)



                            
