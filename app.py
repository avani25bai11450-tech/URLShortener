from flask import Flask, render_template, request, redirect, jsonify
import string
import random
import json
import os

app = Flask(__name__)

# In-memory storage for URL mappings (no database)
url_mappings = {}

# Base62 characters for short code generation
BASE62 = string.ascii_letters + string.digits

def generate_short_code(length=6):
    """Generate a random short code of specified length"""
    return ''.join(random.choice(BASE62) for _ in range(length))

def is_valid_url(url):
    """Basic URL validation"""
    return url.startswith(('http://', 'https://'))

@app.route('/')
def index():
    """Home page with URL shortening form"""
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """API endpoint to shorten a URL"""
    try:
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({'error': 'URL is required'}), 400
        
        original_url = data['url'].strip()
        
        # Validate URL
        if not is_valid_url(original_url):
            return jsonify({'error': 'Invalid URL format. URL must start with http:// or https://'}), 400
        
        # Generate unique short code
        short_code = generate_short_code()
        while short_code in url_mappings:
            short_code = generate_short_code()
        
        # Store the mapping
        url_mappings[short_code] = original_url
        
        # Return the shortened URL
        base_url = request.host_url.rstrip('/')
        short_url = f"{base_url}/{short_code}"
        
        return jsonify({
            'short_url': short_url,
            'short_code': short_code,
            'original_url': original_url
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/<short_code>')
def redirect_url(short_code):
    """Redirect to original URL"""
    if short_code in url_mappings:
        original_url = url_mappings[short_code]
        return redirect(original_url)
    else:
        return render_template('404.html'), 404

@app.route('/api/stats')
def get_stats():
    """Get basic statistics"""
    return jsonify({
        'total_urls': len(url_mappings),
        'urls': list(url_mappings.items())
    })

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 page"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """Custom 500 page"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Run the Flask app in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)