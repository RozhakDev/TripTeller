from flask import render_template, request, jsonify
from app.main import bp
from .services import generate_story_from_image

@bp.route('/generate', methods=['POST'])
def generate_story_route():
    if 'photo' not in request.files or request.files['photo'].filename == '':
        return jsonify({'error': 'No photo selected'}), 400

    file = request.files['photo']
    location = request.form.get('location', 'an unknown place')
    tone = request.form.get('tone', 'creative')

    story = generate_story_from_image(file, location, tone)

    if "An error occurred" in story:
        return jsonify({'error': story}), 500
    
    return jsonify({'story': story}), 200

@bp.route('/')
def index():
    return render_template('index.html')