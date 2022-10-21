import os
import mysql.connector as mariadb
from dotenv import load_dotenv
import os


def main():

    #  Connect to the database
    load_dotenv()

    cxn = mariadb.connect(user=os.getenv("USERNAME"), password=os.getenv("PASS"), database=os.getenv("DATABASE"),
                          host=os.getenv("HOST"), port=os.getenv("PORT"))

    #  Create cursor

    cursor = cxn.cursor()

    #  Class Employee

    class Employee():

        def __init__(self, name, dep):
            self.name = name
            self.dep = dep

    #  Create new employee

        def createEmp(name, dep):
            emp = Employee(name, dep)
            cursor.execute(
                f"INSERT INTO employee (name,dep) VALUES ('{emp.name}','{emp.dep}')")
            cxn.commit()
            print("Employee created!")

    #  Show all employees

        def showEmps():
            Employee.showCount()
            cursor.execute("SELECT * FROM employee")
            result = cursor.fetchall()
            for x in result:
                print(
                    f"Employee id: {x[0]} \nEmployee name: {x[1]} \nEmployee department: {x[2]} \n \n********************")

    #  Show one employee

        def showEmp(id):
            cursor.execute(f"SELECT COUNT(*) FROM employee WHERE id={id}")
            result = cursor.fetchall()
            for x in result:
                isExist = x[0]

            #  If the id not existed
            if isExist == 0:
                print("Employee not existed!")
                quit()

            #  If the id existed
            else:
                cursor.execute(f"SELECT * FROM employee where id={id}")
                result = cursor.fetchall()
                for x in result:
                    print(
                        f"Employee id: {x[0]} \nEmployee name: {x[1]} \nEmployee department: {x[2]} \n \n********************")

        #  Delete employee

        def deleteEmp(id):
            #  Check if the id is exist
            cursor.execute(f"SELECT COUNT(*) FROM employee WHERE id={id}")
            result = cursor.fetchall()
            for x in result:
                isExist = x[0]

            #  If the id not existed
            if isExist == 0:
                print("Employee not existed!")
                quit()

            #  If the id existed
            else:
                cursor.execute(f"DELETE FROM employee WHERE id={id}")
                cxn.commit()
                print("Employee deleted!")

        #  Update employee

        def updateEmp(id):
            #  Check if the id is exist
            cursor.execute(f"SELECT COUNT(*) FROM employee WHERE id={id}")
            result = cursor.fetchall()
            for x in result:
                isExist = x[0]

            #  If the id is not exist
            if isExist == 0:
                print("Employee not exist!")
                quit()

            #  If the id is exist
            else:
                statusUpdate = input(
                    "What you wanna update, name of the employee (name) or department of the employee (dep): ")

                if statusUpdate == "name":  # To update the employee name
                    newName = input("Enter the new name: ")
                    cursor.execute(
                        f"UPDATE employee SET name='{newName}' WHERE id={id}")
                    cxn.commit()
                    print("Name updated!")

                elif statusUpdate == "dep":  # To update the employee department
                    newDep = input("Enter the new departemnt: ")
                    cursor.execute(
                        f"UPDATE employee SET dep='{newDep}' WHERE id={id}")
                    cxn.commit()
                    print("Department updated!")

                else:  # If the entered value is not valid
                    print("Plase enter a currect word next time!")
                    quit()

    # --------------------------------------------------------------- End class employee

    #  Status determination

    status = input(
        "\n create new employee (Create),\n update employee (update),\n delete employee (delete),\n show all employees (shows),\nshow one employee (show), \n quit(q) \n What you wanna do: ").lower()
    print("\n")

    #  Invoke create employee

    if status == "create":
        empName = input("Employee name: ")
        empDep = input("Employee department: ")
        Employee.createEmp(empName, empDep)

    #  Invoke update employee

    elif status == "update":
        empId = input("Enter employee number: ")
        check = empId.isnumeric()
        if check:
            Employee.updateEmp(empId)
        else:
            print("Please enter a number next time!")

    #  Invoke show all employees

    elif status == "shows":
        Employee.showEmps()

    #  Invoke delete employee ***

    elif status == "delete":
        empId = input("Enter employee id: ")
        check = empId.isnumeric()
        if check:
            Employee.deleteEmp(empId)
        else:
            print("Please enter a number next time!")

    elif status == "show":
        empId = input("Enter employee number: ")
        check = empId.isnumeric()
        if check:
            Employee.showEmp(empId)
        else:
            print("Please enter a number next time!")

    #  Quit the program

    elif status == "q":
        print("Bey bey :) ")
        quit()

    #  If the entered status not valid

    else:
        print("Please enter a currect word next time!")
        quit()

    cursor.close()
    cxn.close()


if __name__ == "__main__":
    main()
