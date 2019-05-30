# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
# we can use ord function that returns the unique number of a character.

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))
