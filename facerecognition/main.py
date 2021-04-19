import sys
import os

import webcam


def ensure_dir_exists(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def take_training_photos(name, n):
    for i in range(n):
        for face in webcam.capture().faces():
            normalized = face.gray().scale(100, 100)

            face_path = 'training_images/{}'.format(name)
            ensure_dir_exists(face_path)
            normalized.save_to('{}/{}.pgm'.format(face_path, i + 1))

            # normalized.show()


def parse_command():
    args = sys.argv[1:]
    return args[0] if args else None


def print_help():
    print("""Usage:
    train - takes 10 pictures from webcam to train software to recognize your
            face.
    detect - runs live detect. Captures images from webcam and tries to recognize
           faces.
    """)


def train():
    name = input('Enter your name: ')
    take_training_photos(name, 100)


def main():
    cmd = parse_command()
    if cmd == 'New':
        train()
    elif cmd == 'detect':
        webcam.display()
    else:
        print_help()


if __name__ == '__main__':
    main()
