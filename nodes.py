# import csv
# import datetime
# import os
#
# class VersionUpdate:
#     def __init__(self):
#         self.csv_file = os.path.join(os.path.dirname(__file__), "node_version.csv")
#         self.version = self.read_version()
#
#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                 # No inputs required
#             },
#         }
#
#     RETURN_TYPES = ("STRING",)  # Add string output
#     RETURN_NAMES = ("version",)  # Name the output "version"
#
#     FUNCTION = "update_and_display"
#
#     OUTPUT_NODE = True
#
#     CATEGORY = "display/VersionControl"
#
#     def update_and_display(self):
#         # self.update_version()
#         self.version = self.read_version()
#         print(self.version)
#         return {"ui": {"text": self.version}, "result": (self.version,)}
#
#     def update_version(self):
#         timestamp = datetime.datetime.now().isoformat()
#         file_exists = os.path.isfile(self.csv_file)
#         with open(self.csv_file, 'a', newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             if not file_exists:
#                 writer.writerow(["Timestamp"])
#             writer.writerow([timestamp])
#
#     def read_version(self):
#         try:
#             with open(self.csv_file, 'r') as csvfile:
#                 reader = csv.reader(csvfile)
#                 next(reader)  # Skip header
#                 last_row = None
#                 for row in reader:
#                     last_row = row
#                 if last_row:
#                     return last_row[0]
#                 else:
#                     return "No version history."
#         except FileNotFoundError:
#             return "No version history."
#
#     @classmethod
#     def IS_CHANGED(cls, **kwargs):
#         return float("NaN")
#
# # A dictionary that contains all nodes you want to export with their names
# NODE_CLASS_MAPPINGS = {
#     "VersionUpdate": VersionUpdate
# }
#
# # A dictionary that contains the friendly/humanly readable titles for the nodes
# NODE_DISPLAY_NAME_MAPPINGS = {
#     "VersionUpdate": "Version Update"
# }

import csv
import datetime
import os
import json
import uuid

class VersionUpdate:
    def __init__(self):
        self.csv_file = os.path.join(os.path.dirname(__file__), "node_version.csv")
        self.version = self.read_version()
        self.node_id = str(uuid.uuid4())

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "trigger": ("BOOLEAN", {"default": False, "label_on": "Update", "label_off": "Not Update"}),
            },
        }

    RETURN_TYPES = ("STRING",)  # Add string output
    RETURN_NAMES = ("version",)  # Name the output "version"

    FUNCTION = "update_and_display"

    CATEGORY = "display/VersionControl"

    def update_and_display(self, trigger):
        if trigger:
            self.update_version()
        self.version = self.read_version()
        print(self.version)
        return {"ui": {"text": self.version}, "result": (self.version,)}

    def update_version(self):
        timestamp = datetime.datetime.now().isoformat()
        file_exists = os.path.isfile(self.csv_file)
        with open(self.csv_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(["Timestamp"])
            writer.writerow([timestamp])

    def read_version(self):
        try:
            with open(self.csv_file, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header
                last_row = None
                for row in reader:
                    last_row = row
                if last_row:
                    return last_row[0]
                else:
                    return "No version history."
        except FileNotFoundError:
            return "No version history."

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def get_node_id(self):
        return self.node_id

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "VersionUpdate": VersionUpdate
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "VersionUpdate": "Version Update"
}