import os

# Getting the size of the window to perfectly scale the bar.
window_size = os.get_terminal_size().columns

# Calculating some default sizes.
short = window_size * 0.25 - 5
medium = window_size * 0.5 - 5
maximum = window_size - 5

length = medium
auto_print = True


def progress_bar(split, total):
    progressbar_list = list()
    pb_string = str()
    percent = (split / total)

    length_of_black_bar = percent * length

    while length_of_black_bar > 0:
        progressbar_list.append("█")
        length_of_black_bar -= 1

    while len(progressbar_list) < length:
        progressbar_list.append("-")

    bar_string = f'{pb_string.join(progressbar_list)} {round(percent * 100)}% '

    if auto_print is True:
        print(bar_string)

    else:
        return bar_string


progress_bar(50, 500)
