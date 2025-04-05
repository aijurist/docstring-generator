from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

#custom imports
from model import DocstringOutput
from gemini import get_gemini_api_key

class GenerateDocstring():
    def __init__(self, model_name: str, api_key: str = get_gemini_api_key()):
        self.model = GoogleGenerativeAI(model_name=model_name, api_key=api_key)
        self.output_parser = JsonOutputParser(pydantic_object=DocstringOutput)
        self.prompt_template = PromptTemplate(
            template=(
                "You are an expert technical writer and Python developer. Your task is to generate a high-quality, "
                "PEP-257-compliant docstring for the given Python code. The docstring should accurately describe "
                "the function’s purpose, parameters, return value, and any exceptions it may raise.\n\n"
                "Code:\n{code}\n\n"
                "Please follow this format:\n{format_instructions}"
            ),
            input_variables=["code"],
            partial_variables={
                "format_instructions": [self.output_parser.get_format_instructions()]
            }
        )
        self.docstring_chain = self.prompt_template | self.model | self.output_parser
    def generate_docstring(self, code: str) -> DocstringOutput:
        """
        Generate a docstring for the provided Python code using the Google Generative AI model.
        
        Args:
            code (str): The Python code for which to generate a docstring.
        
        Returns:
            DocstringOutput: The generated docstring and related information.
        """
        response = self.docstring_chain.invoke({"code": code})
        return response
        
        