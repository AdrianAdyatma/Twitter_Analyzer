from nltk.tokenize import TweetTokenizer

import credentials_var as cred
import formalization

count = 0

# Read documents in raw tweets collection then export to mongodb
for element in cred.find_all:
    message = element["text"]
    tokens = TweetTokenizer().tokenize(message.lower())


    # # Check if tokens already inserted
    # if not cred.tokens.count_documents({"id_str": element["id_str"]}, limit=1):
    #
    #     # Convert tokens as list to dictionary data type
    #     dictOfTokens = {str(i): tokens[i] for i in range(0, len(tokens))}
    #     dictOfTokens["id_str"] = element["id_str"]
    #
    #     # Export dictOfTokens to mongodb
    #     cred.tokens.insert_one(dictOfTokens)
    #     print(element["id_str"], "export token success")
    #     count += 1
    # else:
    #     print(element["id_str"], "export token error")
    #
    # print(count, "token(s) exported")
