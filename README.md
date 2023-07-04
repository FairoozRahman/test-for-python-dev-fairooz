# Steps to run the project (Assuming that Python is installed and added in the environment variable in the computer)
1. Extract the zip file

2. Go into the extracted directory

3. Open a powershell terminal

4. Run the command 'pip install virtualenv'

5. Run the command 'python -m venv <virtual-environment-name>'

6. Run the command 'pip install -r requirements.txt'

7. Go into 'sentiment_analysis_api' directory

8. Run the command 'python manage.py runserver'

9. Open the url 'http://127.0.0.1:8000/' in your browser to have a frontend view.

10. Open the url 'http://127.0.0.1:8000/api/analyze/' in your browser to have a rest API view.


# URLs
## Examples images folder has various screenshots
* 'http://127.0.0.1:8000/' for submitting text data for analyzing with a frontend view.

* 'http://127.0.0.1:8000/analysis/:id/' for seeing the sentiment analysis with a frontend view (submit button would take you here).

* 'http://127.0.0.1:8000/api/analyze/' for the endpoint that accepts POST requests with a JSON data field "text".



# Superuser id (for accessing the database) 
url: http://127.0.0.1:8000/admin/

username: Fairooz

email: fairooz.rahman26@gmail.com

password: pythontest