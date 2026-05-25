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
---

# 🖥️ Frontend Interface

The system provides a simple and user-friendly interface designed for both teachers and students.

The homepage acts as a navigation portal where users can choose their role and access the appropriate module.

The frontend is developed using:
- HTML5
- CSS3
- Responsive Design Principles

---

# 🔐 User Login & Navigation System

The application contains separate access interfaces for:

- 👨‍🏫 Teachers
- 🎓 Students

This role-based navigation helps organize the system efficiently and improves usability.

---

# 👨‍🏫 Teacher Interface

The Teacher Module is designed for managing the evaluation process.

Teachers can:

- Upload student answer sheet PDFs
- Upload answer key CSV files
- Trigger AI-based evaluation
- Generate marks automatically
- View detailed feedback
- Store results in the database

The teacher dashboard simplifies the correction process and reduces manual effort.

---

# 🎓 Student Interface

The Student Module allows students to securely access their evaluation results.

Students can:

- Enter Student ID
- Enter Exam ID
- Search for their results
- View obtained score
- Access AI-generated feedback

This module provides quick and transparent result access.

---

# 🎨 User Interface Highlights

## ✅ Clean Design
The application uses a simple and professional layout for better readability.

## ✅ Responsive Interface
The interface adapts to different screen sizes and devices.

## ✅ Easy Navigation
Separate navigation paths for teachers and students improve accessibility.

## ✅ Interactive Components
Buttons and forms are styled for smooth user interaction.

## ✅ Modern Styling
The UI includes:
- Soft shadows
- Rounded corners
- Organized layouts
- Minimal color design

---

# 🔄 Workflow Navigation

```text
Homepage
   ↓
Select User Type
   ↓
Teacher Portal  → Upload Files → AI Evaluation → Store Results

OR

Student Portal → Enter Credentials → View Results
```

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



## Preview

<p align="center">
  <img 
    src="https://raw.githubusercontent.com/sharon207/sharon207/ai-driven-exam-evaluation-system\intex.png"
    width="100%"
    alt="Sharon Xavier Banner"
  />
</p>
