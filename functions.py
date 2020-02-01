def python_food():
    width = 80
    text = "Spam and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


with open("centered", mode='w') as centered_file:

    center_text("Spam and Eggs", file=centered_file)
    center_text("Spam, spam and Eggs", file=centered_file)
    center_text(12, file=centered_file)
    center_text("Spam, spam, spam and Eggs", file=centered_file)
    center_text("First", "Second", 3, 4, "Spam", file=centered_file)

