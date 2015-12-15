'''
Created on Dec 5, 2015

@authors: urjit0209,vec241, mc3784
'''

import sys
import matplotlib.pyplot as plt
import DataPlotter as dataplotter
import time

class DataStatistics():
    features = {"1":"viewCount", "2":"likeCount", "3":"dislikeCount", "4":"favoriteCount","5":"commentCount","6":"dimension", "7":"definition", "8":"caption"}
    Catagory_mapping = {2: 'Autos & Vehicles', 23: 'Comedy' , 27: 'Education', 24: 'Entertainment' , 1: 'Film & Animation', 20: 'Gaming' ,26: 'Howto & Style', 10: 'Music',25: 'News & Politics', 29:'Nonprofits & Activism' ,22:'People & Blogs', 15: 'Pets & Animals' , 28: 'Science & Technology', 17: 'Sports' , 19:'Travel & Events'}
    def __init__(self):
        print "Perform data analysiss..."
    """
    def printExploreOptions(self):
        print "String with a short description of the program and how it works. Than the list of option...\n \
               2) press 1 for general analysis \n \
               1) press 2 for individual analyisis of each video catagory \n \
               3) press 3 for individual feature analysis "

    def InitiateDataExplorer(self,data):
        self.data = data
        self.printExploreOptions()
        self.userInputLoop()

    def userInputLoop(self):
        '''
            Create a loop asking the user which action he or she wants to take. The loop is break (and the program ends) whenever the user type quit.
        '''
        userInput=""
        try:
            while userInput != "quit":
                userInput = raw_input("Please enter one of the number: ")
                if userInput == "1":
                    pass
                elif userInput == "2":
                    self.individual_videocatagory_analysis()
                elif userInput == "3":
                    self.individual_feature_analysis()
        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()
    """


    def individual_videocatagory_analysis(self,data):
            dataframe = data
            variable_names = ["viewCount", "likeCount", "dislikeCount", "favoriteCount","commentCount","dimension", "definition", "caption","licensedContent"]
            count_features = ["viewCount", "likeCount", "dislikeCount", "favoriteCount","commentCount"]
            columnNames = dataframe.columns.values
            print columnNames
            video_ids = dataframe["video_category_id"].unique()


            for video_id in video_ids:

                print "\n==============="
                print "Analysis for video catagory = ",video_id
                print "===============\n"
                VideoCatagoryData = dataframe[dataframe["video_category_id"]==video_id]
                VideoCatagory_CountData = VideoCatagoryData[count_features]
                description = VideoCatagoryData.describe()
                correlation = VideoCatagory_CountData.corr(method='pearson', min_periods=1)
                print "description of each feature - "
                print description
                print "correlation within count features - "
                print correlation

                print "\nCount for Binary features :------> \n"
                print "Dimension : 2d(1) , 3d(0)"
                dim=VideoCatagoryData.groupby('dimension')['video_category_id'].count()
                print dim
                print "definition : hd(1) , sd(0)"
                defi=VideoCatagoryData.groupby('definition')['video_category_id'].count()
                print defi
                print "caption : TRUE(1) , FALSE(0)"
                cap=VideoCatagoryData.groupby('caption')['video_category_id'].count()
                print cap
                print "caption : TRUE(1) , FALSE(0)"
                lic=VideoCatagoryData.groupby('licensedContent')['video_category_id'].count()
                print lic


            """
            columnNames = dataframe.columns.values
            nl= dataframe.isnull().sum()
            print "Number of rows containing null values =",nl
            #print nl['description']
            #print type(nl)
            #print columnNames

            print "Analysis for feature "
            #dimension
            dim=dataframe.groupby('dimension')['video_category_id'].count()

            #definition
            defi=dataframe.groupby('definition')['video_category_id'].count()

            #caption
            dataframe['caption'] = (dataframe['caption'])*1
            #licensedContent
            dataframe['licensedContent'] = (dataframe['licensedContent'])*1

            #df1=dataframe[variable_names]
            #print df1

            new_dataframe  = dataframe[variable_names]
            #print new_dataframe
            description = new_dataframe.describe()
            correlation = new_dataframe.corr(method='pearson', min_periods=1)
            print "description of each feature - "
            print description
            print "correlation within features - "
            print correlation
            #print dataframe.groupby([columnNames[0]])['viewCount'].mean()
            #for col in columnNames:
            #    print
            """
    def printCategories(self):
        """
            Print the list of features in the dataset 
        """
        for key in self.features:
            print key, "-->", self.features[key]


    def individual_feature_analysis(self,data,chosenFeature):
        """
            Compute a group by on the chosenFeature and call featuresBarPlot to plot the result 
        """
            print "chosen feature: ",self.features[chosenFeature]
            featuresMeans = data.groupby(['video_category_id'])[self.features[chosenFeature]].mean()
            featuresNames = [self.Catagory_mapping[x] for x in featuresMeans.index]
            dataplotter.featuresBarPlot(featuresNames,featuresMeans.values)


    def generalAnalysis(self,data,clf):

            dataplotter.plotFeatureImportance(data,clf)

            dataplotter.plotCorrelationMatrix(data)






