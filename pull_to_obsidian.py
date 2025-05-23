import datetime as dt
import os


def format_leetcode_file(problem_name, tags):
    readme_path = os.path.join(repo_path, problem_name, "README.md")
    solution_path = os.path.join(repo_path, problem_name, f"{problem_name}.py")

    if not os.path.exists(readme_path) or not os.path.exists(solution_path):
        print(f"Files for {problem_name} not found.")
        return

    with open(readme_path, "r") as f:
        problem_description = f.read()
    with open(solution_path, "r") as f:
        solution_code = f.read()

    mod_time = os.path.getmtime(readme_path)
    formatted_date = dt.datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")

    markdown_content = (
        f"---\n"
        f"title: {problem_name}\n"
        f"tags: [{tags}]  # Add your tags here, separated by commas\n"
        f"difficulty:   # Customize this or make it dynamic\n"
        f"date: {formatted_date}\n"
        f"---\n\n"
        f"## Problem Description\n"
        f"{problem_description}\n\n"
        f"## My Solution\n"
        f"```python\n"
        f"{solution_code}\n"
        f"```\n"
    )

    return markdown_content


def save_to_obsidian(problem_name, content, overwrite_existing=False):
    obsidian_file_path = os.path.join(obsidian_vault_path, f"{problem_name}.md")

    os.makedirs(obsidian_vault_path, exist_ok=True)

    if os.path.exists(obsidian_file_path) and not overwrite_existing:
        print(
            f"File for {problem_name} already exists. Skipping due to overwrite_existing=False."
        )
        return

    with open(obsidian_file_path, "w") as f:
        f.write(content)
    print(f"Saved {problem_name} to {obsidian_file_path}.")


if __name__ == "__main__":
    overwrite_existing = False
    repo_path = "/Users/noahegger/git/Leetcode"
    obsidian_vault_path = (
        "/Users/noahegger/Documents/Obsidian Vault/Programming/LeetCode Problems"
    )

    for folder in os.listdir(repo_path):
        if os.path.isdir(os.path.join(repo_path, folder)):
            tags = "example_tag"

            markdown_content = format_leetcode_file(folder, tags)
            if markdown_content:
                save_to_obsidian(
                    folder, markdown_content, overwrite_existing=overwrite_existing
                )
