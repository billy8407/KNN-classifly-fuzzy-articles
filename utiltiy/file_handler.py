import json
import os

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