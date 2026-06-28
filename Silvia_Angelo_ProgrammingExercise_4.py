#Functions will validate phone numbers, social security numbers and zip codes using regular expressions.
#Main function will get input from a user and then display if
#the phone number, social security number and zip code they entered is valid.
import re

#Function to validate zipcode.
def validate_zip_code(zip_code):
    #Zip code pattern used for comparison.
    zip_pattern = r'^\d{5}?$'
    if re.match(zip_pattern, zip_code):
        return True
    return False

#Function to validate SSN.
def validate_ssn(ssn):
    #SSN pattern used for comparison.
    ssn_pattern = r'^\d{3}-\d{2}-\d{4}$'
    if re.match(ssn_pattern, ssn):
        return True
    return False

#Function to validate phone number.
def validate_phone_number(phone):
    #Phone number pattern used for comparison.
    phone_pattern = r'^(\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$'
    if re.match(phone_pattern, phone):
        return True
    return False

#Main function to gather numbers, analyze, and display results.
def main():
    print ("--- Data Validation Tool ---")

    #Gather input/data.
    get_zip_code = input("Please enter a zip code: ")
    get_ssn = input("Please enter a Social Security Number: ")
    get_phone = input("Please enter a phone number: ")

    #Display results.
    if validate_zip_code(get_zip_code):
        print(f"Valid zip code: {get_zip_code}")
    else:
        print(f"Invalid zip code: {get_zip_code}")

    if validate_ssn(get_ssn):
        print(f"Valid SSN: {get_ssn}")
    else:
        print(f"Invalid SSN: {get_ssn}")

    if validate_phone_number(get_phone):
        print(f"Valid Phone Number: {get_phone}")
    else:
        print(f"Invalid Phone Number: {get_phone}")

if __name__ == "__main__":
        main()

