#encoding: utf-8
import os
import os.path

import task


class TrainData:
    def __init__(self, train_inputs, train_targets):
        self.train_inputs = train_inputs
        self.train_targets = train_targets


class TestData:
    def __init__(self, test_inputs, test_targets):
        self.test_inputs = test_inputs
        self.test_targets = test_targets


def get_files(file_directory_name):
    file_directory_path = os.path.join(task.DATA_HOME, file_directory_name)
    files = os.listdir(file_directory_path)
    waves = []
    names = []
    for file in files:
        if task.AUDIO_EXT in file:
            names.append(file)
            waves.append(os.path.join(os.path.join(task.DATA_HOME, file_directory_name, file)))
            if len(waves) >= task.AUDIO_NUM:
                break
    return waves, names

