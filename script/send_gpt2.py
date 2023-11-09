import openai
from gitscript import Git


class V2(Git):
    def process(self):
        try:
            msg = [
                {"role": "user",
                 "content": f"Értékel egy 1-10 skálán ezt a commit üzenetet. Válaszodban csak egy szám "
                            f"legyen: {self.my_commit}\n{self.diff}"}]
            response = openai.ChatCompletion.create(
                model=self.GPT_version,
                temperature=self.tmt,
                messages=msg
            )
            answer = response['choices'][0]['message']['content']
            print(answer)
            # 0: allow commit 1: stop commit
            exit(0)

        except Exception as e:
            print(f"Hiba történt a {type(self).__name__}-ben: {e}")
            exit(1)