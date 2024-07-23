from pathlib import Path

def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, "r") as file:
            for line in file.readlines():
                    cat_info = {}
                    parts = line.split(',')
                    if len(parts) != 3:
                        raise ValueError(f"Incorrect format in line: {line}")
                    cat_info.update({
                        "id": str(parts[0].strip()),
                        "name": str(parts[1].strip()),
                        "age": str(parts[2].strip())
                    })
                    cats_info.append(cat_info)
    except:
        print("Oooops eror")
    return cats_info

current_dir = Path(__file__).parent
# relative_path = current_dir / "Cats.txt"

# cats_info = get_cats_info(relative_path)
# print(cats_info)