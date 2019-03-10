## load data
train = pd.read_csv('~/train.csv')
test = pd.read_csv('~/test.csv')

# encode all the categorical variables
lb_make = LabelEncoder()
train["day_code"] = lb_make.fit_transform(train["day"])
train["week_code"] = lb_make.fit_transform(train["weekofm"])
train["month_code"] = lb_make.fit_transform(train["month"])
train["season_code"] = lb_make.fit_transform(train["season"])
train["category_code"] = lb_make.fit_transform(train["category"])
train["pricecat_code"] = lb_make.fit_transform(train["pricecat"])
test["day_code"] = lb_make.fit_transform(test["day"])
test["week_code"] = lb_make.fit_transform(test["weekofm"])
test["month_code"] = lb_make.fit_transform(test["month"])
test["season_code"] = lb_make.fit_transform(test["season"])
test["category_code"] = lb_make.fit_transform(test["category"])
test["pricecat_code"] = lb_make.fit_transform(test["pricecat"])

# select columns by name
train_y = train.filter(items=['event'])
test_y = test.filter(items=['event'])
train_x = train.filter(items=['duration', 'fullprice', 'day_code', 'month_code', 'week_code', 'season_code',
                              'category_code', 'pricecat_code'])
test_x = test.filter(items=['duration', 'fullprice', 'day_code', 'month_code', 'week_code', 'season_code',
                            'category_code', 'pricecat_code'])

# time series CV
tscv = TimeSeriesSplit(n_splits=10)

# RF
clf = RandomForestClassifier(n_estimators=25, random_state=7, warm_start='True')
clf = clf.fit(train_x, train_y)
score = clf.score(train_x, train_y)
"Mean accuracy of Random Forest: {0}".format(score)

# Random forest STOME
clf_rf = RandomForestClassifier(n_estimators=25)
clf_rf.fit(trainstome_x, trainstome_y)
