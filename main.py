import argparse, yaml
from .scanner import Scanner

def main():
    parser = argparse.ArgumentParser(description="Extreme WVS Scanner")
    parser.add_argument("-c", "--config", default="config.yaml", help="Path to config YAML")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    scanner = Scanner(config)
    report_paths = scanner.crawl()
    print(f"Reports saved: {report_paths}")

if __name__ == "__main__":
    main()
