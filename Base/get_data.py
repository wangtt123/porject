import yaml, os

class Get_Data:

    def __init__(self, file_name):
        self.file_path = "./Data" + os.sep + file_name

    def return_yaml_data(self):
        with open(self.file_path, "r"，encoding=utf-8) as f:
            return yaml.load(f)