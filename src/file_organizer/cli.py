import argparse
import os
from .core import organize_files
#from file_organizer.core import organize_files


def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory based on their extensions."
        
    )
    parser.add_argument(
        "directory",
        type=str,
        help="The path to the directory to organize."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without actually moving files."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output."
    )
    # Add more arguments as needed (e.g., --undo, --exclude-extensions)

    args = parser.parse_args()

    # Resolve the directory path to an absolute path for robustness
    target_directory = os.path.abspath(args.directory)

    organize_files(target_directory, dry_run=args.dry_run, verbose=args.verbose)

if __name__ == "__main__":
    main()