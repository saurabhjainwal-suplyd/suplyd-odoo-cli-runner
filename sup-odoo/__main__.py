import subprocess
import os.path as path
import sys
from halo import Halo

pwd = path.abspath(path.dirname(__file__))
dcPath = path.join(pwd, "docker-compose.yaml")


def run_docker_compose(cmd):
    out = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    return out


def spinner(msg: str):
    spin = Halo(text=f"{msg}..", spinner="dots")
    spin.start()
    return spin


def start():
    cmd = ("docker-compose", "-f", dcPath, "up", "-d", "--build")
    sp = spinner("Starting Containers...")
    out = run_docker_compose(cmd)
    if out.returncode != 0:
        sp.stop()
        print(out.stderr)
    else:
        sp.stop()
        print("🎮 Odoo Web Console is available at → ", "http://localhost:8069")


def stop():
    cmd = ("docker-compose", "-f", dcPath, "down", "-v")
    sp = spinner("Stopping Containers...")
    out = run_docker_compose(cmd)
    if out.returncode != 0:
        sp.stop()
        print(out.stderr)
    else:
        sp.stop()
        print("🎉 Successfully stopped Suplyd Odoo Containers ✅")


def main(command: str):
    if command == "start":
        start()
        sys.exit(0)
    elif command == "stop":
        stop()
        sys.exit(0)
    else:
        print("Exit bad command input")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Exit - more than once arguments were passed")
        sys.exit(1)
    elif len(sys.argv) <= 1:
        print("Exit - no command was passed")
        sys.exit(1)
    if sys.argv[1] != "start" and sys.argv[1] != "stop":
        print("Exit - invalid command was passed")
        print("Valid choices are 1) start, 2) stop")
        sys.exit(1)
    main(sys.argv[1])
