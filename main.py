import Processing as Processing
import Classification as Classifier


processing = Processing.Processing()

processing.__init__()

data, answer, valData, valAnswer = processing.clean()

classifier = Classifier.Classifaction()

classifier.__init__()

classifier.training(data, answer, valData, valAnswer)



