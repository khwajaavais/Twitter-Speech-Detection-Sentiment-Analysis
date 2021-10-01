# TWITTER SPEECH DETECTION - SENTIMENT ANALYSIS

**DEMO: https://twitter-speech-detection-04.herokuapp.com/**

## PROJECT DESCRIPTION
The context of this project is to classify the Positive and the Negative **real-time** Tweets fetched from the **Twitter API** using the Machine Learning and the Natural Language Programming algorithms.

## AIM & OBJECTIVE
The aim of this project is to implement the Logistic Regression Algorithm and NLP Algorithms along with help of sentiment analysis in a newer manner and evaluate the performance of the chosen Machine Learning and NLP algorithm to find out the best suitable and efficient model for the chosen data set.

### OBJECTIVE
- To understand the efficient use of Twitter API and the machine learning model.
- To evaluate the performance of the selected models

## WHAT IS SENTIMENT ANALYSIS?
The process of detecting positive or negative sentiment in text is known as sentiment analysis. Businesses mostly use it to detect sentiment in social data, assess brand reputation, and gain a better understanding of their customers.

![App Screenshot](https://github.com/khwajaavais/Twitter-Speech-Detection-Sentiment-Analysis/blob/7f61b11ffd8997a67554c87c7e5783dc2a836caa/templates/sentiments.JPG)

**Sentiment analysis** is becoming a crucial tool for monitoring and understanding client sentiment as they share their opinions and feelings more openly than ever before. 

Brands can learn what makes customers happy or frustrated by automatically evaluating customer feedback, such as comments in survey replies and social media dialogues. This allows them to customise products and services to match their customers' demands.

The overall **benefits** of sentiment analysis include:
- Sorting Data at Scale
- Real-Time Analysis
- Consistent criteria

## ABOUT THE DATA

    Attribute Information (in order):
        - ID      Tweet I'd
        - Tweet   Actual Tweet

        - Label   Class 0 - Positive Tweet
                  Class 1 - Negative Tweet

    Missing Attribute Values: None

## TECHNICAL ASPECTS

1. **MODEL BUILDING**
The implementation of the Twitter Speech Deteching Model Building is done in 3 steps.

**STEP - 1:** As we know the TWITTER data contains lots of stops words.
- **Stop words** are a group of words that are frequently employed in a language. Stop words in English include "a," "the," "is," "are," and others. 
- Stop words are frequently used in Text Mining and Natural Language Processing (NLP) to exclude terms that are so widely used that they contain little meaningful information.

For implementation, I used the TF-IDF Vectorizer Algorithm for removing the English stop words and fetched the top 1,000 most used words from the text.

**STEP - 2:** Implementation of Logistic Regression
- As the problem  statement was about classification of real-time Tweets; **Logistic Regression** is used.

        Class 0 - Positive Tweets
        Class 1 - Negative Tweets

**STEP - 3: PIPELINE CREATION**

As both the above steps were important for classifying the Tweet as Postive or Negative; a Pipeline was created were both the above steps were implemented in this single step.

Where first the data was cleaned using the TF-IDF and then this data is passed for the classification purpose.

2. **CHECKING THE BALANCE OF THE DATASET**

        % of Class 0 : 92.99%
        % of Class 1 : 7.01

        Our Dataset is imbalance as Class 0 is almost the 13x times of Class 1. 
        So we need to up-sample to balance the dataset. 

    RandomOverSampler was implemented to balance the dataset.

    After the implementation of RandomOverSampler; another **PIPELINE** was created to predict the classification model.

3. **TWITTER API SETUP**

    To fetch the real-time Tweets from the Twitter API; we need to create the **TWITTER DEVELOPER ACCOUNT** in order fetch the Tweets.
 
   Steps for creating the Twitter Developer Account follow: 
    https://github.com/khwajaavais/Twitter-Speech-Detection-Sentiment-Analysis/blob/main/Twitter%20Account%20Setup.md

## MODEL DEPLOYMENT
**LOCALHOST**

For implementating the project in your own system follow the steps;

- Download the directory
- Open the Command Prompt (CLI) and change the command line path to this current file path.
- Run the command

        python app.py

- Hit http://127.0.0.1:5000/

-  

**WEB APPLICATION**

For deploying the project via Heroku platform

Follow Krish Naik`s Deployment of ML models in Heroku using Flask 
https://www.youtube.com/watch?v=mrExsjcvF4o

**Note**: Mandatory Files required while deploying ML Model in Heroku using Flask

1. app.py
2. Procfile
3. model.pkl file (Pickle File)
4. request.py
5. requirement.txt
6. templates / index.html (UI File)
7. static/css/ style.css
(You can use my Repository to follow the steps)


## INSTALLATION
The Code is written in Python 3.7. If you don't have Python installed you can find it [there](https://www.python.org/downloads/)
. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 
To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

    pip install -r requirements.

## Conclusion and Future Work
- Implementation of Machine Learning Pipeline(Logistic Regression Algorithm and Natural Language Processing) for the classifying the real-time Tweets  is successful.

**FUTURE WORK**
- With the increase in dataset; a more accurate model can be build up and with more values within the Label Attribute (e.g. 'Neutral')

## SCREENSHOTS

**DEMO: https://twitter-speech-detection-04.herokuapp.com/**

### INDEX PAGE
![App Screenshot](https://github.com/khwajaavais/Twitter-Speech-Detection-Sentiment-Analysis/blob/36a3a7dbee1acbf0111f7d24145316900b8f3471/templates/INDEX%20PAGE.png)

### RESULT PAGE
![App Screenshot](https://github.com/khwajaavais/Twitter-Speech-Detection-Sentiment-Analysis/blob/36a3a7dbee1acbf0111f7d24145316900b8f3471/templates/RESULT%20PAGE.png)