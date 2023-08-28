library(titanic)
head(titanic_train)

## DROP NA (missing values)
titanic_train <- na.omit(titanic_train)
nrow(titanic_train)

## SPLIT DATA
set.seed(42)
n <- nrow(titanic_train)
id <- sample(1:n, size = n * 0.7) ## 70% train 30% test
train_data <- titanic_train[id, ]
test_data <- titanic_train[-id, ]

## Train Model for 'survived'
model_survived <- glm(survived ~ pclass, data = train_data, family = "binomial")

## Test Model for 'survived'
predictions_survived <- predict(model_survived, newdata = test_data, type = "response")
binary_predictions_survived <- ifelse(predictions_survived > 0.5, 1, 0)

## Compare predictions to actual outcomes
actual_survived <- test_data$survived
correct_predictions_survived <- binary_predictions_survived == actual_survived

## Calculate Accuracy for 'survived' predictions
accuracy_survived <- mean(correct_predictions_survived)
cat("Survived Accuracy:", accuracy_survived, "\n")
