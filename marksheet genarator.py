# College Student Result Management System - SGPA Marksheet Generator

def get_grade_point(grade_letter):
    # Standard 10-point scale
    mapping = {
        'O': 10,
        'A+': 9,
        'A': 8,
        'B+': 7,
        'B': 6,
        'C': 5,
        'F': 0
    }
    return mapping.get(grade_letter.upper(), None)

print("========== College Student SGPA Calculator ==========")

# Student details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
num_subjects = int(input("Enter number of subjects: "))

subjects = []
results = []
total_points = 0
total_credits = 0

for i in range(num_subjects):
    print(f"\nSubject {i+1}")
    subject_name = input("Enter subject name: ")
    grade_letter = input("Enter grade letter (O, A+, A, B+, B, C, F): ").upper()
    credit = float(input("Enter credits for this subject: "))

    grade_point = get_grade_point(grade_letter)
    if grade_point is None:
        print("Invalid grade! Use only O, A+, A, B+, B, C, F.")
        continue

    status = "Pass" if grade_point > 0 else "Arrear"

    results.append({
        "subject": subject_name,
        "grade": grade_letter,
        "credits": credit,
        "status": status
    })

    total_points += grade_point * credit
    total_credits += credit

# Calculate SGPA
sgpa = total_points / total_credits if total_credits > 0 else 0.0

# Pass/Fail: must pass all subjects
overall_status = "Pass" if all(r['status'] == "Pass" for r in results) else "Fail"

# Display mark sheet
print("\n========== MARK SHEET ==========")
print(f"Name: {student_name}")
print(f"Roll Number: {roll_number}")
print(f"Total Credits: {total_credits}\n")
print("Subject\t\tGrade\tCredits\tStatus")

for res in results:
    print(f"{res['subject']:15} {res['grade']:5} {res['credits']:7} {res['status']}")

print(f"\nSGPA: {sgpa:.2f} / 10.0")
print(f"Overall Result: {overall_status}")
print("===============================")

# Save to file
save = input("\nDo you want to save the mark sheet to a file? (yes/no): ").lower()
if save == 'yes':
    filename = f"{student_name}_marksheet.txt"
    with open(filename, "w") as f:
        f.write("========== MARK SHEET ==========\n")
        f.write(f"Name: {student_name}\n")
        f.write(f"Roll Number: {roll_number}\n")
        f.write(f"Total Credits: {total_credits}\n\n")
        f.write("Subject\t\tGrade\tCredits\tStatus\n")
        for res in results:
            f.write(f"{res['subject']:15} {res['grade']:5} {res['credits']:7} {res['status']}\n")
        f.write(f"\nSGPA: {sgpa:.2f} / 10.0\n")
        f.write(f"Overall Result: {overall_status}\n")
        f.write("===============================\n")
    print(f"Mark sheet saved as {filename}")

