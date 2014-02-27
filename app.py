from flask import Flask
app = Flask(__name__)

def convert_to_uzzy(original_text):
    """a function that converts 'normal' English to Uzzy plaintext"""
    print "start convert_to_uzzy"
    mappings = map(lambda l: map(lambda w: w.strip(), l.split("=")), open('./uzzy_dict.txt').readlines())
    print "after reading"

    converted = original_text
    for m in mappings:
        converted = converted.replace(m[0], m[1])

    # print original_text
    return converted

@app.route('/', methods=['POST', 'GET'])
def index():
    return convert_to_uzzy('do you want a banana')

if __name__ == "__main__":
    app.run()
