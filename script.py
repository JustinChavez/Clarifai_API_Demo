from clarifai import rest
from clarifai.rest import ClarifaiApp

#USE THIS FOR DEMO
#CLARIFAI_APP_ID =  <API_ID>
#CLARIFAI_APP_SECRET = <API_SECRET>
#app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)

#USE THIS FOR BUILDING THE DEMO
with open('keys.txt', 'r') as f:
	keys = [line.strip() for line in f]

CLARIFAI_APP_ID =  <API_ID>
CLARIFAI_APP_SECRET = <API_SECRET>
app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)



#PREDICT
# get the general model
#JLC: The convolutional neural network of Clarifai can see concepts
#based on the model you give it. The general model will see general concepts
#like "dog" or "food". If you want a more specific concept to be recognized
#for example "pasta" instead of just food, you would use the corresponding model
#like the food model.
#model = app.models.get("general-v1.3")

#How to predict with the model
##result = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

#how to get the input
#print(result["outputs"][0]["input"])

#JLC: The api will return a JSON object. Within the JSON Object are
#the 20 concepts the API calculates are contained within the image.
#The concepts are listed with the probablility that they are 
#contained within the image.
##concept_list = result["outputs"][0]["data"]["concepts"]
##for concept in concept_list:
##	print(str(concept["value"]) + "\t"+ concept["name"])

#JLC: add more image examples for the demo






#SEARCH


# before search, first need to upload a few images
#JLC: Only upload an image once. If you upload the same image multiple
#time you will get a 400 error
#app.inputs.create_image_from_url("https://samples.clarifai.com/metro-north.jpg")

# search by predicted concept
##result = app.inputs.search_by_predicted_concepts(concept='dog')
#JLC:use the following to look at all the variables that are in the object
#Note: the API might return more than one image.
#print(vars(result[0]))
##print(result[0].url)

for key in erw:
	print
#Train
#JLC: emphasize the variabilities in the image. Use examples like 2 vs 10 images trained
#or training with different ang;es/variability vs training with similar images (may train on 
#a different concept than intedned)
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog2.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])

app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat1.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])
app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat2.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])


#model = app.models.create(model_id="pets", concepts=["cute cat", "cute dog"])

model = app.models.get("pets")
model.train()

# predict with samples
result = model.predict_by_url(url="https://samples.clarifai.com/dog3.jpeg")
#b =  model.predict_by_url(url="https://samples.clarifai.com/cat3.jpeg")

for concept in result['outputs'][0]['data']['concepts']:
	#prints name of concept
	print(concept["name"])
	#prints probability of the concept above
	print(concept["value"])

