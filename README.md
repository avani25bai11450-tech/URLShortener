# URL Shortener Project

A simple and elegant URL shortener application built with Flask for first-year CSE students. This project demonstrates basic web development concepts including routing, templating, and API endpoints without requiring database knowledge.

## 🚀 Features

- **URL Shortening**: Convert long URLs into short, shareable links
- **No Database Required**: Uses in-memory storage (perfect for beginners)
- **Beautiful UI**: Modern, responsive design with gradient backgrounds
- **Real-time Statistics**: Track total number of shortened URLs
- **Copy to Clipboard**: Easy copying of shortened URLs
- **Error Handling**: User-friendly error messages and pages
- **API Endpoints**: RESTful API for URL operations

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Modern CSS with gradients and animations
- **No Database**: Uses Python dictionaries for storage

## 📋 Requirements

- Python 3.6 or higher
- Flask 2.3.3 or higher

## 🎯 Installation & Setup

1. **Clone or download the project files**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run the application**:
   ```bash
   python app.py
   ```
   
4. **Open your browser** and go to `http://localhost:5000`

## 📁 Project Structure

```
URLShortner/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── Statement.md       # Project requirements
│
└── templates/         # HTML templates
    ├── index.html     # Main page with URL form
    ├── 404.html       # Not found error page
    └── 500.html       # Server error page
```

## 🔧 How It Works

### URL Shortening Process
1. User enters a long URL in the input field
2. Frontend validates the URL format
3. Backend generates a unique 6-character short code
4. URL mapping is stored in memory
5. Shortened URL is returned and displayed

### URL Redirection Process
1. User clicks on a shortened URL
2. Backend looks up the short code in memory
3. If found, redirects to the original URL
4. If not found, shows 404 error page

## 🌐 API Endpoints

### Shorten URL
- **POST** `/shorten`
- **Body**: `{"url": "https://example.com/long-url"}`
- **Response**: `{"short_url": "http://localhost:5000/abc123", "short_code": "abc123", "original_url": "https://abc.com/long-url"}`

### Get Statistics
- **GET** `/api/stats`
- **Response**: `{"total_urls": 5, "urls": [["abc123", "https://abc.com"]]}`

### Redirect to Original URL
- **GET** `/{short_code}`
- **Redirects** to original URL or shows 404 if not found

## 🎨 User Interface

The application features:
- **Modern Design**: Gradient backgrounds and smooth animations
- **Responsive Layout**: Works on desktop and mobile devices
- **User-Friendly Forms**: Clear input fields and buttons
- **Real-time Feedback**: Loading states and success messages
- **Error Handling**: Clear error messages for invalid inputs

## 🧪 Testing the Application

1. **Test URL Shortening**:
   - Enter a long URL like `https://www.abc.com/very/long/url/path`
   - Click "Shorten URL"
   - Copy the shortened URL

2. **Test URL Redirection**:
   - Paste the shortened URL in a new browser tab
   - Verify it redirects to the original URL

3. **Test Error Handling**:
   - Try entering an invalid URL
   - Try accessing a non-existent short code

## 🔍 Code Learning Points

This project demonstrates several important concepts for first-year CSE students:

### Python Concepts
- **Flask Routing**: How to create web routes
- **JSON Handling**: Working with JSON requests and responses
- **String Manipulation**: URL validation and short code generation
- **Dictionary Usage**: In-memory data storage
- **Error Handling**: Try-catch blocks and HTTP status codes

### Web Development Concepts
- **Client-Server Architecture**: How web applications work
- **HTTP Methods**: GET, POST requests
- **API Design**: RESTful endpoint creation
- **Frontend-Backend Communication**: AJAX requests
- **Template Rendering**: HTML templates with Flask

### JavaScript Concepts
- **DOM Manipulation**: Updating HTML elements
- **Event Handling**: Click events and form submissions
- **Fetch API**: Making HTTP requests
- **Async/Await**: Asynchronous programming
- **Clipboard API**: Copying text to clipboard

## 🎓 Educational Value

This project is designed to teach:
- Basic web application structure
- How URL shorteners work
- Frontend-backend communication
- Error handling and validation
- Modern web development practices

## 🔒 Security Considerations

- **URL Validation**: Ensures URLs start with http:// or https://
- **Input Sanitization**: Basic validation of user inputs
- **Error Handling**: Prevents application crashes
- **No Database**: Eliminates SQL injection risks

## 🐛 Common Issues & Solutions

### Port Already in Use
If you get a "port already in use" error:
```bash
# Kill process using port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or use a different port:
python app.py --port 5001
```

### Module Not Found
If you get "ModuleNotFoundError":
```bash
pip install Flask
```

### Template Not Found
If you get "TemplateNotFound" error:
- Ensure the `templates` folder exists in the same directory as `app.py`
- Check that HTML files are in the `templates` folder

## 🚀 Future Enhancements

Students can extend this project by adding:
- **Custom Short Codes**: Allow users to choose their own short codes
- **URL Expiration**: Add time-based expiration
- **Click Analytics**: Track how many times each URL is accessed
- **User Accounts**: Add authentication and user-specific URLs
- **QR Code Generation**: Generate QR codes for shortened URLs
- **URL Blacklist**: Block malicious URLs
- **Rate Limiting**: Prevent abuse
- **URL Preview**: Show preview before redirecting

## 🤝 Contributing

This is an educational project. Students are encouraged to:
- Experiment with the code
- Add new features
- Improve the design
- Fix any bugs they find
- Share their modifications with classmates

---

**Happy Coding! 🎉**

This URL shortener is a great starting point for learning web development. Keep experimenting and building amazing things!