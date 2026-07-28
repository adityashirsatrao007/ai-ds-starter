import wandb
from config import DATA_DIR, MODELS_DIR

def train():
    wandb.init(project="ai-ds-starter", job_type="train")
    wandb.config.learning_rate = 0.001
    wandb.config.epochs = 10

    # Training logic here
    print(f"Data: {DATA_DIR}")
    print(f"Models: {MODELS_DIR}")

    wandb.log({"accuracy": 0.95, "loss": 0.05})
    wandb.finish()

if __name__ == "__main__":
    train()
