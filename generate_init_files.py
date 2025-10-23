import os


def generate_init_files(base_dir="."):
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden/system folders and virtual environments
        if any(part.startswith('.') or part == 'venv' or part == '.venv' for part in root.split(os.sep)):
            continue

        init_path = os.path.join(root, "__init__.py")
        if not os.path.exists(init_path):
            with open(init_path, "w") as f:
                f.write(f'"""Package: {os.path.basename(root)}"""\n')
            print(f"✅ Created: {init_path}")


if __name__ == "__main__":
    generate_init_files("app")
