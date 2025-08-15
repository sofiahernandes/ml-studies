import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from mock_response import MOCK_TEST

load_dotenv()

MODE = os.getenv("MODE", "prod")

def upload_code(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def save_test(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def generate_test(code):
    llm = AzureChatOpenAI(
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT"),
        openai_api_type="azure",
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        temperature=0,
    )

    prompt = PromptTemplate(
        input_variables=["code"],
        template=f"""
You are a Python unit test generator.
Given the following code, generate unit tests using Pytest that cover expected cases, errors, and exceptions.
```python
{code}
```

Return only the content of the file test_*.py with the generated unit tests.
Make sure to include imports and necessary setup.
Do not include any explanations or comments.
""")

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(code)

def main():
    codigo = upload_code("code_files/sample_code.py")
    result = ""

    if MODE == "mock":
        print("Executing in MOCK mode")
        result = MOCK_TEST
    else:
        print("Executing in PROD mode with Azure OpenAI")
        result = generate_test(codigo)

    save_test(result, "generated_tests/test_sample_code.py")
    print("✅ Successfully generated test! Check the result in generated_tests/test_sample_code.py")

if __name__ == "__main__":
    main()
