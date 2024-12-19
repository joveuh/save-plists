 and target directories exist
    # if not os.path.isdir(source_dir):
    #     print(f"Source directory '{source_dir}' does not exist.")
    #     return
    # if not os.path.isdir(target_dir):
    #     os.makedirs(target_dir)  # Create target directory if it doesn't exist

    # # Walk through the source directory
    # for root, dirs, files in os.walk(source_dir):
    #     # Calculate target path
    #     relative_path = os.path.relpath(root, source_dir)
    #     target_path = os.path.join(target_dir, relative_path)

    #     # Ensure the target directory structure exists
    #     os.makedirs(target_path, exist_ok=True)

    #     # Copy files
    #     for file_name in files:
    #         source_file = os.path.join(root, file_name)
    #         target_file = os.path.join(target_path, file_name)

    #         # Skip if the file is a symbolic link (alias)
    #         if os.path.islink(source_file):
    #             print(f"Skipping alias (symlink): {source_file}")
    #             continue

    #         shutil.copy2(source_file, target_file)  # Copy file with metadata
    #         print(f"Copied file: {source_file} -> {target_file}")

    #     # Copy directories (skip symbolic links)
    #     dirs[:] = [d for d in dirs if not os.path.islink(os.path.join(root, d))]

    # print("All files a