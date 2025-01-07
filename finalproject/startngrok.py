import subprocess

def start_ngrok():
    try:
        subprocess.run(["./ngrok.exe", "http", "5000"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_ngrok()