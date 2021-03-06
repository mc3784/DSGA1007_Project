'''
Created on Dec 5, 2015

@author: urjit0209,vec241, mc3784
'''

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier
import timeit
import time

class Video():

    title         =""
    description   = ""

    def __init__(self,title,description):
        """
            Video Constructor: initialize all the video's features.
        """

        self.title = title
        self.description = description

    @staticmethod
    def generatePredictingModel(data):
        """
            Build the prediction model (based on the data set we have) in order to be able to predict the category
            of a new video from the user input
            Return a classifier able to predict the category of a video based on its title and description.
        """

        # Intitialize a timer to compute the time to build the model
        start = time.time()

        # Replace the NaN values in 'description'
        data['description'].fillna('No description', inplace=True)

        # Split into train-test data set
        X = data[[x for x in data.columns if x in ('title', 'description')]]
        Y = data[[x for x in data.columns if x in ('video_category_id')]]
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.80, random_state = 10)

        # Build the 2 text corpus
        corpus_title = X_train['title'].values.tolist()
        corpus_description = X_train['description'].values.tolist()

        # initializes the 2 vectorizers.
        count_vectorizer_title = CountVectorizer()
        count_vectorizer_description = CountVectorizer()

        # learn the 2 vocabulary dictionary
        count_vectorizer_title.fit(corpus_title)
        count_vectorizer_description.fit(corpus_description)

        # Build the sparse matrices
        X_train_count_title = count_vectorizer_title.transform(X_train['title'])
        X_train_count_description = count_vectorizer_description.transform(X_train['description'])
        X_test_count_title = count_vectorizer_title.transform(X_test['title'])
        X_test_count_description = count_vectorizer_description.transform(X_test['description'])

        # Set and train the models (for title and description features)
        model_count_title = BernoulliNB()
        model_count_description = BernoulliNB()
        model_count_title.fit(X_train_count_title, Y_train['video_category_id'])
        model_count_description.fit(X_train_count_description, Y_train['video_category_id'])

        # Merge the title and description predictions and build a new prediction based on these 2 predictions combined
        new_df_train = pd.DataFrame()
        new_df_train['title_prediction'] = model_count_title.predict(X_train_count_title)
        new_df_train['description_prediction'] = model_count_description.predict(X_train_count_description)
        new_df_test = pd.DataFrame()
        new_df_test['title_prediction'] = model_count_title.predict(X_test_count_title)
        new_df_test['description_prediction'] = model_count_description.predict(X_test_count_description)
        tree = DecisionTreeClassifier()
        tree.fit(new_df_train, Y_train)

        end = time.time()
        execution_time = end - start

        print "Time to build this incredibly amazing model, only : {} seconds!!!!!!".format(execution_time)
        time.sleep(3) # delay for 3 seconds
        print "\nNow give it a try and check out our awesome predictions !!!"
        time.sleep(3) # delay for 3 seconds

        return tree, model_count_title, model_count_description,count_vectorizer_title,count_vectorizer_description

    def predictVideoCategory(self,tree,model_count_title,model_count_description,count_vectorizer_title,count_vectorizer_description):
        """
            Predict the category of the video
        """

        vect_title = count_vectorizer_title.transform([self.title])
        vect_description = count_vectorizer_description.transform([self.description])

        title_based_prediction = model_count_title.predict(vect_title)
        description_based_prediction = model_count_description.predict(vect_description)

        video_df = pd.DataFrame({'title_prediction': title_based_prediction,
                                 'description_prediction': description_based_prediction})

        category_prediction = tree.predict(video_df)

        return category_prediction[0]


    def assignLabel(self):
        """
            Write logic to perform the prediction of the label and return the label value
        """
        print "Performing label prediction for the inserted data..."
        return "label"


