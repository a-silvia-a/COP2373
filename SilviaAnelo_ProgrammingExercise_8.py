#Program will allow user to record a specified number of student records.
#Then enter each student’s first name and last name as strings and
#the student’s three exam grades as integers.
# The CSV module will be used to write each record
#in grades.csv file and read the data back.

import csv

def write_grade_file():
    num_students = int(input("How many students do you want to enter? : "))

    with open('grades.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)

        csv_writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        for i in range(num_students):
            first_name = input(f"Enter First Name for student {i+1}: ")
            last_name = input(f"Enter Last Name for student {i+1}: ")
            exam1 = int(input(f"Enter score for Exam 1: "))
            exam2 = int(input(f"Enter score for Exam 2: "))
            exam3 = int(input(f"Enter score for Exam 3: "))

            student_record = {
                "First Name": first_name,
                "Last Name": last_name,
                "Exam 1": exam1,
                "Exam 2": exam2,
                "Exam 3": exam3
            }

            csv_writer.writerow([
                student_record['First Name'],
                student_record['Last Name'],
                student_record['Exam 1'],
                student_record['Exam 2'],
                student_record['Exam 3']
            ])
    print("\n[Success] grades.csv has been created and saved!")

def read_and_display_grades():
    print("\n" + "=" * 60)
    print("              STUDENT REPORT")
    print("=" * 60)

    with open('grades.csv', 'r') as f:
        csv_reader = csv.reader(f)

        headers = next(csv_reader)


        print(f"{'First Name':<15}{'Last Name':<15}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}")
        print("-" * 60)


        for row in csv_reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

    print("=" * 60)


def main():

    write_grade_file()
    read_and_display_grades()

if __name__ == "__main__":
    main()