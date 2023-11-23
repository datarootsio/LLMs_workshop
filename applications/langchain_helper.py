import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain



def generate_post_dataroots(openai_api_key, temperature, social_network, position, tone, max_words, extra_info= ""):
    llm = OpenAI(temperature=temperature, openai_api_key=openai_api_key)

    my_prompt = PromptTemplate(
    input_variables = ["social_network", "position", "tone", "max_words", "extra_info"],
    input_types={
        "social_network": str,
        "position": str,
        "tone": str,
        "max_words": int,
        "extra_info": str
        },
    template = """
    You are Dataroots assistant and you are here to help HR create new posts on {social_network} to recruite new people.
    The post should be about looking for a {position}.
    The tone must be {tone}.
    The max number of words for the post should be {max_words}.

    {extra_info}
    """
    )
#Be as captivating as possible and use emojis to convey the message.
    recruitment_chain = LLMChain(llm=llm, prompt=my_prompt, output_key="generated_post")

    response = recruitment_chain({
        "social_network": social_network,
        "position": position,
        "tone": tone,
        "max_words": max_words,
        "extra_info": extra_info
    })

    return response
