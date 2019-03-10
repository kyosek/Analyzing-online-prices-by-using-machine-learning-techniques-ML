# RF
# AP score
rf_ap = average_precision_score(test_y, y_pred)
print('Average precision-recall score: {0:0.2f}'.format(rf_ap))
from sklearn.metrics import cohen_kappa_score

rf_kappa = cohen_kappa_score(test_y, y_pred)
print("Kappa %.2f" % rf_kappa)

# accuracy
rf_acc = accuracy_score(test_y, y_pred)
print("Accuracy = %.5f" % rf_acc)
# confusion matrix
print(confusion_matrix(test_y, y_pred))

report = classification_report(test_y, y_pred)
print(report)

# Cohen's kappa
rf_kappa = cohen_kappa_score(test_y, y_pred)
print("Kappa %.5f" % rf_kappa)