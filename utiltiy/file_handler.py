import json
import os
from random import shuffle

SETTING_FOLDER_PATH = os.path.abspath(
    os.path.dirname(
        os.path.dirname(__file__)
        )
)


class File():
    @classmethod
    def read_json(cls, filename):
        json_path = SETTING_FOLDER_PATH + r"/data/" + filename
        with open(json_path, "r") as infile:
            data = json.load(infile)

            return data

    @classmethod
    def write_json(cls, filename, data):
        json_path = SETTING_FOLDER_PATH + r"/data/" + filename
        with open(json_path, "w") as infile:
            json.dump(data, infile)
    
    @classmethod
    def generate_data(cls, filename):
        """
        Generate training and testing data.
        """
        
        # Get all articles
        data: list[dict[str, str]] = cls.read_json(filename)
        
        # Random the order.
        shuffle(data)
        train_num = int(len(data) * 0.8)
        train_data = data[:train_num]
        test_data = data[train_num:]

        # Write to files.
        cls.write_json('train_data.json', train_data)
        cls.write_json('test_data.json', test_data)