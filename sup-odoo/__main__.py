import subprocess
import os.path as path
import asyncio
import sys
from halo import Halo

pwd = path.abspath(path.dirname(__file__))
dcPath = path.join(pwd, "docker-compose.yaml")
starting_spinner = Halo(text="Starting Containers..", spinner="dots")
stopping_spinner = Halo(text="Stopping Containers..", spinner="dots")


async def run_docker_compose(cmd):
    out = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    return out


async def run_spinner():
    starting_spinner.start()


async def stop_spinner():
    stopping_spinner.start()


async def start():
    cmd = ("docker-compose", "-f", dcPath, "up", "-d", "--build")
    x, out = await asyncio.gather(run_spinner(), run_docker_compose(cmd))
    if out.returncode != 0:
        starting_spinner.stop()
        print(out.stderr)
    else:
        starting_spinner.stop()
        print("🎉 Successfully started Suplyd Odoo Containers ✅")
        print("💿 Postgres Server is available on → ", "http://localhost:5432")
        print("🎮 Odoo Web Console is available at → ", "http://localhost:8069")


async def stop():
    cmd = ("docker-compose", "-f", dcPath, "down", "-v")
    x, out = await asyncio.gather(stop_spinner(), run_docker_compose(cmd))
    if out.returncode != 0:
        stopping_spinner.stop()
        print(out.stderr)
    else:
        stopping_spinner.stop()
        print("🎉 Successfully stopped Suplyd Odoo Containers ✅")


async def main(command: str):
    if command == "start":
        await start()
        sys.exit(0)
    else:
        await stop()
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error - more than once arguments were passed")
        sys.exit(1)
    if sys.argv[1] != "start" and sys.argv[1] != "stop":
        print("Error - invalid command was passed")
        print("Valid choices are 1) start, 2) stop")
        sys.exit(1)
    asyncio.run(main(sys.argv[1]))
