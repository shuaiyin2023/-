import threading
import queue

data_queue = queue.Queue()


def producer():
    """ 生产者线程不断产生数据 """
    for i in range(5):
        data_queue.put(i)  # 往队列中生产数据
        print("producer生产数据{}".format(i))
        threading.Event().wait(0.1)  # 模拟生产数据中的处理过程


def consumer():
    """ 消费者线程不断获取数据 """
    while True:
        data = data_queue.get()
        print("consumer消费数据: {}".format(data))
        threading.Event().wait(0.1)  # 模拟数据处理过程中的延迟


""" 创建生产者和消费者线程 """
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()


producer_thread.join()
consumer_thread.join()

