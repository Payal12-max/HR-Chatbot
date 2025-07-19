import csv
import os

def save_to_csv(candidate_name, candidate_email, job_role, questions, answers, scores, average_score, status, filename="candidate_results.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write headers if the file doesn't exist
        if not file_exists:
            headers = ["Name", "Email", "Role"]
            max_questions = max(len(questions), 5)  # Handles cases where questions < or > 5
            for i in range(1, max_questions + 1):
                headers += [f"Q{i}", f"A{i}", f"S{i}"]
            headers += ["Avg Score", "Status"]
            writer.writerow(headers)

        # Pad lists to ensure consistent number of columns
        max_len = max(len(questions), 5)
        questions += [""] * (max_len - len(questions))
        answers += [""] * (max_len - len(answers))
        scores += [""] * (max_len - len(scores))

        # Create the row
        row = [candidate_name, candidate_email, job_role]
        for q, a, s in zip(questions, answers, scores):
            row += [q, a, s]
        row += [average_score, status]

        writer.writerow(row)



