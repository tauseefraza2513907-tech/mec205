# app.py

```python
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Mechanical tools data
TOOLS = {
    "Vernier Caliper": {
        "use": "Measures internal, external, and depth dimensions accurately.",
        "range": "0-150 mm"
    },
    "Micrometer": {
        "use": "Measures very small dimensions with high precision.",
        "range": "0-25 mm"
    },
    "Torque Wrench": {
        "use": "Applies a specific torque to nuts and bolts.",
        "range": "10-200 Nm"
    },
    "Dial Gauge": {
        "use": "Measures small linear displacement and alignment errors.",
        "range": "0-10 mm"
    },
    "Hammer": {
        "use": "Used for striking, fitting, and shaping materials.",
        "range": "General Tool"
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mechanical Tools Web App</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 900px;
            margin: auto;
        }

        h1 {
            text-align: center;
            color: #222;
        }

        form {
            text-align: center;
            margin-bottom: 30px;
        }

        input[type="text"] {
            padding: 10px;
            width: 260px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button {
            padding: 10px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .tool-card {
            background-color: white;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .message {
            text-align: center;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Mechanical Engineering Tools</h1>

    <form method="POST">
        <input type="text" name="tool_name" placeholder="Enter Tool Name" required>
        <button type="submit">Search</button>
    </form>

    {% if searched %}
        {% if result %}
            <div class="tool-card">
                <h2>{{ tool_title }}</h2>
                <p><strong>Use:</strong> {{ result['use'] }}</p>
                <p><strong>Range:</strong> {{ result['range'] }}</p>
            </div>
        {% else %}
            <p class="message">Tool not found.</p>
        {% endif %}
    {% endif %}

    <h2>Available Mechanical Tools</h2>

    {% for tool, details in tools.items() %}
        <div class="tool-card">
            <h3>{{ tool }}</h3>
            <p><strong>Use:</strong> {{ details['use'] }}</p>
            <p><strong>Range:</strong> {{ details['range'] }}</p>
        </div>
    {% endfor %}
</div>

</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    tool_title = ""
    searched = False

    if request.method == 'POST':
        searched = True
        tool_name = request.form.get('tool_name', '').strip()

        for tool, details in TOOLS.items():
            if tool.lower() == tool_name.lower():
                result = details
                tool_title = tool
                break

    return render_template_string(
        HTML_TEMPLATE,
        tools=TOOLS,
        result=result,
        tool_title=tool_title,
        searched=searched
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

# requirements.txt

```txt
Flask==3.0.3
```

---

# Project Setup Instructions

## Step 1: Create Project Folder

Create a folder named:

```text
mechanical-tools-webapp
```

---

## Step 2: Create Files

Inside the folder create:

```text
app.py
requirements.txt
```

---

## Step 3: Install Required Library

Open terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

---

## Step 4: Run the Project

```bash
python app.py
```

---

## Step 5: Open in Browser

```text
http://127.0.0.1:5000
```

---

## Features of This Web App

* Mechanical tools information
* Search functionality
* Responsive user interface
* Flask backend
* Easy GitHub upload
* Beginner friendly project for ICT Lab
