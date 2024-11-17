#!/usr/bin/env python3
import os
from datetime import datetime

if __name__ == "__main__":

    posts_directory = os.path.join(os.path.dirname(__file__), '..', '_posts')
    current_date = datetime.now().strftime('%Y-%m-%d')
    file_name = f"{current_date}.md"
    file_path = os.path.join(posts_directory, file_name)
    header = f"---\nlayout: post\ntitle: \ndate: {current_date}\n---\n"

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(header)

    print(f"Post creado: {file_path}")