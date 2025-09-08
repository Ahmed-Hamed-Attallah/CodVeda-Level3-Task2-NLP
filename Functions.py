# Natural Language Toolkit
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))




# Function for make new columns (Traget: spam/ham)
def check_spam (emotion):
    """
    Maps a primary emotion category to a spam/ham target based on 
    common spam message tactics.
    """
    # Define which emotions are likely used in spam
    spam_cues = ['excitement', 'euphoria', 'surprise', 'fear', 'anxiety', 'neutral']
    
    # Convert input to lowercase for case-insensitive comparison
    emotion_str = str(emotion).lower()
    
    if emotion_str in spam_cues:
        return 'spam'
    else:
        return 'ham'



# Function to create Emotions column by useing sentiment label 
def map_emotion(sentiment_label):
    
    label = str(sentiment_label).lower()
    
    # Map variations of Happy
    if label in ['happiness', 'joy', 'enjoyment', 'elation', 'euphoria', 'overjoyed', 'happy']:
        return 'Happiness'
    
    # Map variations of Sadness
    elif label in ['sadness', 'grief', 'sorrow', 'melancholy', 'despair', 'heartbreak', 'sad']:
        return 'Sadness'
    
    # Map variations of Anger
    elif label in ['anger', 'frustration', 'resentment', 'bitterness', 'hate']:
        return 'Anger'
    
    # Map variations of Fear
    elif label in ['fear', 'anxiety', 'apprehensive', 'worry']:
        return 'Fear'
    
    # Map variations of Surprise
    elif label in ['surprise', 'awe', 'amazement', 'wonder']:
        return 'Surprise'
    
    # Map positive but calm states
    elif label in ['calmness', 'contentment', 'serenity', 'tranquility', 'gratitude', 'relief']:
        return 'Contentment'
    
    # If the emotion is already a good primary category, keep it.
    elif label in ['positive', 'negative', 'neutral', 'love', 'disgust', 'shame', 'pride', 'curiosity', 'boredom', 'excitement', 'hope', 'optimism', 'nostalgia']:
        return sentiment_label.title()
    
    # For all the complex/creative ones, you might map them to a broader category or keep them as "Other"
    else:
        return 'Other' 




def clean_text(text):
    text = str(text).lower()
    words = word_tokenize(text,preserve_line="C:/Users/ahmed/AppData/Roaming/nltk_data/tokenizers")
    words = [word for word in words if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    
    return words



def plot_wordcloud(word_freq, text):
    wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.title(text, fontsize=16)
    plt.axis('off')
    plt.show()
