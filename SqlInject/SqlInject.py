# @Author: 60dimension
# @Date: 2023/4/3 6:17 上午
import os

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml') :
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    if 'Mapper' in f.read():
                        f.seek(0, 0)
                        for i, line in enumerate(f):
                            if '$' in line:
                                print(f"{filepath}:{i+1}: {line.strip()}")

# Example usage
scan_directory('/Users/seckeep/IdeaProjects/lowsec')