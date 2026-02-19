import requests
import os 
import subprocess

Everything_URL = "http://localhost:8888/"


def search(app_name):
    query = f'{app_name} ext:exe !setup !installer'

    params = {
        "search" : query,
        "json" : 1,
        "count" : 5,
        "path_column" : 1
    }
    response = requests.get(Everything_URL, params = params)

    if response.status_code != 200:
        return []
    
    data = response.json()
    results = [ 
        os.path.join(item["path"], item["name"])
        for item in data.get("results", [])
    ]
    

    return results


def rank_paths(paths, app_name):
    best_path = None
    best_score = -1
    for path in paths:
        score = 0
        lower_path = path.lower()
        filename = os.path.basename(lower_path)

        if filename == f"{app_name}.exe":
            score += 50

        if "program files" in lower_path:
            score += 30

        if "portable" in lower_path:
            score-= 30

        if "backup" in lower_path:
            score-= 20

        if score> best_score:
            best_score = score
            best_path = path

    return best_path




if __name__ == "__main__":
    app_name = input("Enter the app you want to open: ").lower()
    paths = search(app_name)
    best_match = rank_paths(paths, app_name)

    if best_match:
        print(f"Running {app_name}... ")
        subprocess.Popen(best_match)
    else:
        print("No Valid Application found!!")

