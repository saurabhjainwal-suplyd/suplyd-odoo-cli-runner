import subprocess
import typer
import os.path as path

app = typer.Typer()
pwd = path.abspath(path.dirname(__file__))
dcPath = path.join(pwd, "docker-compose.yaml")


@app.command()
def start():
    out = subprocess.run(
        ("docker-compose", "-f", dcPath, "up", "-d", "--build"),
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        print(out.stderr)
    else:
        print("🎉 Successfully started Suplyd Odoo Containers ✅ ")
        print("💿 Postgres Server is available on → ", "http://localhost:5432")
        print("🎮 Odoo Web Console is available at → ", "http://localhost:8069")


@app.command()
def stop():
    out = subprocess.run(
        ("docker-compose", "-f", dcPath, "down", "-v"),
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        print(out.stderr)
    else:
        print("🎉 Successfully stoped Suplyd Odoo Containers ✅ ")


if __name__ == "__main__":
    app()
