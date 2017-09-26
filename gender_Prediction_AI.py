#Using the sklearn Machine Learning library and Regression learning model
#Predict the gender based on past height, weight, and shoe size 
#Of precious arrays with their cooresponding gender

from sklearn import tree

#[height(in inches), weight, shoe size]
x = [[180,250,12],[160,125,7.5],[160,130,6],[154, 154, 6], 
	[166, 200,10], [190,190,13], [175, 164, 8],[177,150,8.5], [159,155,11],
	[171,155,8], [181,185,11.5]]

y = ['male','female', 'female','female', 'male', 'male', 
	'male', 'female', 'male','female','male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([160, 130, 9])

print(prediction) 