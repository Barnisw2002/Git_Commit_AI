#!/usr/bin/env python3
# import sys
import configparser
import os
import subprocess
import sys
import openai
import send_gpt1
import send_gpt2


def git_diff():
    diffs = subprocess.check_output(['git', 'diff', '--cached']).decode('utf-8').split('\n')
    diff = ""
    for i in range(5, len(diffs)):
        if diffs[i] and len(diffs[i]) > 0 and (diffs[i][0] == "-" or diffs[i][0] == "+"):
            diff += diffs[i] + "\n"
    return diff


class Git:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('.git/script/config.ini')
        openai.api_key = config.get('API', 'key')
        self.GPT_version = config.get('GPT', 'version')
        self.tmt = int(config.get('TMT', 'temperature'))
        self.var = int(config.get('VAR', 'variant'))
        self.my_commit = os.environ['COMMIT_MESSAGE']
        self.diff = git_diff()

    def send_gpt1(self):
        return send_gpt1.send_gpt1(self)

    def send_gpt2(self):
        return send_gpt2.send_gpt2(self)


if __name__ == "__main__":
    T1 = Git()
    if T1.var == 0:
        if int(T1.send_gpt1()) <= 8:
            raise Exception("Commit leállítva")
    elif T1.var == 1:
        print(T1.send_gpt2())
    else:
        print(f"Rossz send verzió [{T1.var}]")
