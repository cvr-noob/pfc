text = input("Enter the sentence: ")

freq = {}

for i in text:
    if i in freq.keys():
        freq[i] += 1
    else:
        freq[i] = 1

print("The frequency of each letter is:", freq)
