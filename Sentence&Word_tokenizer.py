import nltk

def tokenizer(finalContent):
  sentence_tokens=nltk.sent_tokenize(finalContent)
  words_tokens=nltk.word_tokenize(finalContent)
  return sentence_tokens,words_tokens
