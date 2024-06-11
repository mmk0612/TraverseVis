from flask import Flask, render_template, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bfs')
def bfs():
    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'uninformed', 'breadth-first-search.py')
    print(f"Script path: {script_path}")
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        print(f"Script output: {result.stdout}")
        return render_template('bfs.html', output=result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return render_template('bfs.html', output=str(e))

@app.route('/dfs')
def dfs():
    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'uninformed', 'depth-first-search.py')
    print(f"Script path: {script_path}")
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        print(f"Script output: {result.stdout}")
        return render_template('bfs.html', output=result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return render_template('bfs.html', output=str(e))

@app.route('/dijkstra')
def dijkstra():
    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'uninformed', 'dijakstra-search.py')
    print(f"Script path: {script_path}")
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        print(f"Script output: {result.stdout}")
        return render_template('bfs.html', output=result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return render_template('bfs.html', output=str(e))

@app.route('/a_star')
def a_star():
    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'informed', 'a* search.py')
    print(f"Script path: {script_path}")
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        print(f"Script output: {result.stdout}")
        return render_template('bfs.html', output=result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return render_template('bfs.html', output=str(e))

@app.route('/best_fit')
def best_fit():
    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'informed', 'best-fit-search.py')
    print(f"Script path: {script_path}")
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        print(f"Script output: {result.stdout}")
        return render_template('bfs.html', output=result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return render_template('bfs.html', output=str(e))
    
@app.route('/hill_climbing')
def hill_climbing():
    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'informed', 'hill_climbing.py')
    print(f"Script path: {script_path}")
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        print(f"Script output: {result.stdout}")
        return render_template('bfs.html', output=result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return render_template('bfs.html', output=str(e))

if __name__ == "__main__":
    app.run(debug=True)
