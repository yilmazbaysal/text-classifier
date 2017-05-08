from text_classifier.code.classifier import Classifier
from text_classifier.code.text_handler import TextHandler

handler = TextHandler()

classifier = Classifier(handler.get_train_data(), handler.get_vocabulary())

print(classifier.find_sense(['ball']))
