todo_list = []

def add_task(deskripsyon):
    todo_list.append(deskripsyon)
    print("Tach ajoue :", deskripsyon)

def display_tasks():
    print("Lis tach yo :")
    for idx, task in enumerate(todo_list, start=1):
        print(f"{idx}. {task}")

def mark_task_done(task_idx):
    try:
        done_task = todo_list.pop(task_idx - 1)
        print("Tach ki fini :", done_task)
    except IndexError:
        print("Indice tach pa valid.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")
    print("Tach anrejistre nan tasks.txt.")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            todo_list.extend(file.read().splitlines())
        print("Tach soti nan tasks.txt.")
    else:
        print("Pa gen fichye tach.")

def main():
    while True:
        print("\nMenu:")
        print("1. Ajoute yon tach")
        print("2. Afiche tach yo")
        print("3. Make yon tach ki fini")
        print("4. Anrejistre tach yo")
        print("5. Telechaje tach yo")
        print("6. kite")

        choice = input("Chwazi yon opsyon : ")

        if choice == "1":
            deskripsyon = input("Mete deskripsyon tach la : ")
            add_task(deskripsyon)
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            task_idx = int(input("Mete nimewo tach ki fini an : "))
            mark_task_done(task_idx)
        elif choice == "4":
            save_tasks()
        elif choice == "5":
            load_tasks()
        elif choice == "6":
            print("Pwogram lan femen.")
            break
        else:
            print("Opsyon sa pa valid.")

if __name__ == "__main__":
    main()