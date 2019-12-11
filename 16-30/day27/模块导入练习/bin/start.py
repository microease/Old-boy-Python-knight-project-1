import os
import sys
base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

from core import main

if __name__ == '__main__':
    main.entry_point()