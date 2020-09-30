import nltk

def score(sentence_tokens,word_frequencies):
  sentence_scores={}
  for sentence in sentence_tokens:
      for word in nltk.word_tokenize(sentence.lower()):
          if word in word_frequencies.keys():
              if(len(sentence.split(' ')))<30:
                  if sentence not in sentence_scores.keys():
                      sentence_scores[sentence]=word_frequencies[word]
                  else:
                      sentence_scores[sentence]+=word_frequencies[word]
   return sentence_scores                   
