from text_classifier.code.classifier import Classifier
from text_classifier.code.text_handler import TextHandler

handler = TextHandler()

classifier = Classifier(handler.get_train_data(), handler.get_vocabulary())


f = open('output.txt', 'w')

index = 1
test_instance_count = 5
for test_id, test_instance in handler.get_test_data():
    # Find the class
    probability, category = classifier.find_class(test_instance)

    # Print the results to both console and a file
    print('{0} -> {1}'.format(test_id, category))
    f.write('{0} -> {1}\n'.format(test_id, category))

    # To print more beautifully
    if index % test_instance_count == 0:
        print()
        f.write('\n')
    index += 1
