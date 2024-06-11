from langchain_openai import ChatOpenAI

def load_model(t, token_limit):

    model_name = "TechxGenus/Meta-Llama-3-70B-Instruct-AWQ"
    # model_name = "Qwen/CodeQwen1.5-7B-Chat"

    base_url = "http://pyxis.ics.uci.edu:49999/v1"
    model = ChatOpenAI(
                model=model_name,
                temperature=t,
                api_key="lm-studio",
                base_url=base_url,
                max_tokens=token_limit
            )
    
    # output_parser = StrOutputParser()
    # chain = model | output_parser
    return model