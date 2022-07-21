import csv

with open("data_3.csv", mode="r") as f:

    reader = csv.DictReader(f)

    res = {}
    rep = {}
    for row in reader:
        reply_key = "utter_" + row['intent']
        if row['intent'] not in res.keys():
            res[row['intent']] = []
            rep[reply_key] = []
        res[row['intent']].append(row['text'])
        rep[reply_key].append(row['reply'])

    # print(res.keys())
    Note = open('ques.txt', mode='w')
    Note.write("nlu:\n")
    for key in res.keys():
        Note.write("- intent: "+key+"\n")
        Note.write("  examples: |\n")
        for text in res[key]:
            Note.write("    - "+text+"\n")

    Note2 = open('reply.txt', mode='w')
    for key in rep.keys():
        Note2.write("  "+key + ":\n")
        for text in rep[key]:
            Note2.write("    - text: \"" + text + "\"\n")