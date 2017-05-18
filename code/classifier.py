from math import log2


class Classifier:
    def __init__(self, train_data, vocabulary):
        self.train_data = train_data
        self.vocabulary = vocabulary
        self.V = len(vocabulary)
        self.instance_count = sum([len([self.train_data[key]]) for key in self.train_data.keys()])

    def find_sense(self, test_data):
        """
        :param test_instance: A string which contains the tagged word
        :return: Calculated sense id of the word
        """
        maximum = (float("-inf"), "")  # (Probability, Sense ID)
        for sense_id in self.train_data.keys():
            instance_word_counts = 0
            for instance_id in self.train_data[sense_id].keys():
                instance_word_counts += sum(self.train_data[sense_id][instance_id].values())

            probability = log2(len(self.train_data[sense_id]) / self.instance_count)  # class_count / total_class_count
            for token in test_data:
                if token in self.vocabulary:
                    token_count = 0
                    for instance_id in self.train_data[sense_id].keys():
                        token_count += self.train_data[sense_id][instance_id][token]

                    probability += log2(((token_count + 1) / (instance_word_counts + self.V)))

            if probability > maximum[0]:
                maximum = (probability, sense_id)

        print(maximum)

        return maximum[1]