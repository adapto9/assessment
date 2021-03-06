# assessment

## Project setup - Windows only
```
Clone this repo or download the root/dist folder
Run server.exe located in root/dist
*Database file will be generated in the same directory as server.exe, called database.db*
Navigate to http://127.0.0.1:5000/ on web browser to access the app
```

## Assumptions
```
Assuming internet connection is stable between User <-> Vue and Vue <-> Flask

# Story 1: Upload Users
Assuming CSV files to be uploaded are in same format as those in root/test folder
Assuming login and name are strings without any restrictions on alphabets only

# Story 2: Employee Dashboard Feature
Assuming 30 employees is the default amount of employees to view at a time
```

## Notes
```
Architecture is:
Vue <-> Flask

Vue
  -App.vue contains router-view, along with Navigation.vue component
  -Default view is Home.vue, containing Dashboard.vue component to view Employee list
  -Navigation can lead to Upload view to upload Employee CSVs
  -Vuetify was used for UI aesthetics and UX purposes
  -Therefore, flow is: App > View > Components

Flask
  -server.py for route definition and serverside logic
  -database.py for sqlite3 database querying
  -util.py for helper methods

If needed:
  -Vue CLI:
    -npm install inside root/frontend to install dependencies
    -npm run serve to host the Vue frontend

  -Python 3.7.7:
    -pip install -r requirements.txt inside root/backend to install dependencies
    -python server.py to host the Flask backend

To run the tests:
  -Have Python 3.7 installed
  -Run server.exe located in root/dist
  -Run test.py located in root/test/story1
  -Run test.py located in root/test/story2

To create a new dist:
  -server.exe is generated using PyInstaller inside root/backend through the command: pyinstaller --onefile server.py
  -Templates and static folder are generated inside root/frontend using the command: npm run build
  -From there, edit the links in the generated index.html and /js files to the following format:
    -href="{{ url_for('static', filename='img/favicon.ico') }}"
```

