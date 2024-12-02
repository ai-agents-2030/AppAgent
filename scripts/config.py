import os
import yaml


def load_config(config_path="./config.yaml"):
    configs = dict(os.environ)
    with open(config_path, "r") as file:
        yaml_data = yaml.safe_load(file)
    configs.update(yaml_data)
    if os.getenv("OPENAI_BASE_URL"):
        configs["OPENAI_API_BASE"] = os.getenv("OPENAI_BASE_URL") + "/chat/completions"
    return configs
