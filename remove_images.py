#!/usr/local/bin/python3

import os
import re

def get_all_images(image_dir):
    return set([img for img in os.listdir(image_dir) if img not in [".keep", "banner.png"]])

def extract_images_from_md(md_content):
    # Extract images using markdown syntax
    md_images = re.findall(r'!\[.*?\]\(images/(.*?)\)', md_content)
    print(md_images)
    
    # Extract images using HTML img tag
    html_images = re.findall(r'<img.*?src=["\']images/(.*?)[\'"].*?>', md_content)
    
    return set(md_images + html_images)

def main(directory):
    image_dir = os.path.join(directory, 'images')
    archive_dir = os.path.join(image_dir, 'archive')
    
    # Ensure archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    all_images = get_all_images(image_dir)
    referenced_images = set()
    print("All images \n")
    print(all_images)

    # Traverse all .md files and extract image references
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    referenced_images.update(extract_images_from_md(content))

    print("Referenced images \n")
    print(referenced_images)

    # Determine unreferenced images
    unreferenced_images = all_images - referenced_images - {'archive'}

    print("Unreferenced images \n")
    print(unreferenced_images)

    # Move unreferenced images to archive
    for image in unreferenced_images:
        os.rename(os.path.join(image_dir, image), os.path.join(archive_dir, image))

    print(f"Moved {len(unreferenced_images)} images to the archive.")

if __name__ == "__main__":
    directory = input("Enter the image directory path: ")
    main(directory)

