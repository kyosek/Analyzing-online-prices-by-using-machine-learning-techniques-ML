## RF
# prediction
y_pred = clf.predict(test_x)

## RF + SMOTE
# prediction
y_pred = clf_rf.predict(test_x)
# check
score = clf_rf.score(trainstome_x, trainstome_y)
print("Mean accuracy of Random Forest: {0}".format(score))
