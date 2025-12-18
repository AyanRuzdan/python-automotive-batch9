'''
function to write to
specified TEXT_FILE
a given MESSAGE
'''
def write_file_log(text_file, message):
    with open(text_file, "a") as f:
        f.write(message + "\n")