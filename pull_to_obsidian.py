import os
import shutil

# Path to your GitHub repo
repo_path = "/Users/noahegger/git/Leetcode"
# Path to your Obsidian vault
obsidian_vault_path = "/Users/noahegger/Documents/Obsidian Vault/LeetCode Problems"


# Function to format the content
def format_leetcode_file(problem_name):
    readme_path = os.path.join(repo_path, problem_name, "README.md")
    solution_path = os.path.join(repo_path, problem_name, f"{problem_name}.py")

    if not os.path.exists(readme_path) or not os.path.exists(solution_path):
        print(f"Files for {problem_name} not found.")
        return

    # Read contents
    with open(readme_path, "r") as f:
        problem_description = f.read()
    with open(solution_path, "r") as f:
        solution_code = f.read()

    # Create Markdown content
    markdown_content = f"# {problem_name} Leetcode Problem\n\n"
    markdown_content += f"## Problem Description\n{problem_description}\n\n"
    markdown_content += "## My Solution\n```python\n" + solution_code + "\n```\n"

    return markdown_content


# Function to save the Markdown file
def save_to_obsidian(problem_name, content):
    obsidian_file_path = os.path.join(obsidian_vault_path, f"{problem_name}.md")
    with open(obsidian_file_path, "w") as f:
        f.write(content)
    print(f"Saved {problem_name} to {obsidian_file_path}.")


# Main execution
if __name__ == "__main__":
    for folder in os.listdir(repo_path):
        if os.path.isdir(os.path.join(repo_path, folder)):
            markdown_content = format_leetcode_file(folder)
            if markdown_content:
                save_to_obsidian(folder, markdown_content)
                print(f"Saved {folder} to Obsidian.")
