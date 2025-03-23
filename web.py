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