import argparse
import yaml
import sys
import os
import pandas as pd

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

def load_data(input_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"input file not found: {input_path}")
        
    if os.path.getsize(input_path) == 0:
        raise ValueError("input file is empty")
        
    try:
        df = pd.read_csv(input_path)
    except Exception as e:
        raise ValueError(f"failed to parse csv: {e}")
        
    if df.empty:
        raise ValueError("csv contains no data rows")
        
    if 'close' not in df.columns:
        raise ValueError("csv is missing required 'close' column")
        
    return df

def main():
    parser = argparse.ArgumentParser(description="batch pipeline")
    parser.add_argument("--config", required=True, help="path to config yaml file")
    parser.add_argument("--input", required=True, help="path to input csv file")
    
    args = parser.parse_args()
    
    config = load_config(args.config)
    data = load_data(args.input)
    
    window = config['window']
    data['rolling_mean'] = data['close'].rolling(window=window, min_periods=window).mean()

if __name__ == "__main__":
    main()
