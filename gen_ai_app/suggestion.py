import json
import dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from parser import ArrayOfDictResponseParser

OPENAI_API_KEY = dotenv.get_key(".env", "OPENAI_API_KEY")

TEMPLATE = """
You are a helpful friend of a Product Manager who generates product improvement
hypotheses.

A user will pass in two values:
- a feature context which is giving information what the general environment of the desired feature is
- a heart_category: using Google's HEART framework, it is either happiness, engagement, adoption, retention, or task_success

Come up with a product_change that is context dependent using the feature context and the product change should drive the provided heart_category.

Return 1 hypothesis in json format for each of the heart categories, so five in total.
The total response should be an array of 5 json objects.

A hypothesis is always a combination of a product change and an effect.
It follows the following logic: If we do "product change", then "improvement in HEART dimension".

Each json object has the key "hypothesis" and starts with an IF statement.
"""



class SuggestionEngine():
    system_message_prompt = SystemMessagePromptTemplate.from_template(TEMPLATE)

    def suggest(self, product_context: str) -> json:
        """
        Takes in a product context description and based with further
        instructions passes it to the LLM which should return a 
        array of dicts, where each dict is a suggested hypothesis to improve
        the product in its given context.
        """

        human_template = "product_context: {product_context}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, human_message_prompt])
        chain = LLMChain(
            llm=ChatOpenAI(openai_api_key=OPENAI_API_KEY),
            prompt=chat_prompt,
            output_parser=ArrayOfDictResponseParser()
        )
        return chain.run(product_context)