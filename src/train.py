import os
from config import DATA_DIR, MODELS_DIR

try:
    import wandb
    HAS_WANDB = bool(os.environ.get("WANDB_API_KEY"))
except ImportError:
    HAS_WANDB = False

def train():
    if HAS_WANDB:
        wandb.init(project="ai-ds-starter", job_type="train")
        wandb.config.learning_rate = 0.001
        wandb.config.epochs = 10

    print(f"Data: {DATA_DIR}")
    print(f"Models: {MODELS_DIR}")

    if HAS_WANDB:
        wandb.log({"accuracy": 0.95, "loss": 0.05})
        wandb.finish()

if __name__ == "__main__":
    train()
