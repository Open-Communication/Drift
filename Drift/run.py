import os
from pathlib import Path
import secrets

env_path = Path(".env")
if not env_path.exists():
    print("[+] .env file not found. Creating one...")
    with open(env_path, "w") as f:
        f.write(f"SECRET_KEY={secrets.token_urlsafe(32)}\n")
        f.write("SQLALCHEMY_DATABASE_URI=sqlite:///app.db\n")
        f.write("DEBUG=true\n")
    print("[+] .env created.")

from app import create_app

app = create_app()

if __name__ == "__main__":
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(debug=debug)
