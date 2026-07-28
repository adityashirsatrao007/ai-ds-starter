import os
from pathlib import Path

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    print("HF_TOKEN not set, skipping HF deployment")
    exit(0)

from huggingface_hub import HfApi, create_repo

api = HfApi()
repo_id = f"adityashirsatrao007/ai-ds-starter-model"

try:
    create_repo(repo_id, token=HF_TOKEN, exist_ok=True)
    api.upload_folder(
        folder_path=str(Path("models")),
        repo_id=repo_id,
        token=HF_TOKEN,
    )
    print(f"Deployed to https://huggingface.co/{repo_id}")
except Exception as e:
    print(f"Deploy failed: {e}")
