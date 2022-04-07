
# Gets the patient name from the console
get_thePatientName = input("Hi there, What is your name? ")
print(f'Hi, {get_thePatientName}')

# Gets the patient name and converts it to integer
get_thePatientAge = int(input("How old are you? (In years e.g. 30) "))

# Gets the patient status , patient or a new patient & converts it to lower case.
get_patientStatus = input("Are you a new patient with us? (Yes/No)").lower()

# Checks if they are a new patient or not
is_newPatient = False
summary = ''

# The if statements returns a summary of the patient details
# If the patient indicates yes, the message will be shown as a new patient
if get_patientStatus == 'yes':
    message = 'you are a new patient'
else:
    message = "you already a patient with us!"

# The summary of the patient details will be shown
print(f'Hi {get_thePatientName}, you are {get_thePatientAge} years old and {message}')