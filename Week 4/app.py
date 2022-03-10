#!/usr/bin/env python
# coding: utf-8

# In[11]:


from flask import Flask
app = Flask(__name__)
@app.route('/') # https://www.google.com/
def home():
    return 'Hello world'

app.run(port = 5000)


# In[ ]:




