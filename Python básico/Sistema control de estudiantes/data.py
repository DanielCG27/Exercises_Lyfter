import csv

def export_students_to_csv(students):
    if not students:
        print("No students to export.")
        return
    
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Class group", "Spanish", "English", "Social studies", "Science", "Average"])

        for student in students:
            writer.writerow([student['name'], student['class_group'], student['spanish'], student['english'], student['social_studies'], student['science'], student['average']])

    print("Students exported successfully")


def import_students_from_csv(students):
    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
    

            next(reader)

            temp_students = []

            has_data = False

            for row in reader:
                has_data = True
                name, class_group, spanish, english, social_studies, science, average = row
            

                student = {
                    "name": name,
                    "class_group": class_group,
                    "spanish": float(spanish),
                    "english": float(english),
                    "social_studies": float(social_studies),
                    "science": float(science),
                    "average": float(average)
                }

                temp_students.append(student)

            if not has_data:
                print("File is empty. No students imported.")
                return
            
            students.clear()
            students.extend(temp_students)

        print("Students imported successfully")
        
    except FileNotFoundError:
        print("No previous file found.")