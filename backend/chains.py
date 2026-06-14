# LangChain chains / AI workflow logic
from backend.llm_model import model
from backend.prompts import code_explain_prompt,parser


explain_code_chain=code_explain_prompt | model | parser