import openai


def send_gpt1(self):
    history = [{"role": "user", "content": f"Írj egy rövid commitot erről a módosításról:\n{self.diff}"}]
    response = openai.ChatCompletion.create(
        model=self.GPT_version,
        temperature=self.tmt,
        messages=history
    )
    answer = response['choices'][0]['message']['content']
    history.append({"role": "assistant", "content": answer})
    print(answer)

    history.append({"role": "user", "content": f"Hasónlítsd össze ezt a két commitot 1-10 skálán. Csak egy "
                                               f"pontszámot írj hogy a te általad írt commithoz ké"
                                               f"pest mennyire hasonlít!\n'{self.my_commit}' vs '{answer}'"})
    # print(history)
    response = openai.ChatCompletion.create(
        model=self.GPT_version,
        temperature=self.tmt,
        messages=history
    )
    answer = response['choices'][0]['message']['content']
    return answer
