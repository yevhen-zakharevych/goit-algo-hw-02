from queue import Queue
import random
from time import sleep


def generate_request(q, unique_id):
    el = "element_" + str(unique_id)
    q.put(el)


def process_request(q):
    if q.empty():
        print("Queue is empty")

        return
    el = q.get()
    print("Processing request: {}".format(el))


def main():
    try:
        counter = 0
        queue = Queue()

        while True:
            for i in range(random.randrange(10)):
                generate_request(queue, counter)
                counter += 1

            for i in range(random.randrange(11)):
                process_request(queue)
                sleep(0.5)

    except KeyboardInterrupt:
        print('Interrupted!')


if __name__ == "__main__":
    main()
