import os
import openai
# import gradio as gr

#when we have OpenAI API key as an environment variable = 
#openai.api_key = os.getenv("OPENAI_API_KEY")

# key as string=
# openai.api_key = os.getenv("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")
openai.api_key = "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"


# start_sequence = "Chatbot:"
# restart_sequence = "User: "


def chatgpt_clone(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    # stop=[" User:", " Chatbot:"]
    )
    return response.choices[0].text

prompt = input()
out = chatgpt_clone(prompt)
print(out)
# def Output(input,history):
#     s = list(sum(history, ()))
#     s.append(input)
#     inp = ' '.join(s)
#     output = chatgpt_clone(inp)
#     history.append((input, output))
#     return output

# history = []
# input = input()
# Result = Output(input,history)
# print(Result)


# def chatgpt_clone(input, history):
#     history = history or []
#     s = list(sum(history, ()))
#     s.append(input)
#     inp = ' '.join(s)
#     output = openai_create(inp)
#     history.append((input, output))
#     return history, history
    



