import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from nodes import VersionUpdate

VersionUpdate().update_version()
timestamp = VersionUpdate().read_version()