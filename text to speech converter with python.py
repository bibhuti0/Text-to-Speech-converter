#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing the libraries
from newspaper import Article 
import nltk
from gtts import gTTS
import os 


# In[3]:


# get the article 
article  = Article('https://www.indiatoday.in/india/story/industrialist-ratan-tatas-long-pending-pets-project-rolls-out-in-south-mumbai-2499506-2024-02-09')
article.download()
article.parse()


# In[4]:


nltk.download('punkt')
article.nlp()


# In[5]:


# get the article text
mytext = article.text


# In[6]:


language = 'en' # english


# In[7]:


myobj = gTTS(text = mytext,lang=language,slow=False)


# In[12]:


myobj.save("read_article.mp3")


# In[13]:


os.system("start read_article.mp3")

