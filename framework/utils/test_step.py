from contextlib import ContextDecorator

class TestStep(ContextDecorator):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"\nStart step: {self.name}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Failed Step: {self.name} ")
            print(f"Error: {exc_val}")
        else:
            print(f"PASSED STEP: {self.name}")
        return False
