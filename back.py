from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
   return "This route is not used."

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name') 
   return "Hello, " + name + "!"

if __name__ == '__main__':
    app.run()
