#Text Cleaning:

        # remove non ASCII characters
        content = remove_non_ascii(content)
        # removing header number
        re.sub(r'^\s?\d+(.*)$', r'\1', text)
        # removing trailing spaces
        text.strip()
        # words may be split between lines, ensure we link them back together
        re.sub('\s?-\s?', '-', text)
        # remove space prior to punctuation
        re.sub(r'\s?([,:;\.])', r'\1', text)
        # ESG contains a lot of figures that are not relevant to grammatical structure
        re.sub(r'\d{5,}', r' ', text)
        # remove mentions of URLs
        re.sub(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', r' ', text)
        # remove multiple spaces
        re.sub('\s+', ' ', text)

#Lemmatization:
    doc = nlp(content) 
     # convert words into their simplest form (singular, present form, etc.)
    lemma = []
    for token in doc:
        if (token.lemma_ not in ['-PRON-']):
            lemma.append(token.lemma_)
          
#Vectorization and Stop Words removal
  from sklearn.feature_extraction.text import CountVectorizer
  word_tf_vectorizer = CountVectorizer(stop_words=stop_words, ngram_range=(1,1))
