# 🚀 AI Documentation Generator

An AI-powered developer assistant that automatically generates technical documentation, README files, GitHub repository analysis, and pull request summaries using FastAPI and Groq LLMs.

---

## 📌 Features

- 📄 Generate technical documentation from source code
- 🤖 AI-generated README files
- 🔗 Analyze GitHub repositories automatically
- 📝 Summarize Pull Requests (PRs)
- 🌙 Modern dark-mode frontend UI
- 📂 Upload code files directly
- ⚡ FastAPI backend with Groq LLM integration
- 📘 Markdown-rendered documentation output

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Marked.js

### Backend
- FastAPI
- Python
- Groq API
- GitPython
- OpenAI SDK

---

## 📂 Project Structure

```text
AI-Documentation-Generator/
│
├── main.py
├── index.html
├── .env
├── .gitignore
├── requirements.txt
└── temp_repo_*
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Documentation-Generator.git
```

### 2. Open Project Folder

```bash
cd AI-Documentation-Generator
```

### 3. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

---

### 6. Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### 7. Open Frontend

Open `index.html` in your browser.

---

## 📘 API Endpoints

### Generate Documentation

```http
POST /generate-docs
```

#### Request

```json
{
  "code": "def add(a,b): return a+b"
}
```

---

### Analyze GitHub Repository

```http
POST /analyze-repo
```

#### Request

```json
{
  "repo_url": "https://github.com/pallets/flask"
}
```

---

### Summarize Pull Request

```http
POST /summarize-pr
```

#### Request

```json
{
  "diff": "+ Added JWT auth"
}
```

---

## 🧠 How It Works

```text
User Input
    ↓
Frontend UI
    ↓
FastAPI Backend
    ↓
Groq LLM API
    ↓
AI Generated Documentation
```

---

## 🌟 Future Improvements

- Authentication system
- Documentation history
- Export README.md
- Architecture diagram generation
- Multi-language code support
- Deployment to Vercel/Render

---

## 📸 Demo Features

✅ Code Documentation  
✅ README Generation  
✅ GitHub Repository Analysis  
✅ Pull Request Summarization  
✅ Markdown Rendering  

---

## 🤝 Contributing

Contributions are welcome!

Fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built for hackathons and developer productivity using AI + FastAPI + Groq.
