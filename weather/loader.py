import requests
import argparse

def parse_args() -> str:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("start_date", default="2021-01-01", type=str)
    parser.add_argument("end_date", default="2021-12-31", type=str)
    args = parser.parse_args()
    return args.img_path, args.degree


if __name__ == "__main__":
    link = "https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m"
    result = requests.get(link)
    result = result.json()
    print(result)