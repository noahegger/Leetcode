import os

# Path to GitHub repo
repo_path = "/Users/noahegger/git/Leetcode"
# Path to Obsidian vault
obsidian_vault_path = (
    "/Users/noahegger/Documents/Obsidian Vault/Programming/LeetCode Problems"
)


# Function to format the content
def format_leetcode_file(problem_name, tags):
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

    # Create Markdown content without the title
    markdown_content = f"## Tags\n{tags}\n\n"  # Adds tags section
    markdown_content += f"## Problem Description\n{problem_description}\n\n"
    markdown_content += "## My Solution\n```python\n" + solution_code + "\n```\n"

    return markdown_content


def save_to_obsidian(problem_name, content):
    obsidian_file_path = os.path.join(obsidian_vault_path, f"{problem_name}.md")

    # Write content to the file if it doesn't already exist
    if not os.path.exists(obsidian_file_path):
        with open(obsidian_file_path, "w") as f:
            f.write(content)
        print(f"Saved {problem_name} to {obsidian_file_path}.")
    else:
        print(f"{problem_name} already exists in Obsidian. Skipping.")


# Main execution
if __name__ == "__main__":
    for folder in os.listdir(repo_path):
        if os.path.isdir(os.path.join(repo_path, folder)):
            # Prompt user to add tags for each new problem
            tags_input = input(
                f"Enter tags for {folder} (comma-separated, use underscores for multi-word tags): "
            )
            tags = " ".join(
                f"#{tag.strip().replace(' ', '_')}" for tag in tags_input.split(",")
            )  # Formats tags with underscores for multi-word

            markdown_content = format_leetcode_file(folder, tags)
            if markdown_content:
                save_to_obsidian(folder, markdown_content)
