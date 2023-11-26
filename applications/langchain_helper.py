import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Sequence
import pandas as pd



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
    recruitment_chain = LLMChain(llm=llm, prompt=my_prompt, output_key="generated_post")

    output = recruitment_chain({
        "social_network": social_network,
        "position": position,
        "tone": tone,
        "max_words": max_words,
        "extra_info": extra_info
    })

    return output



def generate_post_dataroots_with_parsing(openai_api_key, temperature, n_posts, social_network, position, tone, max_words, extra_info= ""):
    llm = OpenAI(temperature=temperature, openai_api_key=openai_api_key)

    
    class PostInfo(BaseModel):
        post_description: str = Field(description="This is the post")
        reasoning: str = Field(description="This is the reasons for the score")
        likelihood_of_success: int = Field(description="This is an integer score between 1-10")
        
    class Posts(BaseModel):
        posts: Sequence[PostInfo] = Field(..., description="The social media posts")

    pydantic_parser = PydanticOutputParser(pydantic_object=Posts)
    format_instructions = pydantic_parser.get_format_instructions()


    my_prompt = PromptTemplate(
    input_variables = ["n_posts", "social_network", "position", "tone", "max_words", "extra_info", "format_instructions"],
    input_types={
        "n_posts": int,
        "social_network": str,
        "position": str,
        "tone": str,
        "max_words": int,
        "extra_info": str
        },
    template = """
    You are Dataroots assistant and you are here to help HR create new posts on {social_network} to recruite new people.
    Create in total {n_posts} new posts.
    The posts should be about looking for a {position}.
    The tone must be {tone}.
    The max number of words for each post must be {max_words}.
    {extra_info}

    After crafting the new posts, rate their potential success on a scale of 1 to 10 based on how catchy and appealing they sound!
    {format_instructions}
    """
    )
    recruitment_chain = LLMChain(llm=llm, prompt=my_prompt)

    output = recruitment_chain({
        "n_posts": n_posts,
        "social_network": social_network,
        "position": position,
        "tone": tone,
        "max_words": max_words,
        "extra_info": extra_info,
        "format_instructions": format_instructions
    })
    parsed_output= pydantic_parser.parse(output["text"])
    df = pd.DataFrame([dict(obj) for obj in parsed_output.posts])
    return df
