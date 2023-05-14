## Define function to predict topic for a given text document.
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
def predict_topic(text, nlp=nlp):
    global sent_to_words
    global lemmatization
# Step 1: Clean with simple_preprocess
    mytext_2 = list(sent_to_words(text))
    
# Step 2: Lemmatize
    mytext_3 = lemmatization(mytext_2, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
    
# Step 3: Vectorize transform
    mytext_4 = word_tf_vectorizer.transform(mytext_3)
# Step 4: LDA Transform
    topic_probability_scores = best_lda_model.transform(mytext_4)
    topic = df_topic_keywords.iloc[np.argmax(topic_probability_scores), 1:15].values.tolist()
# Step 5: Infer Topic
    infer_topic = df_topic_keywords.iloc[np.argmax(topic_probability_scores), 0]
    
    return infer_topic, topic, topic_probability_scores

# Predict the topic
#Replace mytext with output csv of data extraction and cleanup
mytext = ['make write or oral forward look statement within the meaning of certain security law include the safe harbour provision of the united states private securities litigation reform act of and any applicable canadian security legislation']
infer_topic, topic, prob_scores = predict_topic(text = mytext)
print(mytext)
print(infer_topic)
print(prob_scores)