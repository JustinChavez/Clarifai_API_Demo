# Introduction

Welcome! This is meant to be a guide to introduce develeopers to machine learning through the Clarifai API. We will be using version V2 of Clarifai's API since it enables training of models.

# Installation

## Clarifai account. 

This is the site where the information on V2 of their API can be found: https://developer-preview.clarifai.com/

Please log into your developer account on the site (If you do not have an account you can easily create one on their site by clicking sign-up).

On the account homepage, create an application with a name of your choosing. Keep the default options.

![Alt text](/Images/Create_New_Application.png)

Take note of the Client ID and the Client secret. We need them for the API.

![Alt text](/Images/Client_Info.png)

## Developer tools

Use this tutorial to learn how to set up Python and a text editor: https://learnpythonthehardway.org/book/ex0.html

Download the clarifai library either through pip

```
pip install clarifai
```
or github:
-Download this repository as a zip file: https://github.com/Clarifai/clarifai-python
-Unzip in your working repository
-run setup.py
```
python setup.py
```
# Applications

There are three main applications of the API in V2:

-Predict
-Search
-Train

## Predict

We can use the prediction function to predict the concepts an image contains.
```
from clarifai import rest
from clarifai.rest import ClarifaiApp

CLARIFAI_APP_ID = "<Your_Client_ID>"
CLARIFAI_APP_SECRET = "<Your_Client_Secret>"
app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)
```
Be sure to replace <Your_Client_ID> and <Your_Client_Secret> with your Client ID and Secret from the application you created on the Clarifai's developer site.


We will be using the general model to predict concepts in the image

```
model = app.models.get("general-v1.3")
```
Find an image online. Copy and paste the url to the image below. 
```
result = model.predict_by_url(url="<Your_Url_to_the_Image>")
```
What is returned is a JSON object that contains information about the request to the API that was just processed. Use the following code to neatly print the concepts predicted by the image along with their calculated probability of being within the image.
```
concept_list = result["outputs"][0]["data"]["concepts"]
for concept in concept_list:
    print(str(concept["value"]) + "\t"+ concept["name"])
```
There is other information that is contained in the JSON object which you can parse for. It is pretty simple to create parses of your own once you get a hang of how the syntax works. I recommend using a JSON viewer to help like (http://jsonviewer.stack.hu/). 

## Search

To set up Search we again import the Clarifai app.
```
from clarifai import rest
from clarifai.rest import ClarifaiApp

CLARIFAI_APP_ID = "<Your_Client_ID>"
CLARIFAI_APP_SECRET = "<Your_Client_Secret>"
app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)
```

We need to now upload an image from a url that we want to be tagged by the general model and stored. We can use this cute photo of a puppy.
```
app.inputs.create_image_from_url("https://samples.clarifai.com/puppy.jpeg")
```
Now Clarifai stores the photo we just uploaded. Like how we used the general model to predict concepts on the photo, storing the photo did the just the same in addition to storing the concepts that were predicted to be associated with the photo.


We can use there predicted concepts to search through our stored photos for the a specific photo by using a concept that you predict is within or related to the photo. Say we wanted a nice photo of a dog, we could use the search function and find images that contain or are related to dogs with the following statement below:
```
result = app.inputs.search_by_predicted_concepts(concept='dog')
```

Use the following to show the images that stored images that are related to the concept of dog.
```
for concept in result:
    print (concept.url)
```
## Train

The general model contains concepts that it can predict are within a given photo. The model needed to be trained on what these concepts look like in order to work. The Train function of the API gives us the ability to train on our own set of concepts to make models as specfic and general as we like.

Again, to set up Search we again import the Clarifai app.
```
from clarifai import rest
from clarifai.rest import ClarifaiApp

CLARIFAI_APP_ID = "<Your_Client_ID>"
CLARIFAI_APP_SECRET = "<Your_Client_Secret>"
app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)
```
Say we want to train a model that identifies cute dogs and cute cats. First we need to provide examples of what a cute dog and cat look like to the model. Use the following commands to load photos of the cute dog and cat to Clarifai

```
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog2.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])

app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat1.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])
app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat2.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])
```

Lets use the following commands to name create a model and identify the concepts it will be train with.
```
model = app.models.create(model_id="pets", concepts=["cute cat", "cute dog"])
```
Now retrieve and train the model
```
model = app.models.get("pets")
model.train()
```

Let's test out our model! We can use the following to predict the concepts contained in the image with the model we just trained.
```
result = model.predict_by_url(url="https://samples.clarifai.com/dog3.jpeg")

for concept in result['outputs'][0]['data']['concepts']:
    print(concept["name"])
    print(concept["value"])
```






