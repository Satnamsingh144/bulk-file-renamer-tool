import os


def rename_files(folder, extension, prefix="", suffix="", preview=True):
    files = sorted(os.listdir(folder))
    count = 1

    for file in files:
        old_path = os.path.join(folder, file)

        # Skip non-file items
        if not os.path.isfile(old_path):
            continue

        # Extension filter
        if extension:
            extensions = [e.strip() for e in extension.split(",")]
            if not any(file.lower().endswith(ext.lower()) for ext in extensions):
                continue

        name, ext = os.path.splitext(file)

        new_name = f"{prefix}{name}{suffix}_{count}{ext}"
        new_path = os.path.join(folder, new_name)

        # Skip if file already exists
        if os.path.exists(new_path):
            print(f"⚠ Skipped (already exists): {new_name}")
            continue

        if preview:
            print(f"[PREVIEW] {file} → {new_name}")
        else:
            os.rename(old_path, new_path)
            print(f"Renamed: {file} → {new_name}")
            count += 1


def main():
    print("=== Bulk File Renamer Tool (Pro) ===")

    folder = input("Enter folder path: ").strip()

    if not os.path.isdir(folder):
        print("Invalid folder path!")
        return

    prefix = input("Enter prefix (optional): ").strip()
    suffix = input("Enter suffix (optional): ").strip()

    # Extension choice
    while True:
        choice = input(
            "Do you want to rename a particular extension? (yes/no): "
        ).lower()

        if choice == "yes":
            extension = input(
                "Enter extensions (comma separated, e.g. .jpg, .png): "
            ).strip()
            break
        elif choice == "no":
            extension = ""
            break
        else:
            print("❌ Invalid input! Please type 'yes' or 'no'.")

    # Preview choice
    while True:
        mode = input(
            "\nDo you want to PREVIEW changes first?\n"
            "Type 'yes' → Only show changes (SAFE)\n"
            "Type 'no'  → Rename files (REAL)\n"
            "Enter choice (yes/no): "
        ).lower()

        if mode in ["yes", "no"]:
            break
        else:
            print("❌ Invalid input! Please type 'yes' or 'no'.")

    rename_files(
        folder,
        extension,
        prefix,
        suffix,
        preview=(mode == "yes")
    )

    print("\nDone!")


if __name__ == "__main__":
    main() 