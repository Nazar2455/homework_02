from pathlib import Path

current_dir = Path(__file__).parent

def total_salary(path: str):
    sum_salary = 0
    count = 0
    
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                try:
                    salary = int(line.split(',')[1])
                    sum_salary += salary
                    count += 1
                except (IndexError, ValueError) as e:
                    print(f"Error processing line: {line} - {e}")

    if count == 0:
        return "No valid salary data found"
    
    avg_salary = sum_salary // count
    return f"Загальна сума заробітної плати: {sum_salary}, Середня заробітна плата: {avg_salary}"

# relative_path = current_dir / "salary_file.txt"
# print(total_salary(relative_path))