import json
from datetime import datetime

class Logger:

    @staticmethod
    def info(category, message):
        print(f"[{category}] {message}")

    @staticmethod
    def warn(category, message):
        print(f"[WARN:{category}] {message}")

    @staticmethod
    def error(category, message):
        print(f"[ERROR:{category}] {message}")