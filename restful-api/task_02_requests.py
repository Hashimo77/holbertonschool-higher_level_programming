#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # Check request success
    if response.status_code == 200:
        posts = response.json()

        # Print titles of all posts
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts and save id, title, body to posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure data as list of dictionaries
        rows = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Save to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
