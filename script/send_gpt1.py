import openai
from gitscript import Git

class V1(Git):
    def process(self):
        try:
            history = [{"role": "user", "content": f"Írj egy rövid commitot erről a módosításról:\n{self.diff}"}]
            response = openai.ChatCompletion.create(
                model=self.GPT_version,
                temperature=self.tmt,
                messages=history
            )
            answer = response['choices'][0]['message']['content']
            history.append({"role": "assistant", "content": answer})

            history.append({"role": "user", "content": f"Hasónlítsd össze ezt a két commitot 1-10 skálán. Csak egy "
                                                       f"pontszámot írj hogy a te általad írt commithoz képest "
                                                       f"mennyire hasonlít!\n'{self.my_commit}' vs '{answer}'"})
            response = openai.ChatCompletion.create(
                model=self.GPT_version,
                temperature=self.tmt,
                messages=history
            )
            answer = response['choices'][0]['message']['content']
            print(answer)
            # 0: allow commit 1: stop commit
            exit(0)

        except Exception as e:
            print(f"Hiba történt a {type(self).__name__} függvényben: {e}")
            exit(1)
