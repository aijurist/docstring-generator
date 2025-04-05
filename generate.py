from docstring import GenerateDocstring
import json

docstring = GenerateDocstring(model_name="gemini-2.0-flash")
res = docstring.generate_docstring(
    code="""def add(a, b):
                return a + b
""")

print(json.dumps(res["docstring"], indent=4))