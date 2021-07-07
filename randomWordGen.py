from random_word import RandomWords
r = RandomWords()

ranWords = r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="verb", limit=5)

for word in ranWords:
    print(word)