from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configure Gemini API key
GOOGLE_API_KEY = "AIzaSyD9qMcPLvmDJOZzjBueOL17_f0EuhJgl64"
genai.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    try: 
        response = chat.send_message(user_input).text
        print(response)  # Debugging output
        return jsonify({"response": response})
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"error": "Internal server error"}), 500
    
if __name__ == '__main__': 
    app.run(debug=True)
