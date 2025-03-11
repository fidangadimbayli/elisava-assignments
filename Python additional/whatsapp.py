import emoji
from collections import Counter

filename = "_chat.txt"
count = 0

def get_emojis(message):
    emojis = []
    for character in messages:
        if charachter not in EMOJI_DATA:
            emojis.append(character)
        return emojis
    
def get_emojis(message):
   
    return [char for char in message if char in emoji.EMOJI_DATA]

def get_author(message):
    try:
        return message.split("~")[1].split(":")[0]
    except IndexError:
        return None
def get_author(message):
    try:
        return message.split("~")[1].split(":")[0]
    except IndexError:
        return None
messages = []
with open(filename) as file:
    for line in file:
        messages.append(line)
        # count = count + 1

count = len(messages)
print(f"there are {count} messages in the chat")
# author = get_author(messages[3])

# print("who wrote the first message?", author)

authors = [get_author(message) for message in messages if message is not None]
authors_counter = Counter(authors)
authors = []

# for message in messages:
#     author = get_author(message)
#     if author is not None:
#         authors.append(author)
        

# authors_counter = Counter(authors)

for (author, count) in authors_counter.most_common():
    print(f"{author} wrote {count} messages")

    # print(get_author(message))

emoji_list = []
for message in messages:
    emoji_list.extend(get_emojis(message))

emoji_counter = Counter(emoji_list)

# Print most common emojis
print("\nMost popular emojis:")
for emoji_char, count in emoji_counter.most_common(10):  # Top 10 emojis
    print(f"{emoji_char} used {count} times.")