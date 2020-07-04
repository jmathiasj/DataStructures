from flask import Flask,render_template
app = Flask(__name__) 

@app.route('/')
def running():
        return render_template('home.html')
@app.route('/stack')
def stacks():
        return render_template('stack.html')
@app.route('/queue')
def queues():
        return render_template('queue.html')
@app.route('/sll')
def slls():
        return render_template('sll.html')
@app.route('/cll')
def clls():
        return render_template('cll.html')
@app.route('/dll')
def dlls():
        return render_template('dll.html')
@app.route('/tree')
def trees():
        return render_template('tree.html')
if __name__ == "__main__":
    # app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT','5000')))
    app.run()
    app.debug=True