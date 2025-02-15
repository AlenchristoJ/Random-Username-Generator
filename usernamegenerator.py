import random
adjectives = ["Cool", "Happy", "Silly", "Brave", "Fast", "Smart", "Crazy", "Funny", "Epic", "Chill"]
nouns = ["Tiger", "Dragon", "Lion", "Panda", "Shark", "Eagle", "Wolf", "Bear", "Falcon", "Cheetah"]
print("Welcome to the Random Username Generator!")
print("Would you like to add numbers to the username? (yes/no)")
add_numbers = input().lower()
print("Would you like to add special characters? (yes/no)")
add_special_chars = input().lower()
random_adj = adjectives[random.randint(0, len(adjectives)-1)]
random_noun = nouns[random.randint(0, len(nouns)-1)]
username = random_adj + random_noun
if add_numbers == "yes":
    username += str(random.randint(10, 99))
if add_special_chars == "yes":
    username += random.choice(["!", "@", "#", "$", "%", "&", "*"])
print("Generated Username:", username)
with open("usernames.txt", "a") as file:
    file.write(username + "\n")
print("Username saved to usernames.txt")