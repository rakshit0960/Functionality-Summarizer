
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


import ast

def extract_definitions(code):
    tree = ast.parse(code)
    functions = []
    classes = []

    # preOrder traversal of the tree
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            functions.append((node.name, ast.get_source_segment(code, node)))
        elif isinstance(node, ast.ClassDef):
            classes.append((node.name, ast.get_source_segment(code, node)))
    return functions, classes


def summarize_function(function_name, function_code):
    prompt = f"""You are a Python code documentation assistant.

Please explain the following function in **Markdown format**, following the structure below:

### Function: `{function_name}`

```python
{function_code}
```

### Summary

[Your detailed explanation here]

### Key Points
- [Point 1]

"""

    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = ""

    for stream in response:
        if stream.text is not None:
            text += stream.text
            print(stream.text, end="", flush=True)
        else:
            print("No text in stream", flush=True)
    return text

def summarize_class(class_name, class_code):
    prompt = f"""You are a code summarizer. Please explain the following class in detail using Markdown format.

### Class: `{class_name}`

```python
{class_code}
```
### Summary

[Your detailed explanation here]

### Key Points
- [Point 1]

"""

    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = ""
    
    for stream in response:
        if stream.text is not None:
            text += stream.text
            print(stream.text, end="", flush=True)
        else:
            print("No text in stream", flush=True)
    return text

def summarize_file(filepath):
    with open(filepath, "r") as file:
        code = file.read()

    functions, classes = extract_definitions(code)
    summary = []

    for name, func_code in functions:
        func_summary = summarize_function(name, func_code)
        summary.append(f"Function `{name}`:\n{func_summary}\n")

    for name, class_code in classes:
        class_summary = summarize_class(name, class_code)
        summary.append(f"Class `{name}`:\n{class_summary}\n")

    return "\n\n---\n\n".join(summary)



def save_summary(summary_text, output_path):
    with open(output_path, "w") as f:
        f.write(summary_text)


if __name__ == "__main__":
    input_path = "code.py"
    output_path = "summary.md"
    
    summary = summarize_file(input_path)
    save_summary(summary, output_path)
    print(f"Summary saved to {output_path}")




