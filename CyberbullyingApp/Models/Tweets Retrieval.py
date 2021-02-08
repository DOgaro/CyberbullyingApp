
# coding: utf-8

# In[2]:

#Importing packages and libraries
import twitter
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize


# In[3]:


#Putting credentials 
api = twitter.Api(consumer_key="LJEz9PSPqjrmVvZ6DO0ejeQjO",
  consumer_secret="qFzI7iO8sn1beJHGgfLL6FOv9hyXxszeJAtUJbh9FH7taGoEM7",
  access_token_key="806066029952729088-dbgGsMd0QTPSOTnRicf6Pvv2wBlMxfI",
  access_token_secret="nXJFnnyUXhsKmsbx2TPEEcMVZ4HkMLERo6KxNMaULNKNf")


# In[4]:


#Verifying credentials 
print(api.VerifyCredentials())


# In[5]:


#Attempting to strip as much emojis as possible by pattern
import re

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"
              "]+", flags=re.UNICODE)
print(emoji_pattern)

#In[56]:
#"curse word" example: 


search = api.GetSearch("f*#$ you", count=50)
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]
    print(clean_words)

#In[63]:
#"sexuality" example: 


search = api.GetSearch("you are a p*#$", count=50)
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]
    print(clean_words)


# In[76]:
# sample "mean word/phrase" example: 


search = api.GetSearch("nobody cares about you", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)
