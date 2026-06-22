import inheritance_class as inh


def main():
    # Production Worker Details
        # Creating an input userface for workers to make manual entries 
    print("\n=== Production Worker Entry ===")
    name = input("Enter employee name: ")
    number = input("Enter employee number: ")
    shift = int(input("Enter shift (1 = Day, 2 = Night): "))
    pay_rate = float(input("Enter hourly pay rate: "))

    # Creating worker object from inheritance_class file
    worker = inh.ProductionWorker(name, number, shift, pay_rate)


    # Printing Worker Details 
        # Calling superclass Employee attributes from subclass ProductionWorker
    print("\n--- Production Worker Details ---")
    print(f"{'Name:':20}{worker.get_name()}")
    print(f"{'Employee Number:':20}{worker.get_number()}")

    # Printing Details of the type of shift
    if worker.get_shift() == 1:
        print(f"{'Shift:':20}Day")
    elif worker.get_shift() == 2:
        print(f"{'Shift:':20}Night")
    else:
        print("Invalid Shift")

    # Printing the Hourly Pay Rate
    print(f"{'Hourly Pay Rate:':20}${worker.get_pay_rate():.2f}")
    print()
    print()



    # Shift Supervisor Manual Entry
        # This also could have been done by creating a dictionary for two different supervisors attributes
        # Entry method used to match the Production Worker method
    print("\n=== Shift Supervisor Entry ===")
    sup_name = input("Enter supervisor name: ")
    sup_number = input("Enter supervisor number: ")
    salary = float(input("Enter annual salary: "))
    bonus = float(input("Enter annual bonus: "))

    # Creating supervisor object from inheritance file
    supervisor = inh.ShiftSupervisor(sup_name, sup_number, salary, bonus)

    # Printing Shift Supervisor Details
    print("\n--- Shift Supervisor Details ---")
    print(f"{'Name:':20}{supervisor.get_name()}")
    print(f"{'Employee Number:':20}{supervisor.get_number()}")
    print(f"{'Salary:':20}${supervisor.get_salary():,.2f}")
    print(f"{'Bonus:':20}${supervisor.get_bonus():,.2f}")
    print()
    print()

# Run the program
if __name__ == "__main__":
    main()
       