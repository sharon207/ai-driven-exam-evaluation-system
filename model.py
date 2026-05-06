
# import pdfplumber
# import pandas as pd
# from textblob import TextBlob
# import re

# def evaluate_student_answer(student_pdf_path, answers_csv_path):
#     # Read the correct answers from the CSV file
#     qa_data = pd.read_csv(answers_csv_path)
#     correct_questions = qa_data['Question'].tolist()
#     correct_answers = qa_data['Answer'].tolist()

#     # Extract student answers from the PDF file
#     student_text = ""
#     with pdfplumber.open(student_pdf_path) as pdf:
#         for page in pdf.pages:
#             student_text += page.extract_text() + " "

#     # Clean and correct the text
#     student_text = clean_text(student_text)
#     student_text = correct_spelling(student_text)

#     # Process the student answers
#     student_qas = process_student_answers(student_text)
    
#     # Call the model and compute score and feedback
#     score, feedback = process_model(correct_questions, correct_answers, student_qas)
    
#     return score, feedback


# def clean_text(text):
#     text = text.replace("(cid:415)", "").replace("  ", " ").strip()
#     return text


# def correct_spelling(text):
#     blob = TextBlob(text)
#     return str(blob.correct())


# def process_student_answers(text):
#     # This function will extract questions and answers from the text
#     student_qas = []
#     current_q = ""
#     current_a = ""
    
#     for line in text.split("\n"):
#         line = line.strip()
#         if line.startswith("Q."):
#             if current_q and current_a:
#                 student_qas.append((current_q, current_a))
#             current_q = line[2:].strip()
#             current_a = ""
#         elif line.startswith("A."):
#             current_a = line[2:].strip()
#         else:
#             current_a += " " + line.strip()

#     if current_q and current_a:
#         student_qas.append((current_q, current_a))
    
#     return student_qas


# def extract_key_points(text):
#     """
#     Extracts key points from the correct answer by splitting at commas, 'and', 'or', etc.
#     This helps break down longer answers into meaningful segments.
#     """
#     key_points = re.split(r',|\band\b|\bor\b', text)
#     key_points = [point.strip() for point in key_points if len(point.split()) > 1]
#     return key_points


# def check_key_points(correct, student):
#     """
#     Compares the key points of the correct answer to the student's answer.
#     Returns the missing key points and the match ratio.
#     """
#     key_points = extract_key_points(correct)
#     missing_points = []
#     score_contribution = 0

#     for point in key_points:
#         words = point.split()
#         match_count = sum(1 for word in words if word.lower() in student.lower())
        
#         # Calculate score contribution for this key point based on how much of it was matched
#         match_ratio = match_count / len(words)
        
#         if match_ratio < 0.5:  # Less than 50% match = missing key point
#             missing_points.append(point)
        
#         score_contribution += match_ratio

#     return key_points, missing_points, score_contribution / len(key_points)  # Return the match ratio


# def adjust_score_for_key_points(correct_answer, student_answer):
#     """
#     Adjust the score based on the proportion of key points matched.
#     """
#     key_points, missing_points, match_ratio = check_key_points(correct_answer, student_answer)

#     if match_ratio == 1.0:  # All key points matched
#         return 1.0, "Correct"
#     elif match_ratio > 0.5:  # Partial match (more than 50% of key points matched)
#         return match_ratio, f"Partially Correct. You missed some key points like: {', '.join(missing_points)}."
#     else:  # Little or no match
#         return match_ratio, f"Incomplete answer. You missed key points like: {', '.join(missing_points)}."


# def evaluate_one_word_answer(correct, student):
#     """
#     Evaluates a one-word answer by checking exact match.
#     """
#     if correct.strip().lower() == student.strip().lower():
#         return 1.0, "Correct answer!"
#     else:
#         return 0.0, "Incorrect answer. Try again."


# def process_model(correct_questions, correct_answers, student_qas):
#     total_score = 0
#     feedback = []
#     total_possible_score = len(correct_questions)  # Total questions, for calculating percentage

#     # Loop through the student answers and compare them with the correct answers
#     for idx, (student_question, student_answer) in enumerate(student_qas):
#         correct_answer = correct_answers[idx]
        
#         # Check if the answer is one-word
#         if len(correct_answer.split()) == 1 and len(student_answer.split()) == 1:
#             # Use one-word answer evaluation (exact match only)
#             score_part, feedback_part = evaluate_one_word_answer(correct_answer, student_answer)
#             total_score += score_part
#             feedback.append({
#                 'question': correct_questions[idx],
#                 'student_answer': student_answer,
#                 'correct_answer': correct_answer,
#                 'status': feedback_part,
#                 'score': score_part
#             })
#         else:
#             # For longer answers, check key points and similarity
#             score_part, feedback_part = adjust_score_for_key_points(correct_answer, student_answer)
            
#             total_score += score_part
#             feedback.append({
#                 'question': correct_questions[idx],
#                 'student_answer': student_answer,
#                 'correct_answer': correct_answer,
#                 'status': feedback_part,
#                 'score': score_part
#             })

#     # Calculate overall score as a percentage
#     final_score = (total_score / total_possible_score) * 100
    
#     return final_score, feedback





# import pdfplumber
# import pandas as pd
# from textblob import TextBlob
# import re
# from sentence_transformers import SentenceTransformer
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

# # Load SentenceTransformer model
# model = SentenceTransformer('all-MiniLM-L6-v2')

# def evaluate_student_answer(student_pdf_path, answers_csv_path):
#     # Read the correct answers from the CSV file
#     qa_data = pd.read_csv(answers_csv_path)
#     correct_questions = qa_data['Question'].tolist()
#     correct_answers = qa_data['Answer'].tolist()

#     # Extract student answers from the PDF file
#     student_text = ""
#     with pdfplumber.open(student_pdf_path) as pdf:
#         for page in pdf.pages:
#             student_text += page.extract_text() + " "

#     # Clean and correct the text
#     student_text = clean_text(student_text)

#     # Process the student answers
#     student_qas = process_student_answers(student_text)

#     # Call the model and compute score and feedback
#     score, feedback = process_model(correct_questions, correct_answers, student_qas)

#     return score, feedback


# def clean_text(text):
#     text = text.replace("(cid:415)", "").replace("  ", " ").strip()
#     return text


# def correct_spelling(text):
#     blob = TextBlob(text)
#     return str(blob.correct())


# def process_student_answers(text):
#     student_qas = []
#     current_q = ""
#     current_a = ""

#     for line in text.split("\n"):
#         line = line.strip()
#         if line.startswith("Q."):
#             if current_q and current_a:
#                 student_qas.append((current_q, current_a))
#             current_q = line[2:].strip()
#             current_a = ""
#         elif line.startswith("A."):
#             current_a = line[2:].strip()
#         else:
#             current_a += " " + line.strip()

#     if current_q and current_a:
#         student_qas.append((current_q, current_a))

#     return student_qas


# def extract_key_points(text):
#     key_points = re.split(r',|\band\b|\bor\b', text)
#     key_points = [point.strip() for point in key_points if len(point.split()) > 1]
#     return key_points


# def check_key_points(correct, student):
#     key_points = extract_key_points(correct)
#     missing_points = []
#     score_contribution = 0

#     for point in key_points:
#         words = point.split()
#         match_count = sum(1 for word in words if word.lower() in student.lower())
#         match_ratio = match_count / len(words)

#         if match_ratio < 0.5:  # Less than 50% match = missing key point
#             missing_points.append(point)

#         score_contribution += match_ratio

#     return key_points, missing_points, score_contribution / len(key_points)


# def adjust_score_for_key_points(correct_answer, student_answer, semantic_score):
#     # Check the key points and calculate the missing ones
#     key_points, missing_points, match_ratio = check_key_points(correct_answer, student_answer)

#     # If there are missing key points, we penalize the score
#     if missing_points:
#         adjusted_score = (semantic_score * 0.5) + (match_ratio * 0.5)
#         return adjusted_score, f"Incomplete answer. You missed key points like: {', '.join(missing_points)}."
#     else:
#         # If all key points are there, return the semantic score as is
#         return semantic_score, "Correct answer."


# def evaluate_one_word_answer(correct, student):
#     if correct.strip().lower() == student.strip().lower():
#         return 1.0, "Correct answer!"
#     else:
#         return 0.0, "Incorrect answer. Try again."


# def process_model(correct_questions, correct_answers, student_qas):
#     total_score = 0
#     feedback = []
#     total_possible_score = len(correct_questions)  # Total questions, for calculating percentage

#     # Loop through the student answers and compare them with the correct answers
#     for idx, (student_question, student_answer) in enumerate(student_qas):
#         correct_answer = correct_answers[idx]

#         # For one-word answers, use exact match evaluation
#         if len(correct_answer.split()) == 1 and len(student_answer.split()) == 1:
#             score_part, feedback_part = evaluate_one_word_answer(correct_answer, student_answer)
#             total_score += score_part
#             feedback.append({
#                 'question': correct_questions[idx],
#                 'student_answer': student_answer,
#                 'correct_answer': correct_answer,
#                 'status': feedback_part,
#                 'score': score_part
#             })
#         else:
#             # For longer answers, use semantic similarity via SentenceTransformer
#             score_part, feedback_part = evaluate_semantic_similarity(correct_answer, student_answer)

#             # Adjust the score by considering key points as well
#             adjusted_score, adjusted_feedback = adjust_score_for_key_points(correct_answer, student_answer, score_part)

#             total_score += adjusted_score
#             feedback.append({
#                 'question': correct_questions[idx],
#                 'student_answer': student_answer,
#                 'correct_answer': correct_answer,
#                 'status': adjusted_feedback,
#                 'score': adjusted_score
#             })

#     final_score = (total_score / total_possible_score) * 100

#     return final_score, feedback


# def evaluate_semantic_similarity(correct_answer, student_answer):
#     # Encode both correct and student answers using SentenceTransformer
#     correct_embedding = model.encode([correct_answer])
#     student_embedding = model.encode([student_answer])

#     # Calculate cosine similarity between the embeddings
#     similarity = cosine_similarity(correct_embedding, student_embedding)[0][0]

#     # Score based on similarity (thresholds can be adjusted as needed)
#     if similarity >= 0.9:
#         return 1.0, "Correct"
#     elif similarity >= 0.7:
#         return similarity, f"Partially Correct. Similarity: {similarity:.2f}"
#     else:
#         return similarity, f"Incomplete answer. Similarity: {similarity:.2f}"




import pdfplumber
import pandas as pd
from textblob import TextBlob
import re
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_student_answer(student_pdf_path, answers_csv_path):
    # Read the correct answers from the CSV file
    qa_data = pd.read_csv(answers_csv_path)
    correct_questions = qa_data['Question'].tolist()
    correct_answers = qa_data['Answer'].tolist()

    # Extract student answers from the PDF file
    student_text = ""
    with pdfplumber.open(student_pdf_path) as pdf:
        for page in pdf.pages:
            student_text += page.extract_text() + " "

    # Clean and correct the text
    student_text = clean_text(student_text)
    student_text = correct_spelling(student_text)

    # Process the student answers
    student_qas = process_student_answers(student_text)

    # Call the model and compute score and feedback
    score, feedback = process_model(correct_questions, correct_answers, student_qas)

    return score, feedback


def clean_text(text):
    text = text.replace("(cid:415)", "").replace("  ", " ").strip()
    return text


def correct_spelling(text):
    blob = TextBlob(text)
    return str(blob.correct())


def process_student_answers(text):
    student_qas = []
    current_q = ""
    current_a = ""

    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("Q."):
            if current_q and current_a:
                student_qas.append((current_q, current_a))
            current_q = line[2:].strip()
            current_a = ""
        elif line.startswith("A."):
            current_a = line[2:].strip()
        else:
            current_a += " " + line.strip()

    if current_q and current_a:
        student_qas.append((current_q, current_a))

    return student_qas


def extract_key_points(text):
    key_points = re.split(r',|\band\b|\bor\b', text)
    key_points = [point.strip() for point in key_points if len(point.split()) > 1]
    return key_points


def check_key_points(correct, student):
    key_points = extract_key_points(correct)
    missing_points = []
    score_contribution = 0

    for point in key_points:
        words = point.split()
        match_count = sum(1 for word in words if word.lower() in student.lower())
        match_ratio = match_count / len(words)

        if match_ratio < 0.5:  # Less than 50% match = missing key point
            missing_points.append(point)

        score_contribution += match_ratio

    return key_points, missing_points, score_contribution / len(key_points)


def adjust_score_for_key_points(correct_answer, student_answer, semantic_score):
    # Check the key points and calculate the missing ones
    key_points, missing_points, match_ratio = check_key_points(correct_answer, student_answer)

    # If there are missing key points, we penalize the score
    if missing_points:
        adjusted_score = (semantic_score * 0.5) + (match_ratio * 0.5)
        return adjusted_score, f"Incomplete answer. You missed key points like: {', '.join(missing_points)}."
    else:
        # If all key points are there, return the semantic score as is
        return semantic_score, "Correct answer."


def evaluate_one_word_answer(correct, student):
    if correct.strip().lower() == student.strip().lower():
        return 1.0, "Correct answer!"
    else:
        return 0.0, "Incorrect answer. Try again."


def process_model(correct_questions, correct_answers, student_qas):
    total_score = 0
    feedback = []
    total_possible_score = len(correct_questions)  # Total questions, for calculating percentage

    # Loop through the student answers and compare them with the correct answers
    for idx, (student_question, student_answer) in enumerate(student_qas):
        correct_answer = correct_answers[idx]

        # For one-word answers, use exact match evaluation
        if len(correct_answer.split()) == 1 and len(student_answer.split()) == 1:
            score_part, feedback_part = evaluate_one_word_answer(correct_answer, student_answer)
            total_score += score_part
            feedback.append({
                'question': correct_questions[idx],
                'student_answer': student_answer,
                'correct_answer': correct_answer,
                'status': feedback_part,
                'score': score_part
            })
        else:
            # For longer answers, use semantic similarity via SentenceTransformer
            score_part, feedback_part = evaluate_semantic_similarity(correct_answer, student_answer)

            # Adjust the score by considering key points as well
            adjusted_score, adjusted_feedback = adjust_score_for_key_points(correct_answer, student_answer, score_part)

            total_score += adjusted_score
            feedback.append({
                'question': correct_questions[idx],
                'student_answer': student_answer,
                'correct_answer': correct_answer,
                'status': adjusted_feedback,
                'score': adjusted_score
            })

    final_score = (total_score / total_possible_score) * 100

    return final_score, feedback


def evaluate_semantic_similarity(correct_answer, student_answer):
    # Encode both correct and student answers using SentenceTransformer
    correct_embedding = model.encode([correct_answer])
    student_embedding = model.encode([student_answer])

    # Calculate cosine similarity between the embeddings
    similarity = cosine_similarity(correct_embedding, student_embedding)[0][0]

    # Score based on similarity (thresholds can be adjusted as needed)
    if similarity >= 0.9:
        return 1.0, "Correct"
    elif similarity >= 0.7:
        return similarity, f"Partially Correct. Similarity: {similarity:.2f}"
    else:
        return similarity, f"Incomplete answer. Similarity: {similarity:.2f}"