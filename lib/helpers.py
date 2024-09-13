from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name_ = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name_)
    print(employee) if employee else print(f'Employee {name_} not found')


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_name(id_)
    print(employee) if employee else print(f'Employee {id_} not found')


def create_employee():
    name = input("Enter the employee's name:")
    job_title = input("Enter the employee's job title:")
    while True:
        department_id = input("Enter the employee's department id:")
        if Department.find_by_id(department_id):
            break
        else:
            print(f'Department with ID {department_id} not found.')
    try:
        Employee.create(name,job_title, int(department_id))
        print("Employee created successfully.")
    except Exception as exc:
        print("Error creating new employee")


def update_employee():
    id = input("Enter the employee's id:")
    if employee := Employee.find_by_id(int(id)):
        try:
            new_name = input("Enter the employees's new name:")
            employee.name = new_name

            new_job_title = input("Enter the employee's new job title:")
            employee.job_title = new_job_title

            while True:
                new_depertment_id = input("Enter the employees's new department id:")
                if Department.find_by_id(int(new_depertment_id)):
                    employee.department_id = int(new_depertment_id)
                    break
                else:
                    print(f'Department id not found.')
            employee.update()
            print('Successfully updated.')
        except Exception as exc:
            print('Error updating employee', exc)
    else:
        print('Employee id not found')


def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(int(id_)):
        employee.delete()
        print('Successfully Deleted')
    else:
        print('Employe id not found')


def list_department_employees():
    department_id = input("Enter the department id:")
    department = Department.find_by_id(int(department_id))

    if department:
        employees = [emp for emp in Employee.get_all() if emp.department_id == int(department_id)]
        if employees:
            print(f'Employees in {department.name}:')
            for employee in employees:
                print(employee)
        else:
            print(f'No employees found.')
    else:
        print('Department given not found.')