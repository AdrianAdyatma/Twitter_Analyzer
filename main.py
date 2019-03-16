import stream_twitter
import mongo_to_sql
import credentials_var as cred


if __name__ == '__main__':
    # keyword = ["Joko Widodo", "jokowi"]
    # limit = 493
    # stream_twitter.stream(keyword, limit)
    #
    # keyword = ["Prabowo Subianto", "prabowo"]
    # limit = 500
    # stream_twitter.stream(keyword, limit)

    mongo_to_sql.mongo_to_sql(cred.find_unprocessed)
