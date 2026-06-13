# API endpoints: /health, /explain-code, etc.
from fastapi import APIRouter

router=APIRouter()



@router.get("/")
def greeting():
    return "hello world"



# Checking Server Status
@router.get("/health")
def checking_health():
    return {
        "status":"Ok",
        "message":"CodeLens-AI backend is running"
    }

# API for Sending Code to the LLM and recieving a respinse from it .
@router.post("/explain_code")
def explain():
    # Write a logic
    return {
        "Message":"Explain code logic API under construction ."
    }