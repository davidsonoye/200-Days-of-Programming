import os

def list_files(directory, indent=0):
    """
    Recursively lists all files and subdirectories in a given directory.
    
    Parameters:
    - directory (str): Path to the directory to explore.
    - indent (int): Used to format nested structure (optional).
    """
    try:
        items = os.listdir(directory)
    except PermissionError:
        print(" " * indent + f"Permission Denied: {directory}")
        return

    for item in items:
        full_path = os.path.join(directory, item)
        print(" " * indent + "|-- " + item)
        
        # If item is a directory, recurse
        if os.path.isdir(full_path):
            list_files(full_path, indent + 4)

# Example usage:
if __name__ == "__main__":
    root_path = "."  # Replace with your desired path
    print(f"Listing files in directory: {root_path}\n")
    list_files(root_path)
