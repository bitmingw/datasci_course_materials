load("~/GitHub/datasci_course_materials/assignment5/seaflow_problem.RData")
setwd("~/GitHub//datasci_course_materials/assignment5/")

library("ggplot2")
qplot(pe, chl_small, data = plot_df, color = pop)

library("rpart")
for_obj <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(for_obj, method = "class", data = train)
print(model)

test_results <- predict(model, test, type = "class")
test_match <- test_results == test$pop
sum(test_match) / nrow(test)

library("randomForest")
model2 <- randomForest(for_obj, data = train)
print(model2)

test_results2 <- predict(model2, test, type = "class")
test_match2 <- test_results2 == test$pop
sum(test_match2) / nrow(test)
importance(model2)

library("e1071")
model3 <- svm(for_obj, data = train)
test_results3 <- predict(model3, test, type = "class")
test_match3 <- test_results3 == test$pop
sum(test_match3) / nrow(test)

table(pred = test_results, true = test$pop)
table(pred = test_results2, true = test$pop)
table(pred = test_results3, true = test$pop)

qplot(data$fsc_small, 1)
qplot(data$fsc_perp, 1)
qplot(data$fsc_big, 1)
qplot(data$pe, 1)
qplot(data$chl_small, 1)
qplot(data$chl_big, 1)

newdata <- data[data$file_id != 208,]
newtest <- newdata[sample(nrow(newdata), nrow(newdata)/2),]
new_seq <- rownames(newdata)
new_test_seq <- rownames(newtest)
new_train_seq <- new_seq[!(new_seq %in% new_test_seq)]
newtrain <- data[new_train_seq,]

new_model <- svm(for_obj, data = newtrain)
new_results <- predict(new_model, newtest, type = "class")
new_match <- new_results == newtest$pop
sum(new_match) / nrow(newtest)
