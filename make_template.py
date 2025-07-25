import os
from pathlib import Path

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape

load_dotenv("stack.env")

KEYS = [
    "EXTERNAL_LISTEN_HOSTS",
    "ANY_SYNC_NODE_1_HOST",
    "ANY_SYNC_NODE_1_QUIC_PORT",
    "ANY_SYNC_NODE_1_PORT",
    "ANY_SYNC_NODE_2_HOST",
    "ANY_SYNC_NODE_2_QUIC_PORT",
    "ANY_SYNC_NODE_2_PORT",
    "ANY_SYNC_NODE_3_HOST",
    "ANY_SYNC_NODE_3_QUIC_PORT",
    "ANY_SYNC_NODE_3_PORT",
    "ANY_SYNC_COORDINATOR_HOST",
    "ANY_SYNC_COORDINATOR_QUIC_PORT",
    "ANY_SYNC_COORDINATOR_PORT",
    "ANY_SYNC_COORDINATOR_DEFAULT_LIMITS_SPACE_MEMBERS_READ",
    "ANY_SYNC_COORDINATOR_DEFAULT_LIMITS_SPACE_MEMBERS_WRITE",
    "ANY_SYNC_COORDINATOR_DEFAULT_LIMITS_SHARED_SPACES_LIMIT",
    "ANY_SYNC_FILENODE_HOST",
    "ANY_SYNC_FILENODE_QUIC_PORT",
    "ANY_SYNC_FILENODE_PORT",
    "ANY_SYNC_CONSENSUSNODE_HOST",
    "ANY_SYNC_CONSENSUSNODE_QUIC_PORT",
    "ANY_SYNC_CONSENSUSNODE_PORT",
    "MINIO_URL",
    "MINIO_BUCKET",
    "MONGO_URL",
    "REDIS_URL",
]

BASE_PATH = Path(__file__).parent


def main():
    env = Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        loader=FileSystemLoader(BASE_PATH / "templates/"),
        autoescape=select_autoescape(),
    )
    template = env.get_template("defaultTemplate.yml.j2")
    with open(BASE_PATH / "defaultTemplate.yml", "w") as file:
        file.write(template.render(**{key: os.environ.get(key) for key in KEYS}))


if __name__ == "__main__":
    main()
