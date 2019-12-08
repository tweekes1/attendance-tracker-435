This should answer some questions that you may have about the code

HELPFUL RESOURCES:
    cool flask tutorial that helped me understand flask -- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
    flask-wtf -- https://wtforms.readthedocs.io/en/stable/index.html
    flask-login -- https://flask-login.readthedocs.io/en/latest/
    Bulma (is a responsive framework can probably make mobile views) -- https://bulma.io/documentation/
    good flask authentication article also where I took inspiration for frontend -- https://scotch.io/tutorials/authentication-and-authorization-with-flask-login

Frontend 
    -- CSS frameworks: Bulma and Google icons
            BH this is was something I used just to get the project rolling
            I read an article and someone made similar login and register pages so 
            I took them and put my spin on them. These can be changed once the project is finished
    -- Jinja2:
            This is what will be used to display code returned from the backend to the frontend

Backend 
    -- Flask and extensions:
            Flask: a microframework that will be used to standup the web application
            flask-form: an extension that helps with input forms and basic validation, may need to sanitize forms to avoid SQL vulnerabilities
            flask-mysql: an extension that allows a flask app to connect a mysql database
            flask-wtf: an extension that will be used fof some basic security tools, i.e hashing passwords
            flask-login: provides handy login manager functions
            flask-sqlalchemy: an orm that will handle database operations
    -- MySQL: 
            Tables so far [SUBJECT TO CHANGE]

            User (
                user_id int (maybe use netid?) primary key
                netid varchar,
                name varchar,
                email varchar, 
                password_hash varchar
            )

            Class (
                class_id int primary key,
                name varchar,
                section varchar (may be unnecessary?), 
                professor_id int (will the professors be users, or something else? Will identify who is teaching the class)
            )

            =============FREESTYLING=============

            # Will be used to show all the students that are in a particular class
            # Should this be split up for each class? Maybe not since that would be a lot of data that could be consolidated
            Enrollment (
                class_id foreign key,
                student_id foreign key,
            )
        
            # Will be used to show all the dates in which a student attended class or verified attendance
            Attendance (
                class_id foreign key,
                student_id foreign key,
                date_attended date,
                attended bool
            )

