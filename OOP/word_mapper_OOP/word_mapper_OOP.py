class Mapper:
    """
    This class provides methods to map words to indices and vice versa based on a given list of sentences.

    Attributes:
        bag_of_words (list): A list containing all unique words found in the input sentences.
        word_to_index (dict): A dictionary mapping words to their corresponding indices.

    Methods:
        fit(self, sentence_list): Extracts unique words from the input sentences and assigns an index to each word.
        transform(self, sentence_list): Transforms input sentences into lists of indices based on the mapping created by the fit method.
        inverse_transform(self, sentence_list_number): Converts lists of indices back to sentences using the word-to-index mapping.

    """

    bag_of_words = []
    word_to_index = {}
    
    def fit(self, sentence_list):
        """
        Extracts unique words from the input sentences and assigns an index to each word.

        Parameters:
            sentence_list (list): A list of sentences to extract words from.

        Returns:
            None
        """
        for sentence in sentence_list:
            word1 = ''.join(sentence)
            word1 = word1.lower()
            for word2 in word1.split():
                Mapper.bag_of_words.append(word2)

        Mapper.bag_of_words = set(Mapper.bag_of_words)
        Mapper.bag_of_words = list(Mapper.bag_of_words)
        Mapper.bag_of_words.sort()
        index_num = 0
        for word in Mapper.bag_of_words:
            Mapper.word_to_index[word] = index_num
            index_num += 1
    
    def transform(self, sentence_list):
        """
        Transforms input sentences into lists of indices based on the mapping created by the fit method.

        Parameters:
            sentence_list (list): A list of sentences to be transformed into indices.

        Returns:
            list: A list of lists, where each inner list contains the indices corresponding to words in the input sentences.
        """
        sentence_list_transform = []
        
        for sentence in sentence_list:
            sentence_transform = []
            word1 = ''.join(sentence)
            word1 = word1.lower()
            for word2 in word1.split():
                
                sentence_transform.append(Mapper.word_to_index[word2])
            sentence_list_transform.append(sentence_transform)
            
        return sentence_list_transform

    def inverse_transform(self, sentence_list_number):
        """
        Converts lists of indices back to sentences using the word-to-index mapping.

        Parameters:
            sentence_list_number (list): A list of lists, where each inner list contains the indices to be converted back to words.

        Returns:
            list: A list of sentences where each sentence corresponds to the indices provided in the input list.
        """
        sentence_list = []
        for sentence_num in sentence_list_number:
            sentence = []
            for num in sentence_num:
                
                for key, value in Mapper.word_to_index.items():
                    if value == num:
                        sentence.append(key)
            
            sentence = ' '.join(sentence)
            sentence_list.append(sentence)
        return sentence_list