
from threading import Thread
from random import sample
from string import digits
import pickle



class Saver(Thread):

    path = "./backup/"
    url_directory = "./backup/url_directory/"
    real_estate_data = "./backup/real_estate_data/"

    def __init__(self, element,province):
        """
        Save a given dataframe into a randomly named Pickle file.

        :param dataframe: A pandas Dataframe containing real estate data.
        """

        super().__init__()
        self.element = element
        self.province = province

    def save(self):
        """Save the self.dataframe into a Pickle file."""

        # Randomize the name.
        filename = "".join(sample(digits, 10))
        if self.is_list():
            with open(f"{Saver.url_directory}{filename}.p", 'wb') as f:
                pickle.dump(self.element, f)
        else:


            # Save the file in "./backup/".
            self.element.to_pickle(f"{Saver.real_estate_data}{self.province[0]}-{filename}.p", compression='infer', protocol=4)

    def is_list(self):
        if type(self.element) == list:
            return True

        return False
