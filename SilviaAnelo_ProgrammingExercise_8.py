#Program will allow user to record a specified number of student records.
#Then enter each student’s first name and last name as strings and
#the student’s three exam grades as integers.
# The CSV module will be used to write each record
#in grades.csv file and read the data back.

import csv

#Function will prompt user to enter total number of student data.
def write_grade_file():
    num_students = int(input("How many students do you want to enter? : "))

    #Open file to write mode with newline containment.
    with open('grades.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)

        csv_writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        #Loop through range based on number of students.
        for i in range(num_students):
            first_name = input(f"Enter First Name for student {i+1}: ")
            last_name = input(f"Enter Last Name for student {i+1}: ")
            exam1 = int(input(f"Enter score for Exam 1: "))
            exam2 = int(input(f"Enter score for Exam 2: "))
            exam3 = int(input(f"Enter score for Exam 3: "))

            #Store values in dictionary.
            student_record = {
                "First Name": first_name,
                "Last Name": last_name,
                "Exam 1": exam1,
                "Exam 2": exam2,
                "Exam 3": exam3
            }

            #CSV writer to append student row to file.
            csv_writer.writerow([
                student_record['First Name'],
                student_record['Last Name'],
                student_record['Exam 1'],
                student_record['Exam 2'],
                student_record['Exam 3']
            ])
    print("\n[Success] grades.csv has been created and saved!")

#Function to open csv file, extract column headers, and individual data records.
def read_and_display_grades():
    print("\n" + "=" * 60)
    print("              STUDENT REPORT")
    print("=" * 60)

    #Open grades.csv file
    with open('grades.csv', 'r') as f:
        csv_reader = csv.reader(f)

        headers = next(csv_reader)


        #Print aligned colum headers with format widths.
        print(f"{'First Name':<15}{'Last Name':<15}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}")
        print("-" * 60)

        #Loop through each remaining row in reader object.
        for row in csv_reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

    print("=" * 60)

#Main driver function that executes file writing module followed by file reading module. 
def main():

    write_grade_file()
    read_and_display_grades()

if __name__ == "__main__":
    main()