# App Backend

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    # Open and read current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment count by 1
    count += 1

    # Set new value of count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # Display html with current value of count
    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run()
