from text_classifier.code.classifier import Classifier
from text_classifier.code.text_handler import TextHandler

handler = TextHandler()

classifier = Classifier(handler.get_train_data(), handler.get_vocabulary())

for test_id, test_instance in handler.get_test_data():
    print(test_id, '->', classifier.find_sense(test_instance))
