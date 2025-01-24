from flask import Flask, render_template, request

app = Flask(__name__)

# Route to show the form and handle submission
@app.route('/', methods=['GET', 'POST'])
def home():
    name = ''
    email = ''
    message = ''
    
    # Handle form submission (POST request)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = f'Thank you, {name}! We have received your email: {email}.'

    # Render the page with dynamic content (GET or POST)
    return render_template('index.html', name=name, email=email, message=message)

if __name__ == '__main__':
    app.run(debug=True)


aafasfsf
