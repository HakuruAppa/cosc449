import sys

from ollama import Client
import pandas as pd
from tqdm import tqdm

#list of local Ollama models
model_list=[
    "gemma3:4b",
    "gemma3n:e2b",
    "gemma3n:e4b",
    "qwen3.5:4b",
    "qwen3:4b",
    "qwen3:8b",
    "llama3.2:3b",
]

#list of prompt categories
prompt_types = ["prompts.csv", "badprompts.csv"]

def query_model(client, prompts, model):
  #pull model to ollama instance
  print("Pulling model..."+model)
  client.pull(model)
  
  #List to store responses
  replies = []

  #query model for each prompt
  for prompt in tqdm(prompts,desc="Waiting for responses..."):
    #keep_alive=0 ensures model gets unloaded from memory instantly
    response = client.chat(model=model, keep_alive=0, messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])
    reply = response.message.content
    replies.append(reply)

  #return list of responses from model
  return replies  



def main():
  #initialize Ollama client
  client = Client(
    host='http://192.168.0.51:11434',
    headers={'x-some-header': 'some-value'}
  )

  #Uncomment below to manually select the model to query
  #model=model_list[1]

  #Manually select the prompt category to query
  prompt_type=prompt_types[1]

  #loading each prompt to list
  print("Loading prompts from file..."+prompt_type)
  prompts = pd.read_csv(prompt_type, usecols=['LLM Prompt'], na_values="Empty")
  prompts = prompts['LLM Prompt'].tolist()

  #Uncomment below to query specific prompts
  #prompts = prompts[1:7]

  for model in tqdm(model_list, desc="Querying models...", total=len(model_list)):
    #Get responses from model
    replies = query_model(client, prompts, model)

    #defining filename to save replies per model
    filename = ""+prompt_type.replace(".csv", "") + "_" + model.replace(":","_") + ".csv"

    #use pandas to save responses to csv file
    df = pd.DataFrame({model: replies})
    df.to_csv(path_or_buf=filename, index=False, header=False, sep="|")


if __name__ == "__main__":  sys.exit(main())