import subprocess
import typer
import os.path as path

app = typer.Typer()
pwd = path.abspath(path.dirname(__file__))
dcPath = path.join(pwd, "docker-compose.yaml")


@app.command()
def start():
    try:
        subprocess.Popen(
            ["docker-compose", "-f", dcPath, "up", "-d", "--build"]
        ).communicate()
        print("🎉 Successfully started Suplyd Odoo Containers ✅ ")
        print("💿 Postgres Server is available on → ", "http://localhost:5432")
        print("🎮 Odoo Web Console is available at → ", "http://localhost:8069")
    except:
        print("Is Docker Running?")


@app.command()
def stop():
    try:
        subprocess.Popen(["docker-compose", "-f", dcPath, "down", "-v"]).communicate()
        print("👍 Successfully stopped docker-compose and removed the volumes.")
    except:
        print("Is Docker even running?")


if __name__ == "__main__":
    app()
