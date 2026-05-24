import git
import os
import uuid
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

class CodeInput(BaseModel):
    code: str

@app.get("/")
def home():
    return {
        "message": "AI Documentation Generator Backend Running"
    }

@app.post("/generate-docs")
async def generate_docs(data: CodeInput):

    
    prompt = f"""
You are a senior software engineer.

Analyze this codebase and generate a professional README.md file.

Include:

# Project Title

# Project Overview

# Features

# Installation

# Usage

# API Endpoints (if present)

# Folder Structure Explanation

# Technologies Used

# Example Usage

Code:

{data.code}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "documentation": response.choices[0].message.content
    }

class RepoInput(BaseModel):
    repo_url: str

class PRInput(BaseModel):
    diff: str

@app.post("/analyze-repo")
async def analyze_repo(data: RepoInput):

    try:

        import uuid

        repo_path = f"temp_repo_{uuid.uuid4().hex}"

        # Clone repo
        git.Repo.clone_from(
            data.repo_url,
            repo_path
        )

        code_content = ""

        # Read files
        for root, dirs, files in os.walk(repo_path):

            for file in files:

                if file.endswith((".py", ".js", ".java")):

                    file_path = os.path.join(root, file)

                    try:

                        with open(
                            file_path,
                            "r",
                            encoding="utf-8"
                        ) as f:

                            code_content += (
                                f"\n\nFILE: {file}\n"
                            )

                            code_content += f.read()

                    except:
                        pass

        # Limit content size
        code_content = code_content[:12000]

        prompt = f"""
        Analyze this GitHub repository and generate:

        - Project Overview
        - Features
        - Installation
        - Usage
        - Technologies Used
        - API Endpoints if present

        Repository Code:

        {code_content}
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return {
            "documentation":
            response.choices[0].message.content
        }

    except Exception as e:

        return {
            "error": str(e)
        }
    
@app.post("/summarize-pr")
async def summarize_pr(data: PRInput):

    try:

        prompt = f"""
        Analyze this pull request diff and summarize it.

        Diff:

        {data.diff}
        """

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return {
            "summary":
            response.choices[0].message.content
        }

    except Exception as e:

        return {
            "error": str(e)
        }