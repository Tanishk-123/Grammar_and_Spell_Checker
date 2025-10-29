# Import required modules
# Flask – for building the web app and handling HTTP requests
# request – to access form and file data from client
# render_template – to render HTML templates (like index.html)
from flask import Flask, request, render_template
from model import SpellCheckerModule  # Import the custom spell/grammar checking module

# Initialize Flask app
app = Flask(__name__)

# Create an instance of the SpellCheckerModule class
spell_checker_module = SpellCheckerModule()


# ---------------------- ROUTES ----------------------

# Default route – renders the main index page
@app.route('/')
def index():
    # Render the template with empty placeholders initially
    return render_template(
        "index.html",
        corrected_text="",          # Corrected text from input
        corrected_grammar="",       # Grammar feedback from text area
        corrected_file_text="",     # Corrected text from uploaded file
        corrected_grammar_file=""   # Grammar feedback from uploaded file
    )


# Route to handle spell and grammar checking for text input
@app.route('/spell', methods=['POST', 'GET'])
def spell():
    if request.method == 'POST':
        # Retrieve user text input from the form
        text = request.form['text']

        # Perform spell correction using TextBlob
        corrected_text = spell_checker_module.correct_spell(text)

        # Perform grammar check using LanguageTool
        # NOTE: your correct_grammar() currently returns only one value (a list),
        # so remove the extra comma and underscore (“_”) if you don’t modify it
        corrected_grammar = spell_checker_module.correct_grammar(text)

        # Render the index page again with corrected results
        return render_template(
            'index.html',
            corrected_text=corrected_text,
            corrected_grammar=corrected_grammar
        )


# Route to handle grammar checking for uploaded files
@app.route('/grammar', methods=['POST', 'GET'])
def grammar():
    if request.method == 'POST':
        # Retrieve uploaded file from form
        file = request.files['file']

        # Decode file content into text (ignore non-text bytes)
        readable_file = file.read().decode('utf-8', errors='ignore')

        # Perform spell correction and grammar checking on the file text
        corrected_file_text = spell_checker_module.correct_spell(readable_file)
        corrected_grammar_file = spell_checker_module.correct_grammar(readable_file)

        # Render the index page with results for file input
        return render_template(
            'index.html',
            corrected_file_text=corrected_file_text,
            corrected_grammar_file=corrected_grammar_file
        )


# ---------------------- MAIN ENTRY POINT ----------------------
# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
