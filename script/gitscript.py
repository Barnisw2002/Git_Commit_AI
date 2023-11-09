#!/usr/bin/env python3
import configparser
import importlib.util
import os
import subprocess
from abc import ABC, abstractmethod
import openai

config_path = ".git/script/config.ini"

def git_diff():
    try:
        diffs = subprocess.check_output(['git', 'diff', '--cached']).decode('utf-8').split('\n')
        diff = ""
        for i in range(5, len(diffs)):
            if diffs[i] and len(diffs[i]) > 0 and (diffs[i][0] == "-" or diffs[i][0] == "+"):
                diff += diffs[i] + "\n"
        return diff

    except Exception as e:
        print(f"Hiba történt a git_diff függvényben: {e}")
        exit(1)

class Git(ABC):
    def __init__(self):
        self.tmt = None
        self.GPT_version = None
        self.my_commit = None
        self.diff = None

    @abstractmethod
    def process(self):
        pass

    @staticmethod
    def load_correct_version(path, class_name):
        try:
            spec = importlib.util.spec_from_file_location(class_name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return getattr(module, class_name)()

        except Exception as e:
            print(f"Hiba történt a load_correct_version függvényben: {e}")
            files = os.listdir(path)
            allfile = ""
            for file in files:
                allfile += file + "\n"
            print(f"load_correct_version ezeket a fájlokat látja: {allfile}")
            print(f"Config ini elérés út: {path}")
            exit(1)

    def load(self):
        try:
            config = configparser.ConfigParser()
            config.read(config_path)
            openai.api_key = config.get('API', 'key')
            self.GPT_version = config.get('GPT', 'version')
            self.tmt = int(config.get('TMT', 'temperature'))
            self.my_commit = os.environ['COMMIT_MESSAGE']
            self.diff = git_diff()

        except Exception as e:
            print(f"Hiba történt a load függvényben: {e}")
            exit(1)

def parse():
    try:
        config = configparser.ConfigParser()
        config.read(config_path)
        return [config.get('VERSION', 'path'), config.get('VERSION', 'class_name')]

    except Exception as e:
        print(f"Hiba történt a parse függvényben: {e}")
        exit(1)

if __name__ == "__main__":
    arguments = parse()
    T1 = Git.load_correct_version(arguments[0], arguments[1])
    T1.load()
    T1.process()
    exit(0)
