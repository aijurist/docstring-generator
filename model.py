from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class DocstringOutput(BaseModel):
    """
    Model for the output of a docstring generation request.
    """
    docstring: str = Field(None, description="Generated docstring")
    code: str = Field(None, description="Code snippet for which the docstring was generated")
    errors: Optional[List[str]] = None

    @classmethod
    def from_response(cls, response: Dict[str, Any]) -> "DocstringOutput":
        """
        Create a DocstringOutput instance from the API response.
        """
        return cls(
            docstring=response.get("docstring"),
            code=response.get("code"),
            errors=response.get("errors")
        )