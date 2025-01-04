#!/usr/bin/env python3
import os
from datetime import datetime

def create_post(title):
    posts_directory = os.path.join(os.path.dirname(__file__), '..', '_posts')
    current_date = datetime.now().strftime('%Y-%m-%d')
    file_title = title.lower().replace(" ", "-")
    file_name = f"{current_date}-{file_title}.md"
    file_path = os.path.join(posts_directory, file_name)
    header = f"---\nlayout: post\ntitle: {title}\ndate: {current_date}\n---\n"

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(header)

    print(f"Post created successfully: {file_path}")

if __name__ == "__main__":
    title = input("Enter the title of the post: ")
    create_post(title)
