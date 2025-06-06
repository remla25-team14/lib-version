from .version import VersionUtil

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

__all__ = ["VersionUtil", "__version__"]