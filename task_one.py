from queue import Queue
import random

queue = Queue()

def generate_request(id):
    request = f"request-{id}"
    queue.put(request)
    print(f"Generated: {request}")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processed: {request}")
    else:
        print("Queue is empty")


if __name__ == "__main__":

    while True:
        user_input = input("Enter a command: ").strip().lower()

        if user_input == "exit":
            print("Good bye!")
            break

        elif user_input == "gen":
            generate_request(random.randint(1, 101))

        elif user_input == "proc":
            process_request()

        else:
            print("commands: gen, proc, exit")