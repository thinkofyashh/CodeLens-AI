# CodeLens AI

**CodeLens AI** is an AI-powered Code Explainer API built with **FastAPI**, **Pydantic**, and **LangChain**.  
It helps users understand code by generating simple explanations, line-by-line breakdowns, bug analysis, improvement suggestions, and time/space complexity insights.

This project is designed as a beginner-friendly AI backend project for learning how to build real-world AI APIs.

---

## Features

- Explain code in simple language
- Generate line-by-line code explanation
- Detect possible bugs or issues
- Suggest code improvements
- Explain time and space complexity
- Support multiple explanation levels: beginner, intermediate, and advanced
- Return structured JSON responses
- Easy to test using Swagger UI

---

## Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **LangChain**
- **OpenAI / Gemini API**
- **Uvicorn**
- **Python Dotenv**

---

## Project Structure

```txt
codelens-ai-api/
│
├── main.py
├── schemas.py
├── prompts.py
├── chains.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## API Endpoints

```txt
GET  /health
POST /explain-code
POST /find-bugs
POST /optimize-code
POST /explain-complexity
```

---

## Sample Request

```json
{
  "language": "cpp",
  "code": "for(int i = 0; i < n; i++) { cout << i; }",
  "level": "beginner"
}
```

---

## Sample Response

```json
{
  "summary": "This code prints numbers from 0 to n-1.",
  "line_by_line_explanation": [
    "The loop starts with i = 0.",
    "The loop continues while i is less than n.",
    "After every iteration, i is increased by 1.",
    "The value of i is printed in each iteration."
  ],
  "time_complexity": "O(n)",
  "space_complexity": "O(1)",
  "possible_bugs": [],
  "improvements": [
    "Add a newline after printing each number for better readability."
  ]
}
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/codelens-ai-api.git
cd codelens-ai-api
```

### 2. Create a Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

For Windows:

```bash
python -m venv myenv
myenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Or, if you are using Gemini:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

The API will start at:

```txt
http://127.0.0.1:8000
```

Swagger UI will be available at:

```txt
http://127.0.0.1:8000/docs
```

---

## Example Use Cases

- Students learning DSA and programming
- Developers reviewing unfamiliar code
- Beginners trying to understand syntax and logic
- Interview preparation
- Code documentation assistance
- Debugging and optimization practice

---

## Roadmap

- [ ] Add `/health` endpoint
- [ ] Add `/explain-code` endpoint
- [ ] Add LangChain prompt template
- [ ] Add structured output parser
- [ ] Add bug detection endpoint
- [ ] Add complexity analyzer endpoint
- [ ] Add support for multiple programming languages
- [ ] Add frontend using React
- [ ] Add authentication
- [ ] Deploy API on Render / Railway / AWS

---

## What I Will Learn From This Project

- How to build AI-powered APIs using FastAPI
- How to design request and response schemas using Pydantic
- How to use LangChain prompts, models, chains, and output parsers
- How to structure a backend AI project
- How to return reliable structured responses from LLMs
- How to write clean documentation for GitHub

---

## Author

**Yash Rawat**

GitHub: [@thinkofyashh](https://github.com/thinkofyashh)

---

## License

This project is open-source and available under the MIT License.
