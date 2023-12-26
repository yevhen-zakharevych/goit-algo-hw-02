from queue import Queue
import random
from time import sleep


def generate_request(q, el):
    q.put(el)


def process_request(q):
    if q.empty():
        print("Queue is empty")

        return
    el = q.get()
    print("Processing request: {}".format(el))


def main():
    try:
        while True:
            queue = Queue()

            for i in range(random.randrange(10)):
                generate_request(queue, "element_" + str(i))

            for i in range(random.randrange(10)):
                process_request(queue)
                sleep(0.5)

    except KeyboardInterrupt:
        print('Interrupted!')


if __name__ == "__main__":
    main()
