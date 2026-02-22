import requests
import os 
import subprocess

Everything_URL = "http://localhost:8888/"


def search(name, extensions=None, exclude=None):
    query =  query_builder(name, extensions, exclude)

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

def query_builder(name, extensions = None, exclude_words = None):
    query = name

    if extensions:
        ext_string = ";".join(extensions) 
        query += f" ext: {ext_string}"

    if exclude_words:
        for word in  exclude_words:
            query += f" !{word}"

    return query

def rank_paths(paths, app_name):
    best_path = None
    best_score = -1
    for path in paths:
        score = 0
        lower_path = path.lower()
        filename = os.path.basename(lower_path)

        if filename.startswith(app_name):
            score += 40

        if filename.endswith(".pdf"):
            score += 20
        elif filename.endswith(".mp3"):
            score += 15
        elif filename.endswith(".mp4"):
            score += 10

        if "documents" in lower_path:
            score += 15

        if "downloads" in lower_path:
            score -= 10

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
    if "." in app_name:
        paths = search(app_name)
    else:
        paths = search(app_name, extensions=["exe"])

    best_match = rank_paths(paths, app_name)


    if best_match:
        print(f"Running {app_name}...")
        os.startfile(best_match)
    else:
        print(f"Running {app_name}...")
        subprocess.Popen(f"start {app_name}", shell=True)

