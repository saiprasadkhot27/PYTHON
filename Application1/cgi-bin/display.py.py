#!C:/Python313/python.exe

print("Content-Type: text/html\n")

print("""
<html>
<body>

<h2>Student Records</h2>

<table border="1">
<tr>
<th>Name</th>
<th>Mobile</th>
<th>Email</th>
<th>Age</th>
</tr>
""")

with open("data.txt", "r") as file:
    for line in file:
        row = line.strip().split(",")
        print(f"""
        <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
        </tr>
        """)

print("""
</table>
<br>
<a href="/">Back</a>
</body>
</html>
""")