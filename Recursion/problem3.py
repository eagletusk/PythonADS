def word_split(phrase,list_of_words,output=None):
  new = ''
  new = phrase
  a= []
  if len(phrase) == 0:
    return True

  if (list_of_words[0] in phrase):
    i = phrase.index(list_of_words[0])
    end = len(list_of_words[0])+i+ 1
    new = phrase[0:i:] + phrase[end-1::]

    a = list_of_words[1::]
    print(new,a,i)
    return word_split(new,a)
  return False


print(word_split('themanran',['the','ran','man'], None))
print(word_split('themanran',['clown','ran','man']))