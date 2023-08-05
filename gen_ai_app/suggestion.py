from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
import json
import dotenv

OPENAI_API_KEY = dotenv.get_key(".env", "OPENAI_API_KEY")

class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str) -> list[dict[str, str]]:
        """Parse the output of an LLM call."""
        return json.loads(text)

template = """
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
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    def suggest(self, product_context: str) -> json:

        human_template = "product_context: {product_context}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, human_message_prompt])
        chain = LLMChain(
            llm=ChatOpenAI(openai_api_key=OPENAI_API_KEY),
            prompt=chat_prompt,
            output_parser=CommaSeparatedListOutputParser()
        )
        return chain.run(product_context)