from sklearn import tree

# height, weight, shoes size
X = [[181, 80, 44], [107, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
     [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# gender
Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male',
     'female', 'male', 'female', 'male']

# decision tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# decission tree regresor
reg = tree.DecisionTreeRegressor()
#reg = reg.fit(X, Y)

# deccion tree, extremely randomized
rand = tree.ExtraTreeClassifier()
rand = rand.fit(X, Y)

value = [[140,180,42]]
clf_prediction = clf.predict(value)
#reg_prediction = reg.predict(value)
rand_prediction = rand.predict(value)

print(clf_prediction)
#print(reg_prediction)
print(rand_prediction)