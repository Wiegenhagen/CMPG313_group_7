#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import gradio as gr


# In[2]:


from tensorflow.keras.layers import TextVectorization


# In[3]:


import os
import pandas as pd
import tensorflow as tf
import numpy as np


# In[4]:


df = pd.read_csv('/Users/Arina/Documents/project_backend/train.csv')


# In[5]:


X = df['comment_text']


# In[ ]:





# In[6]:


MAX_FEATURES = 200000 


# In[7]:


vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                               output_sequence_length=1800,
                               output_mode='int')


# In[8]:


vectorizer.adapt(X.values)


# In[9]:


vectorized_text = vectorizer(X.values)


# In[ ]:





# In[10]:


model = tf.keras.models.load_model('toxicity.h5')


# In[11]:


def score_comment(comment):
    vectorized_comment = vectorizer([comment])
    results = model.predict(vectorized_comment)
    
    text = ''
    for idx, col in enumerate(df.columns[2:]):
        text += '{}: {}\n'.format(col, results[0][idx]>0.5)
    
    return text


# In[12]:


interface = gr.Interface(fn=score_comment, 
                         inputs=gr.inputs.Textbox(lines=2, placeholder='Comment to score'),
                        outputs='text')


# In[13]:


interface.launch(share=True)


# In[ ]:




