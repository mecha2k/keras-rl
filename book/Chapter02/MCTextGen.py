from Chapter02.markovify import Text

with open("corpus1.txt") as f:
    CorpusText = f.read()

TextModel = Text(CorpusText)

print("Five randomly-generated sentences")
print("-----------------------------------")
for i in range(5):
    print(TextModel.make_sentence())

print("-----------------------------------")
print("three randomly-generated sentences of no more than 100 characters")
print("-----------------------------------")
for i in range(3):
    print(TextModel.make_short_sentence(100))
