
from typing import Union, Any
from src.cleaner.Saver import Saver
from threading import Thread
import pandas as pd


class Cleaner(Thread):

    default = pd.DataFrame(columns=[
        'locality',
        'type of property',
        'subtype of property',
        'price',
        'sale type',
        'number of rooms', 
        'area',
        "kitchen equipment",
        "furnished",
        "open fire",
        "terrace",
        "terrace area",
        "garden",
        "garden area",
        "surface land",
        "surface plot land",
        "number of facades",
        "swimming pool",
        "building state",
        'build year',
        'epc',
        'full adress',
        'lat',
        'lng',
        "url"
        ])

    def __init__(self, real_estate_data,province):
        """
        Receive the raw data from the Collector, clean/normalize it and
        save it.
        """
        super().__init__()
        self.province = province
        self.df = Cleaner.default.copy()

        # Append the data given to this class to the dataframe
        self.append_raw_real_estate_data(real_estate_data)

    def clean(self):
        """Clean the dataframe by applying function on columns."""

        # Clean the price
        self.df['price'] = self.df['price'].apply(lambda x: self.__normalize_price(x))

        # Clean the property subtype
        self.df['subtype of property'] = self.df['subtype of property'].apply(lambda x: self.__normalize_subtype(x))

        self.__save()

    def append_raw_real_estate_data(self, raw_data):
        """Append the raw data in the dataframe."""

        # If the data to clean is not empty
        if raw_data:

            # Append all entry to the dataset
            for entry in raw_data:

                # Check if the entry is a list with a length of 19
                if entry and type(entry) == list:
                    self.df.loc[len(self.df)] = entry

    def __save(self):
        """Call the Saver and save the dataframe into a pickle file."""
        Saver(self.df,self.province).save()

    def __normalize_price(self, price: str) -> Union[int, None]:
        if price:
            return self.string_to_int(price.replace(".", ""))

        return None

    def __normalize_subtype(self, subtype) -> Union[str, None]:
        if subtype:
            return self.__sanitize_string(subtype)

        return None

    @staticmethod
    def __sanitize_string(string: str) -> str:
        return string.strip()

    @staticmethod
    def string_to_int(x: str, default=None) -> Union[int, Any]:

        x = Cleaner.__sanitize_string(x)

        if x.isdecimal():
            return int(x)

        return default
