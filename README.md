# 🧠 AI-Based Exam Paper Evaluation System

An intelligent web-based application developed using Flask and AI/NLP techniques to automatically evaluate student answer sheets and generate scores with detailed feedback.

The system helps teachers reduce manual correction work by automatically comparing uploaded student answers with answer keys and storing the results in a database for future access.

---

# 📌 Project Overview

The AI-Based Exam Paper Evaluation System is designed to automate the traditional answer sheet correction process.

Teachers can upload:
- Student Answer Sheets (PDF)
- Official Answer Keys (CSV)

The system evaluates the answers using an AI model and generates:
- Marks/Score
- Detailed Feedback
- Result History

Students can later view their results using their Student ID and Exam ID.

---

# 🚀 Features

## ✅ Teacher Features
- Upload student answer sheets
- Upload answer key CSV files
- Automatic AI evaluation
- View generated scores
- Store results permanently

## ✅ Student Features
- Search results using Student ID
- View scores instantly
- View detailed feedback

## ✅ System Features
- AI-powered answer evaluation
- SQLite database integration
- REST API support
- Error handling and validation
- Automatic database table creation
- Clean and responsive interface

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Programming |
| Flask | Web Framework |
| SQLAlchemy | Database ORM |
| SQLite | Database |
| HTML/CSS | Frontend |
| AI/NLP Model | Answer Evaluation |
| JSON | Data Handling |
| Logging | Debugging & Monitoring |

---

# 📂 Project Structure

```bash
AI-Exam-Evaluator/
│
├── app.py
├── model.py
├── database.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── login.html
│   ├── homepage.html
│   ├── index.html
│   ├── result_lookup.html
│   └── results.html
│
├── static/
│
├── instance/
│
└── uploads/