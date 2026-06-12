import os

class ScoreProcessor:
    """A utility class that reads an integer score from a file and multiplies it by 10."""

    def process_score_file(self, file_path: str) -> int:
        file = None
        result = None

        try:
            file = open(file_path, 'r')
            content = file.read().strip()
            score = int(content)
            result = score * 10

        except FileNotFoundError:
            print(f"Error: File not found at path '{file_path}'. Please check the file path and try again.")
            raise

        except ValueError:
            print(f"Error: Invalid data in file '{file_path}'. Expected an integer but got non-numeric content.")
            raise

        else:
            print("Data processed successfully")

        finally:
            if file is not None:
                file.close()
            print("File cleanup completed")

        return result


# ── Demo ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    processor = ScoreProcessor()

    # --- Scenario 1: valid file ---
    valid_path = "score_valid.txt"
    with open(valid_path, 'w') as f:
        f.write("5")

    print("=" * 40)
    print("Scenario 1: Valid file (score = 5)")
    print("=" * 40)
    result = processor.process_score_file(valid_path)
    print(f"Result: {result}")
    os.remove(valid_path)

    print()

    # --- Scenario 2: missing file ---
    print("=" * 40)
    print("Scenario 2: File does not exist")
    print("=" * 40)
    try:
        processor.process_score_file("missing_file.txt")
    except FileNotFoundError:
        print("Caught: FileNotFoundError")

    print()

    # --- Scenario 3: invalid content ---
    bad_path = "score_bad.txt"
    with open(bad_path, 'w') as f:
        f.write("abc")

    print("=" * 40)
    print("Scenario 3: File has letters instead of number")
    print("=" * 40)
    try:
        processor.process_score_file(bad_path)
    except ValueError:
        print("Caught: ValueError")
    os.remove(bad_path)