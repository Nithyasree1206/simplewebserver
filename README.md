# EX01 Developing a Simple Webserver
## Date:24.03.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.


## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Timetable</title>
</head>
<body>

    <h2>Weekly Timetable</h2>
    
    <table border="1">
        <tr>
            <th>Time</th>
            <th>Monday</th>
            <th>Tuesday</th>
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
        </tr>
        <tr>
            <td>9:00 AM - 10:00 AM</td>
            <td>Math</td>
            <td>Science</td>
            <td>English</td>
            <td>Physics</td>
            <td>Chemistry</td>
        </tr>
        <tr>
            <td>10:00 AM - 11:00 AM</td>
            <td>History</td>
            <td>Geography</td>
            <td>Computer Science</td>
            <td>Biology</td>
            <td>Math</td>
        </tr>
        <tr>
            <td>11:00 AM - 12:00 PM</td>
            <td>Break</td>
            <td>Break</td>
            <td>Break</td>
            <td>Break</td>
            <td>Break</td>
        </tr>
        <tr>
            <td>12:00 PM - 1:00 PM</td>
            <td>English</td>
            <td>Physics</td>
            <td>Chemistry</td>
            <td>Math</td>
            <td>Computer Science</td>
        </tr>
    </table>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
<img width="868" alt="terminal code" src="https://github.com/user-attachments/assets/bae8eb4a-b709-4f8c-a2ef-b1148fa3649a" />
<img width="950" alt="web output" src="https://github.com/user-attachments/assets/bacc20ec-a9ce-4189-b81a-6bba8cce8628" />



## RESULT:
The program for implementing simple webserver is executed successfully.
