# lib-version

Version utility library with automatic versioning from Git tags.

## Quick Start

```bash
git clone https://github.com/remla25-team14/lib-version.git
cd lib-version
pip install -e .
```

## Usage

```python
from libversion import VersionUtil, __version__

# Get version
print(VersionUtil.get_version())  # 1.0.1.dev1+g28203f8
print(__version__)                # 1.0.1.dev1+g28203f8
```

## Features

- ✅ Automatic versioning from Git tags
- ✅ Two ways to access version
- ✅ Modern Python packaging

## Install from Git

```bash
pip install libversion @ git+https://github.com/remla25-team14/lib-version@v1.0.0
```

That's it! 🎉