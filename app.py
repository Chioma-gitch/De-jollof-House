from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def booking_page():
    return render_template('booking.html')
@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    date = request.form.get("date")
    service = request.form.get("service")

    # Save booking to a text file
    with open("booking,txt", "a") as file:
        file.write(f"{name},{phone},{email},{date},{service}")

        return render_template("success.html")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")