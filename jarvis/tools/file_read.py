class FileReadTool:
    def __init__(self):
        pass

    def read_file(self, file_path):
        """Reads the content of a file given its path."""
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return str(e)