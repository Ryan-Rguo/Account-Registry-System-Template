# Account-Registry-System-Template
A website account sign-up system practice, with MD5 encrypted,  based on Python 3.8, data stored in SQLite3.

HOW TO START: While WebRegister.py is running, use http://localhost:5000/ in web browser to start testing.

Functions:

Registry:
1. Username minimum lenth: 6
2. Password minimum lenth: 8
3. Repeat password for double-check
4. Email address is required.
5. Check if username and email already exists in database.
6. Each password is added with randomly generated salt, encrypted and stored in MD5 format.
7. Reflect different input errors accordingly.

Login:
1. Check if inputed username exists in database.
2. Reflect different input errors accordingly
3. Show account details with successful login.

Database Maintainance:
1. Check accounts exist in database.
2. Check specific data in database or relevant accounts
3. Delete accounts


File location:

... \ database.db

... \ database_maintainance.py

... \ WebRegister.py

... \ templates \ registry_home.html

... \ templates \ signin_form.html

... \ templates \ signin_ok_registry.html

... \ templates \ signup_form.html

... \ templates \ signup_ok.html


If there is any problem, please let me know, thank you.
