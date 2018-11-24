import os
import datetime

screen_shot_dir = r"C:\Users\Jerome\Documents\Ring of Elysium"
date_format = "%Y%m%d_%H%M%S_1"


def get_screen_shot_path():
    f = []
    for (dir_path, _, file_names) in os.walk(screen_shot_dir):
        for file_name in file_names:  # type: str
            if file_name.endswith('.png'):
                f.append(file_name)
        break

    f.sort()

    return os.path.join(dir_path, f[-1])


def main():
    print(get_screen_shot_path())


if __name__ == '__main__':
    main()