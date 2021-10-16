
from src.cleaner.Cleaner import Cleaner
from src.cleaner.Saver import Saver

import glob
import os
import pandas as pd


class Merger:

    def __init__(self):
        """
        Merge pickle files into one CSV.
        """
        self.df = Cleaner.default.copy()

    def merge(self,province):

        # Retrieve all pickles
        for file in glob.glob(f"{Saver.real_estate_data}{province[0]}*.p"):

            pickle = pd.read_pickle(file)
            self.df = pd.concat([self.df, pickle])
            #os.remove(file)

        # Replace booleans to 0 or 1 in the CSV
        for i in ["swimming pool", "open fire", "furnished", "kitchen equipment", "garden"]:
            self.df[i] = self.df[i].apply(lambda x: self.boolean_to_byte(x))

        # Replace None to "None" (string) in the CSV
        #self.df.fillna("None", inplace=True)

        self.df.to_csv(f"./data/{province[0]}.csv")

    @staticmethod
    def boolean_to_byte(x):
        """Return 1 if x is True, 0 if its False."""

        if x == True:
            return 1
        elif x == False:
            return 0

        return None


