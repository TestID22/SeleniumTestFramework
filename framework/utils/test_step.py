from contextlib import ContextDecorator

# TODO: Add ALlure + Logger
class TestStep(ContextDecorator):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"\nSTART STEP: {self.name}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"FAILED Step: {self.name} ")
            print(f"Error: {exc_val}")
        else:
            print(f"PASSED STEP: {self.name}")
        return False
