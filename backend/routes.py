# API endpoints: /health, /explain-code, etc.
from fastapi import APIRouter
from backend.schema import CodeExplainRequest,CodeExplainResponse
from backend.chains import explain_code_chain


router=APIRouter()



# Checking Server Status
@router.get("/health")
def checking_health():
    return {
        "status":"Ok",
        "message":"CodeLens-AI backend is running"
    }


# API for Sending Code to the LLM and recieving a respinse from it .
@router.post("/explain-code",response_model=CodeExplainResponse)
def explain(req:CodeExplainRequest):
    result=explain_code_chain.invoke({
        'code':req.code,
        'language':req.language,
        'level':req.level
    })
    return result
    