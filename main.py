from modulesync import sync


if __name__ == "__main__":
    changed_dir: str = input("Changed dir: ")
    source_dir: str = input("Source dir: ")
    sync(source_dir, changed_dir)
