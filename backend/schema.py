# Pydantic request/response models


from pydantic import BaseModel,Field
from typing import Literal,List



class CodeExplainRequest(BaseModel):
    code:str=Field(...,description="Code User Submitted .")
    language:Literal["cpp","python","javascript"]=Field(...,description="Programming Language of the code")
    level:Literal["beginner","intermediate","advanced"]=Field(description="Level of Explanation asked by User",default='beginner')

class ComplexityCode(BaseModel):
    space:str=Field(...,description="Space Complexity of the User Code .")
    time:str=Field(...,description="TIme Complexity of the User Code .")


class CodeExplainResponse(BaseModel):
    summary:str=Field(...,description="Summary of the Code you have Written . ")
    step_by_step:List[str]=Field(...,description="Explaining the User Code Line by line")
    complexity:ComplexityCode
    bugs:List[str]=Field(description="Contains the list of the Bugs .",default_factory=list)
    improvements:List[str]=Field(description="Contains the List for the imporvment of the code.",default_factory=list)
