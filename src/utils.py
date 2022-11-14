import yaml

config_path = "config/config.yaml"

def load_config():

    try:

        with open(config_path, "r") as f:

            config = yaml.safe_load(f)

    except FileNotFoundError:

        return "Config file not found!"

    return config

if __name__ == "__main__":

    config=load_config()

    print(config)