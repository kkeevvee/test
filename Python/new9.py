#Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

# Write your reverse_string function here:
def reverse_string(word):
  wynik = []
  for i in range (0, len(word)):
    wynik.append(word[len(word)-1-i:len(word)-i])
    print(wynik)
    print("\n")
  return "".join(wynik)
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print