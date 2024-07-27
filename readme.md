This code is based on a tutorial by Patrick Loeber
https://youtu.be/IUTFrexghsQ?si=55hxwaL9an03eIxR

Some modifications have been made:
1. Running llama in a docker container
2. Including only text selection

A. Initialisation
- python -m venv .venv
- .\.venv\Scripts\activate
- pip install -r requirements.txt

B. Running the app
- .\run_server_app.sh llama3
- python main.py llama3

C. Exiting the app
- Ctrl + q
- .\stop_server_app.sh
