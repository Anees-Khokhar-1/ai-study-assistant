from flask import Flask, request, jsonify
from models.summarizer import Summarizer
from services.pdf_parser import parse_pdf
from services.storage import save_summary, get_summary_by_id

app = Flask(__name__)

# Initialize summarizer
summarizer = Summarizer(model_name='facebook/bart-large-cnn')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    text = parse_pdf(file)  # Extract text from the uploaded PDF
    summary = summarizer.summarize(text)
    summary_id = save_summary(text, summary)  # Save to DB or file storage
    return jsonify({'summary_id': summary_id, 'summary': summary})

@app.route('/api/summarize', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text')
    summary = summarizer.summarize(text)
    return jsonify({'summary': summary})

@app.route('/api/summary/<id>', methods=['GET'])
def get_summary(id):
    summary = get_summary_by_id(id)
    if not summary:
        return jsonify({'error': 'Summary not found'}), 404
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
