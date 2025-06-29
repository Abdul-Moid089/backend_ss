from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('hadith_data.json', 'r', encoding='utf-8') as f:
    hadiths = json.load(f)

def search_hadiths(query):
    query = query.lower()
    results = []
    for hadith in hadiths:
        text = f"{hadith['english']} {hadith['tags']}".lower()
        if query in text:
            results.append(hadith)
    return results

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Missing query'}), 400
    results = search_hadiths(query)
    return jsonify({'results': results})

@app.route('/')
def home():
    return "Seek Sunnah API is running."

if __name__ == '__main__':
    app.run(debug=True)

    if __name__ == '__main__':
    from flask_cors import CORS
    CORS(app)
    app.run(host='0.0.0.0', port=10000)
