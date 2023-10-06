from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a dictionary to store registered users (name as key, organization as value)
registered_users_dict = {}

# List of predefined student organizations
organizations = ['Organization A', 'Organization B', 'Organization C', 'Organization D', 'Organization E']

@app.route('/')
def home():
    return render_template('home.html', organizations=organizations)

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    organization = request.form['organization']

    # Backend validation
    if name.strip() == '' or organization not in organizations:
        return redirect(url_for('home'))

    registered_users_dict[name] = organization  # Updated variable name
    return redirect(url_for('registered_users'))

@app.route('/registered_users')
def registered_users():
    return render_template('registered.html', registered_users=registered_users_dict)  # Updated variable name

if __name__ == '__main__':
    app.run(debug=True)
