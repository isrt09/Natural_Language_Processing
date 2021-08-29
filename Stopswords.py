######################################### 1st WAY ###########################
    import nltk
    from nltk import sent_tokenize            
    from nltk import word_tokenize            

    text = "Recurrent Neural Networks (RNNs), a class of neural networks, are essential in processing sequences such as sensor measurements, daily stock prices, etc. In fact, most of the sequence modelling problems on images and videos are still hard to solve without Recurrent Neural Networks. Further, RNNs are also considered to be the general form of deep learning architecture. Hence, the understanding of RNNs is crucial in all the fields of Data Science. This course addresses all these concerns and empowers you to take your career to the next level with a masterful grip on the theoretical concepts and practical implementations of RNNs in Data Science"

    sentences = nltk.sent_tokenize(text)
    words     = nltk.word_tokenize(text)

    from nltk import PorterStemmer
    from nltk import WordNetLemmatizer

    port = PorterStemmer()
    lem  = WordNetLemmatizer()

    from nltk.probability import FreDist
    fsDist = FreDist(words)


    ######################################### 2ND WAY ###########################
    import nltk
    from nltk.tokenize    import sent_tokenize, word_tokenize
    from nltk.stem        import PorterStemmer, WordNetLemmatizer
    from nltk.corpus      import stopwords
    from nltk.probability import FreDist

    message = "Albert Einstein was born in Ulm, Germany in 1879."
        
    tokenized_sentence = sent_tokenize(message)
    tokenized_word     = word_tokenize(message)
    
    nltk.pos_tag(tokenized_word)
    FreDist(tokenized_word)

    # Removing stopwords
    for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [word for word in words if word not in stopwords.words('english')]
    sentences[i] = ' '.join(words)  
