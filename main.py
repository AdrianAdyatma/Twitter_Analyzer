import stream_twitter
import mongo_to_sql
import credentials_var as cred

keyword = ["tokopedia"]
limit = 5

if __name__ == '__main__':
    stream_twitter.stream.filter(track=keyword)

    # t = time.time()
    #
    # limit = 10
    #
    # thread1 = threading.Thread(target=stream_twitter.stream, args=("tokopedia", limit))
    # thread2 = threading.Thread(target=stream_twitter.stream, args=("bukalapak", limit))
    # # thread3 = threading.Thread(target=stream_twitter.stream, args=("shopee", limit))
    # thread4 = threading.Thread(target=stream_twitter.stream, args=("blibli", limit))
    # # thread5 = threading.Thread(target=stream_twitter.stream, args=("lazada", limit))
    #
    # thread1.start()
    # thread2.start()
    # # thread3.start()
    # thread4.start()
    # # thread5.start()
    #
    # thread1.join()
    # thread2.join()
    # # thread3.join()
    # thread4.join()
    # # thread5.join()
    #
    # print("Took", time.time() - t)

    # mongo_to_sql.mongo_to_sql(cred.find_unprocessed)
