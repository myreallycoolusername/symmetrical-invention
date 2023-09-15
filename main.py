#test
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def thing():
 visitor_ip = request.headers.get("X-Forwarded-For")
 if visitor_ip is None:
  visitor_ip = request.headers.get("True-Client-IP")
  if visitor_ip is None:
   visitor_ip = request.remote_addr
   print(f"IP: {visitor_ip}")
   return f"Your IP is {visitor_ip}"
   # Run app
if __name__ == "__main__":
 app.run(host='0.0.0.0', port=3000)
