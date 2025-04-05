from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from docstring import GenerateDocstring
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DocStringRequest(BaseModel):
    code: str

@app.post("/generate-docstring/")
async def generate_docstring(request: DocStringRequest):
    try:
        docstring_generator = GenerateDocstring(model_name="gemini-2.0-flash")
        result = docstring_generator.generate_docstring(code=request.code)
        return {"data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)