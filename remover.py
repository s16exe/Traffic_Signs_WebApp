import os

def delete_files_by_extension(directory, extension, dry_run=False):
    """
    Recursively deletes files with the specified extension in a directory and all its subdirectories.
    
    Args:
        directory (str): Path to the target directory
        extension (str): File extension to delete (e.g., '.tmp', '.log')
        dry_run (bool): If True, only shows what would be deleted without actual deletion
    """
    if not extension.startswith('.'):
        extension = '.' + extension
    
    deleted_count = 0
    error_count = 0

    try:
        for root, _, files in os.walk(directory):
            for filename in files:
                if filename.endswith(extension):
                    file_path = os.path.join(root, filename)
                    try:
                        if dry_run:
                            print(f"[Dry Run] Would delete: {file_path}")
                        else:
                            os.remove(file_path)
                            print(f"Deleted: {file_path}")
                        deleted_count += 1
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
                        error_count += 1
        
        print(f"\nResults:")
        print(f"Files deleted: {deleted_count}")
        print(f"Errors encountered: {error_count}")
        if dry_run:
            print("Note: Dry run mode was active - no files were actually deleted")
    
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found")
    except PermissionError:
        print(f"Error: No permission to access '{directory}'")

if __name__ == "__main__":
    target_dir = "/home/s16/Projects/traffic/Traffic_Signs_WebApp"
    ext = ".Identifier"
    
    # Safety features
    # print(f"\nWARNING: This will delete ALL {ext} files in {target_dir} and its subfolders!")
    confirm = "DELETE"
    
    if confirm == 'DELETE':
        # First do a dry run
        print("\n=== DRY RUN (showing what would be deleted) ===")
        delete_files_by_extension(target_dir, ext, dry_run=True)
        
        # Ask for final confirmation
        final_confirm = input("\nProceed with actual deletion? (y/n): ")
        if final_confirm.lower() == 'y':
            print("\n=== ACTUAL DELETION ===")
            delete_files_by_extension(target_dir, ext)
        else:
            print("Operation cancelled.")
    else:
        print("Operation cancelled.")