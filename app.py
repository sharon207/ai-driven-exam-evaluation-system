from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import logging
import json
from model import evaluate_student_answer
from database import db, ExamResult


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam_results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

logging.basicConfig(level=logging.DEBUG)

@app.before_request
def create_tables():
    db.create_all()

def cleanup_file(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        logging.error(f"Error deleting file {file_path}: {e}")

@app.route('/')
def index():
    return render_template("login.html")  

@app.route('/index.html')
def teacher():
    return render_template("index.html")

@app.route('/student')
def student():
    return render_template("result_lookup.html")

@app.route("/login", methods=["POST", "GET"])
def homepage1():
    print("working")
    return render_template("homepage.html")   

@app.route('/submit', methods=['POST'])
def submit():
    try:
       
        student_id = request.form['student_id']
        exam_id = request.form['exam_id']
        
       
        logging.debug(f"Received submission from student ID: {student_id}, exam ID: {exam_id}")
        
        student_pdf = request.files['student_pdf']
        answers_csv = request.files['answers_csv']

        #new addtn
        # Check if the files are properly uploaded
        if not student_pdf or not answers_csv:
            raise ValueError("One or both files are missing.")



        
        student_pdf_path = 'temp_student_answer.pdf'
        answers_csv_path = 'temp_answers.csv'
        
        student_pdf.save(student_pdf_path)
        answers_csv.save(answers_csv_path)
        
        logging.debug(f"Saved files to {student_pdf_path} and {answers_csv_path}")
        
        score, feedback = evaluate_student_answer(student_pdf_path, answers_csv_path)
        
         #new addtn 
        for item in feedback:
            item['score'] = float(item['score'])

        cleanup_file(student_pdf_path)
        cleanup_file(answers_csv_path)

        logging.debug(f"Evaluation completed: Score = {score}, Feedback = {feedback}")
        
        exam_result = ExamResult(
            student_id=student_id,
            exam_id=exam_id,
            score=float(score), #newfloat()
            feedback=feedback,   #new,
        )
        
        db.session.add(exam_result)
        db.session.commit()
        
        logging.debug(f"Results saved to database with ID: {exam_result.id}")
        
        return redirect(url_for('view_result', student_id=student_id, exam_id=exam_id))
    
    except Exception as e:
        logging.error(f"Error processing submission: {str(e)}") #newstr()
        return "An error occurred while processing the files. Please try again.", 500

@app.route('/results/<student_id>/<exam_id>')
def view_result(student_id, exam_id):
    try:
        result = ExamResult.query.filter_by(
            student_id=student_id,
            exam_id=exam_id
        ).order_by(ExamResult.created_at.desc()).first()
        
        if not result:
            return "No results found for this student and exam.", 404
        
        return render_template('results.html', score=result.score, feedback=result.feedback)
        
    except Exception as e:
        logging.error(f"Error retrieving results: {e}") 
        return "An error occurred while retrieving the results. Please try again.", 500

@app.route('/api/results/<student_id>/<exam_id>')
def get_result_api(student_id, exam_id):
    try:
        result = ExamResult.query.filter_by(
            student_id=student_id,
            exam_id=exam_id
        ).order_by(ExamResult.created_at.desc()).first()
        
        if not result:
            return jsonify({"error": "No results found"}), 404
        
        return jsonify({
            "student_id": result.student_id,
            "exam_id": result.exam_id,
            "score": result.score,
            "feedback": result.feedback,
            "timestamp": result.created_at.isoformat()
        })
        
    except Exception as e:
        logging.error(f"Error retrieving results via API: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)