def process_text(text):
    # Replace this with your actual processing logic
    return f"You entered: {text.upper()}"

# Get the user input from the form
user_input = request.form["user_input"]

# Process the input and get the output
output = process_text(user_input)

# Send the output back to the HTML page (This approach is not recommended for security reasons)
print(f"<script>document.getElementById('output').innerHTML = '{output}';</script>")
