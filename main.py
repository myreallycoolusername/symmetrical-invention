# Import the flask module
from flask import Flask, request 
# Create an instance of the Flask class
app = Flask(__name__) 
# Define a route for the default URL
@app.route("/")
def index():
    # Try to get the visitor IP address from the X-Forwarded-For header
    visitor_ip = request.headers.get("X-Forwarded-For")
    # If the header is None, try to get the visitor IP address from the True-Client-IP header
    if visitor_ip is None:
        visitor_ip = request.headers.get("True-Client-IP")
    # If the header is None, use the remote_addr attribute instead
    if visitor_ip is None:
        visitor_ip = request.remote_addr
    # Print the visitor IP to console
    print(f"Visitor IP: {visitor_ip}")
    # Return a simple response
    return f"Hello, your IP address is {visitor_ip}" 
# Run the app if this file is executed as the main program
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
