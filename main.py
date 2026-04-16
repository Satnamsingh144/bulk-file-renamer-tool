import os

def rename_files(folder, prefix="",suffix="" , preview=True , extension):
   files=sorted(os.listdir(folder))
   count=1
   for file in files:
        old_path=os.path.join(folder,file)
        name,ext = os.splitext(file)
        new_name=f"{prefix}{name}{suffix}_{count}{ext}"
        new_path=os.path.join()
        if os.path.exists(new_path):
           print(f"⚠ Skipped (already exists): {new_name}")
           continue
        if extension:
            
 
            if preview:
                print(f"[PREVIEW] {file} → {new_name}")
            else:
                os.rename(old_path, new_path)
                print(f"Renamed: {file} → {new_name}")
                count += 1

def main():
    print("=== Bulk File Renamer Tool (Pro) ===")

    folder = input("Enter folder path: ")

    if not os.path.isdir(folder):
        print("Invalid folder path!")
        return

    prefix = input("Enter prefix (optional): ")
    suffix = input("Enter suffix (optional): ")
    while True:
        extensions=input("Do you want to rename an particular extension(yes/no): ").lower()
        if extensions=="yes":
            extension=input("Enter the particular extension you want(coma splited): ")
        elif extensions=="no":
            extension=""
            break
        else:
            continue

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

    if mode == "yes":
        rename_files(folder, prefix, suffix, preview=True,extension)
    else:
        rename_files(folder, prefix, suffix, preview=False)

    print("\nDone!")


if __name__ == "__main__":
    main()  
         
         
         

