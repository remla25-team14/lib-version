try:
    from ._version import version
except ImportError:
    # Fallback for development installations without setuptools-scm
    version = "unknown"


class VersionUtil:
    """Utility class to get version information."""
    
    @staticmethod
    def get_version():
        """
        Returns the version number derived from Git tags using setuptools-scm.
        
        Returns:
            str: The version string (e.g., "1.0.0" or "1.0.0.dev1+g1234567")
        """
        return version