items = ["apple","banana","cherry"]
for item in items:
    if item.lower() == "apple":
        print(f"i don't like to eat {item}\n")
    elif item.lower() == "banana":
        print(f"{item} flavoured stuff taste nice\n")
    else:
        print(f"i have never had a {item}\n")
print("\n")
count = 0
vowel = "aeiouAEIOU"
word = input("enter a word: ")
for letter in word:
    if letter in vowel:
        count+=1
    print(f"you have {count} vowel(s) in your word")
print(f"you have a total of {count} vowels in your word {word}")
print("\n\n")
word1 = "PYTHON"
for letter in word1:
    print(f"{letter}\n")
print("\n")
for i in range(1,21):
    if i%2 == 0:
        print(f"{i}")
print("\n")
for i in range(1,6):
    if i ==3:
        continue
    print(f"{i}") 
