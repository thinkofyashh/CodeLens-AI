# API endpoints: /health, /explain-code, etc.
from fastapi import APIRouter
from backend.schema import CodeExplainRequest


router=APIRouter()



# Checking Server Status
@router.get("/health")
def checking_health():
    return {
        "status":"Ok",
        "message":"CodeLens-AI backend is running"
    }


# API for Sending Code to the LLM and recieving a respinse from it .
@router.post("/explain_code")
def explain(req:CodeExplainRequest):
    print(req)
    return {
        "message":"Request is handled Successfully . ",
        "code":req.code,
        "language":req.language,
        "level":req.level
    }
    