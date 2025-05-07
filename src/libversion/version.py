def get_version():
    """
    Reads the version number from the VERSION file and returns it as a string.
    """
    try:
        with open("VERSION", "r") as version_file:
            return version_file.read().strip()
    except FileNotFoundError:
        return "unknown"