
def get_cats_info(path):
        try:
            with open(path, "r", encoding="UTF-8") as arg:
                lines = [el for el in arg.readlines()]
                cats = []
                for line in lines:
                    parts = line.split(',')
                    cats.append({'id':parts[0], 'name':parts[1], 'age':parts[2]})
            return cats
        except FileNotFoundError:
             print(f'File {path} not found!')
        except Exception as e:
             print(f'Have an error: {e}!')

# приклад використання
cats_info = get_cats_info("lists/cats.txt")
print(cats_info)
