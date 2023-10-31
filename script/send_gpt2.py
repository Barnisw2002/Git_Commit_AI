import os
import sys

import openai


def send_gpt2(self):
    msg = [{"role": "user", "content": f"Értékel egy 1-10 skálán ezt a commit üzenetet. Válaszodban csak egy szám "
                                       f"legyen: {self.my_commit}\n{self.diff}"}]
    response = openai.ChatCompletion.create(
        model=self.GPT_version,
        temperature=self.tmt,
        messages=msg
    )
    answer = response['choices'][0]['message']['content']
    return answer