from threading import Thread, Lock
import time

a_lock = Lock()


def add_word(words, sentence):
    # any task here are executed by multiple threads in a concurrent fashion
    with a_lock:
        # the thread that acquired the lock will block the other threads from executing this section
        for each_word in sentence.split(' '):
            words.append(each_word)
            time.sleep(0.1)
    # assume that there are more work done here; this also will be executed by multiple threads in concurrent manner


def main():
    # shared resource; writable
    list_of_words = []
    s1 = 'my name is vinod and i live in bangalore'
    s2 = 'this is a python training for target corporation'
    s3 = 'the quick and brown fox jumps over the lazy dog'

    t1 = Thread(name='t1', target=add_word, args=(list_of_words, s1))
    t2 = Thread(name='t2', target=add_word, args=(list_of_words, s2))
    t3 = Thread(name='t3', target=add_word, args=(list_of_words, s3))

    for t in (t1, t2, t3): t.start()
    for t in (t1, t2, t3): t.join()
    print(list_of_words)


if __name__ == '__main__':
    main()
