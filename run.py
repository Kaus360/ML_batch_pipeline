import argparse
import yaml
import sys
import os

def load_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"config file not found: {config_path}")
        
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        
    if not isinstance(config, dict):
        raise ValueError("config must be a valid yaml dictionary")
        
    required_keys = ['seed', 'window', 'version']
    for key in required_keys:
        if key not in config:
            raise KeyError(f"missing required config key: {key}")
            
    return config

def main():
    parser = argparse.ArgumentParser(description="batch pipeline")
    parser.add_argument("--config", required=True, help="path to config yaml file")
    
    args = parser.parse_args()
    
    config = load_config(args.config)

if __name__ == "__main__":
    main()
