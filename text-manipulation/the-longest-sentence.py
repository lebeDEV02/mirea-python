file1 = open("text.txt", "r")

sentences = file1.read()

sentences = sentences.split('.')

punctuationsMarks = [',', ';', ':', '-', '[', ']', '{', '}', '`']

theLongestSentence = sentences[0]

numberOfPunctuationsMarks = int(0)

for k in theLongestSentence:
    if k in punctuationsMarks:
        numberOfPunctuationsMarks += 1


for item in sentences:
    counterOfMarks = 0
    for i in item:
        if i in punctuationsMarks:
            counterOfMarks += 1
    if int(counterOfMarks) > int(numberOfPunctuationsMarks):
        theLongestSentence = item
        numberOfPunctuationsMarks = counterOfMarks

print("Самое длинное предложение:")
print(theLongestSentence)
print("Количество знаков пунктуации: ")
print(numberOfPunctuationsMarks)
file1.close()