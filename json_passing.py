import json

def json_export(location, listOut):
    outfile = open(location,"w")


    outfile.write(json.dumps(listOut))
    outfile.close

def json_read(location):
    infile = open(location,"r")
    x = infile.read()
    infile.close()
    return json.loads(x)

def json_updater(location, key, value):
    infile = open(location,"r+")
    db = json.loads(infile.read())
    infile.close
    db[key] = value
    outfile = open(location,"w")
    outfile.write(json.dumps(db))
    outfile.close()


