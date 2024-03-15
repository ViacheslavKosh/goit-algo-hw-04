
def total_salary(path):
        try:
            with open(path, "r", encoding="UTF-8") as arg:
                lines = [el for el in arg.readlines()]
                count = 0
                total_salary = 0
                for line in lines:
                    parts = line.split(',')
                    salary_int = int(parts[1])
                    total_salary += salary_int
                    count += 1
                average_salary = total_salary//count
            return total_salary, average_salary, count # додав ще повернення кількості ітерацій як кількість працівників
        except FileNotFoundError:
             print(f'File {path} not found!')
             return None, None, None
        except Exception as e:
             print(f'Have an error: {e}!')
             return None, None, None


# Приклад використання
total, average, count = total_salary("lists/salary.txt")
print(f"We have {count} employees. Total salary: {total}. Averege salary is: {average}")   
