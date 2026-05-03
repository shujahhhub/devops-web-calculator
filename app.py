from flask import Flask, request, render_template_string

app = Flask(__name__)

# This is our simple frontend UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Calculator</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        input, select, button { padding: 10px; margin: 5px; font-size: 16px; }
    </style>
</head>
<body>
    <h2>CI/CD Web Calculator</h2>
    <form method="POST">
        <input type="number" step="any" name="num1" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" step="any" name="num2" required>
        <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
        <h3 style="color: blue;">Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

# This is our backend logic
@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add': 
            result = num1 + num2
        elif operation == 'subtract': 
            result = num1 - num2
        elif operation == 'multiply': 
            result = num1 * num2
        elif operation == 'divide': 
            result = num1 / num2 if num2 != 0 else "Error: Cannot divide by zero"
            
    return render_template_string(HTML_PAGE, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)