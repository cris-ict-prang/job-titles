# Prang, G.8
# Booleans & Conditionals - Job Titles
# This program will accept a predefined employee's first name as a command line argument and print their employee title as: gender title, full name, and job title of the employee in the form: "{gender_title} {full_name}, {seniority} {job_title}"


### START - DO NOT EDIT ###
import sys

# list of dictionaries of employee data
# (gender_code must be only 'M' for male or 'F' for female)
employees = [
    {
        'first_name': 'John',
        'last_name': 'Smith',
        'age': 23,
        'gender_code': 'M'
    },
    {
        'first_name': 'Joe',
        'last_name': 'Ruddy',
        'age': 33,
        'gender_code': 'M'
    },
    {
        'first_name': 'Jenny',
        'last_name': 'McPherson',
        'age': 24,
        'gender_code': 'F'
    },
    {
        'first_name': 'Janice',
        'last_name': 'Johnson',
        'age': 33,
        'gender_code': 'F'
    },
    {
        'first_name': 'Jill',
        'last_name': 'Lancaster',
        'age': 46,
        'gender_code': 'F'
    }
]

engineers = ['Joe', 'Jenny']
managers = ['Joe', 'Jill']

def employee_data(first_name):
    ''' return the dictionary for an employee if exists, or None '''
    for data in employees:
        if data['first_name'] == first_name:
            return data
    return None

### END - DO NOT EDIT ###

### EDIT HERE ###
def job_title(data): 
    '''accepts a dictionary and returns a string employee job title'''

    first_name = data['first_name']
    last_name = data['last_name']

    if first_name in engineers and first_name in managers:
        job_title = "Engineering Manager"
    elif first_name in engineers:
        job_title = "Engineer"
    elif first_name in managers:
        job_title = "Manager"
    else:
        job_title = "Employee"

    if data['age'] < 25:
        seniority = "Jr. "
    elif data ['age'] >= 35:
        seniority = "Sr. "    
    else:
        seniority = ""

    if data['gender_code'] == 'M':
        gender_title = "Mr."
    else:
        gender_title = "Ms."

    return f"{gender_title} {first_name} {last_name}, {seniority}{job_title}"

# check for proper command line arguments or print usage and exit
if len(sys.argv) != 2:
    print("usage: job-title.py <first_name>", file=sys.stderr)
    sys.exit(1)

# get the first_name from the command line argument
first_name = sys.argv[1]

# get the employee dictionary for this first_name
data = employee_data(first_name)

# check that data is vavid or print error message and exit
if not data:
    print(f"no such employee: {first_name}", file=sys.stderr)
    sys.exit(1)

output = job_title(data)
print(output)

# TODO Steps: 
# 1. check that data is vavid or print error message and exit
# 2. create a 'job-titles()' function that
#    * accepts a dictionary as an argument
#    * returns a string employee job title, for example:
#    * "Mr. John Smith, Jr. Employee"
# 3. Print the string returned by 'job_title()'
