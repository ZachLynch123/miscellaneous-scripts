# Program that recommends movies based on previous positive reviews
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM 

#Fetch data and format it 
data = fetch_movielens(min_rating = 4.0)

#printtraining and texting data
print (repr(data['train']))
print (repr(data['test']))

#Create model
model = LightFM(loss = 'warp')
#train
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommend(model,data,user_ids):
	n_users, n_items = data['train'].shape

	for user_id in user_ids:

		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		scores = model.predict(user_id, np.arange(n_items))

		top_items = data['item_labels'][np.argsort(-scores)]

		print("User %s" % user_id)
		print("		Known positives:")

		for x in known_positives[:3]:
			print ("				%s" % x)

		print ("		Recommended:")

		for x in top_items[:3]:
			print ("				%s" % x)

sample_recommend(model, data, [3,25,450])	



		