# CMPG313_group_7

This is commentToxicty model for our AI project, we used the model that was created by Nicholas Renotte. gh repo clone nicknochnack/CommentToxicity. 
When recreating this model in Jupyter (Python) we changed the Epoch to 3 and a second time to 5, to compare the precision, recall and accuracy of the model. 
If we were able to train the model longer let say over 10 hours the metrics would have improved significantly but loadshedding and my computer processing power does 
not allow that. 

For the data file please follow this link to the githib account of the person who created the model. The data file is to large to upload. 
https://github.com/nicknochnack/CommentToxicity/blob/bf910d57d1a13a902f472141781683108da3d920/jigsaw-toxic-comment-classification-challenge/train.csv/train.csv

THe FinalModelwithComments.py file contains the model without the testing code between steps. It contains comments for each step. 
The saved model hour 5.py is the where you can access the saved model and used it to predict comments, but because the saved model is to big it is not included in 
this repository but it can be access by following the link for the data file. I kept the naming the same does there is no need to change the model name in the code. 
Maybe just the path. 
Because I used Python with Jupyter there was alot of imports needed to be done. Firstly you need to install pip to make the install of the packages easier. 
If you do not have Jupyter install please follow this link https://jupyter.org/install and follow the steps . 
Firstly you MUST install pip for python.
The packages can be imported by using jupyter by using !pip install importname or use your cmd and just type pip install importname 
For easy access to Jupyter you can install Anaconda for Python.  
