# Prompt templates
from langchain_core.prompts import ChatPromptTemplate
from backend.schema import CodeExplainResponse
from langchain_core.output_parsers import PydanticOutputParser

parser=PydanticOutputParser(pydantic_object=CodeExplainResponse)


system_prompt=""
with open("backend/prompt_template/system.txt",'r') as f:
    system_prompt=f.read()


code_explain_prompt=ChatPromptTemplate([
     ('system',system_prompt),
     ('human','The code provided by the user is {code} which is written in {language}. Explain the code to someone who is at a {level} level. \n{format_information}')
   ]
).partial(format_information=parser.get_format_instructions())


