import os
import argparse
from os.path import abspath
from multiprocessing import Queue
from pypdf import PdfReader 

def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Keyword search")
    parser.add_argument("path", type=str, help="Home path")
    parser.add_argument("keywords", default="", type=str, nargs="+", help="Keywords")
    parser.add_argument("--type", default="", type=str, help="Keywords")

    args = parser.parse_args()
    return abspath(args.path), args.keywords, args.type

def process(root_path: str, keywords, type: str) -> dict:
    ds = []
    gen = os.walk(root_path, topdown=True)
    for item in gen:
        current_dir, _, files = item
        for f in files:
            full_file_name = f"{current_dir}/{f}"
            try:
                if type != None and not full_file_name.endswith(type):
                    continue 
                if full_file_name.endswith("pdf"):
                    reader = PdfReader(full_file_name)
                    lines = reader.pages[0]
                    lines = lines.extract_text().lower()
                else:
                    with open(full_file_name, "r") as fp:
                        lines = fp.read()
                for key in keywords:
                    if key in lines: ds.append(full_file_name)
            except Exception:
                break
    return ds

if __name__ == "__main__":
    source_dir, keywords, type = parse_args()
    ds = process(source_dir, keywords, type)
    for d in ds:print(d)