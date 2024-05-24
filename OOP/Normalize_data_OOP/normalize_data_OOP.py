class Normalizer:
    """
    Class to normalize and inverse normalize data using min-max scaling.

    Attributes:
        min (int): Minimum value in the data.
        max (int): Maximum value in the data.

    Methods:
        __init__(self, data): Initializes the Normalizer object with the minimum and maximum values of the data.
        transform(self, data): Scales the input data to a range between 0 and 1.
        inverse_transform(self, data): Reverts the scaled data back to its original range.
    """

    def fit(self, data):
        """
        Initializes the Normalizer object with the minimum and maximum values of the input data.
        """
        self.min = min(data)
        self.max = max(data)

    def transform(self, data):
        """
        Scales the input data to a range between 0 and 1.
        """
        return [(x - self.min) / (self.max - self.min) for x in data]

    def inverse_transform(self, data):
        """
        Reverts the scaled data back to its original range.
        """
        return [(x * (self.max - self.min) + self.min) for x in data]