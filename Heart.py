import turtle
import tkinter as tk
import math
import os
import sys
import argparse
from pathlib import Path
from PIL import Image

RAD2DEGREE = math.pi/180


def set_icon() -> None:
    root = turtle.Screen()._root

    IS_BUNDLED = hasattr(sys, "_MEIPASS")
    if IS_BUNDLED:  # if pyinstaller executible
        BUNDLE_DIR = getattr(
            sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__))
        )
        IMAGE_PATH = "Heart.png"
        imagepath = os.path.abspath(os.path.join(BUNDLE_DIR, IMAGE_PATH))
    else:
        imagepath = "./images/Heart.png"

    icon = tk.PhotoImage(file=imagepath)
    root.iconphoto(True, icon)


def save_gif(file: str | Path) -> None:
    assert file.suffix.lower() == '.gif'

    tmp = Path(__file__).parent / "tmp"
    print("Creating GIF file please be patient")
    eps_files = sorted(tmp.glob('*.eps'))
    # png_files = []
    # for f in eps_files:
    #     img = Image.open(f)
    #     png = f.parent / f"{f.stem}.png"
    #     img.save(png, "PNG")
    #     png_files.append(png)

    last_file = eps_files[-1]

    frames = [Image.open(f) for f in (eps_files[::10] + [last_file])]
    # last_frame = frames[-1]
    # frames = frames[::10] + last_frame
    if frames:
        # Use the first frame as the base
        frame_one = frames[0]
        frame_one.save(
            file,
            format='GIF',
            append_images=frames[1:],
            save_all=True,
            duration=0.001,  # Duration in milliseconds
            # loop=0  # 0 means loop forever
        )
        print(f"Created GIF from {len(frames)} frames.")
    else:
        print("No EPS files found.")


def heart1(angle: float = 50, length: float = 200, Title: str = "Love", message: str = None, fontsize: int = 24) -> None:
    """
    Makes heart with two full semi-circles at top
    """
    assert angle > 0 and angle <= 90

    screen = turtle.Screen()
    screen.setup(width=600, height=600)

    turtle.color('red')
    turtle.title(Title)
    set_icon()
    turtle.begin_fill()

    # calc variables
    circportion = 270 - angle
    radius = length*math.tan(((90-angle)/2)*RAD2DEGREE)

    # draw
    tmp = Path(__file__).parent / 'tmp'
    tmp.mkdir()
    i = 0

    turtle.setheading(angle)
    for _ in range(length):
        turtle.forward(1)
        turtle.getcanvas().postscript(file=tmp / f"step_{i:08d}.eps")
        i += 1
    for _ in range(circportion):
        turtle.circle(radius, 1)
        turtle.getcanvas().postscript(file=tmp / f"step_{i:08d}.eps")
        i += 1
    turtle.setheading(90)
    for _ in range(circportion):
        turtle.circle(radius, 1)
        turtle.getcanvas().postscript(file=tmp / f"step_{i:08d}.eps")
        i += 1
    turtle.setheading(360-angle)
    for _ in range(length):
        turtle.forward(1)
        turtle.getcanvas().postscript(file=tmp / f"step_{i:08d}.eps")
        i += 1

    turtle.hideturtle()
    turtle.end_fill()
    if message is not None:
        turtle.goto(0, 0)
        turtle.color('white')
        turtle.write(message, align='center', font=("Arial", fontsize, "bold"))
    turtle.getcanvas().postscript(file=tmp / f"step_{i+1:08d}.eps")
    turtle.done()


def heart2(angle: float = 50, inpointangle: float = 90, length: float = 200, Title: str = "Love", message: str = None, fontsize: int = 24) -> None:
    """
    Makes a heart with two semicircles at the top where the angle at the point where
    the semi-circles meet is inpointangle
    """
    assert angle > 0 and angle <= 90

    screen = turtle.Screen()
    screen.setup(width=int(2*length), height=int(2*length))

    turtle.color('red')
    turtle.title(Title)
    set_icon()
    turtle.begin_fill()

    # calc variables
    halfpointang = inpointangle/2
    circportion = int(270 - halfpointang - angle)
    radius = length*math.cos((angle*RAD2DEGREE)) / \
        (math.cos(halfpointang*RAD2DEGREE)+math.sin(angle*RAD2DEGREE))

    height = radius + radius * \
        math.cos(angle*RAD2DEGREE) + length*math.sin(angle*RAD2DEGREE)

    turtle.penup()
    turtle.setposition(turtle.position()[0], -height/2)
    turtle.pendown()

    # draw
    tmp = Path(__file__).parent / 'tmp'
    tmp.mkdir()
    i = 0

    turtle.setheading(angle)
    for _ in range(length):
        turtle.forward(1)
        turtle.getcanvas().postscript(file=tmp / f"step_{i:08d}.eps")
        i += 1
    for _ in range(circportion):
        turtle.circle(radius, 1)
        turtle.getcanvas().postscript(file=tmp / f"step_{i:08d}.eps")
        i += 1
    turtle.setheading(-turtle.heading())
    for _ in range(circportion):
        turtle.circle(radius, 1)
        turtle.getcanvas().postscript(file=tmp / f"step_{i:08d}.eps")
        i += 1
    turtle.setheading(360-angle)
    for _ in range(length):
        turtle.forward(1)
        turtle.getcanvas().postscript(file=tmp / f"step_{i:08d}.eps")
        i += 1

    turtle.hideturtle()
    turtle.end_fill()
    if message is not None:
        turtle.goto(0, 0)
        turtle.color('white')
        turtle.write(message, align='center', font=("Arial", fontsize, "bold"))
    turtle.getcanvas().postscript(file=tmp / f"step_{i+1:08d}.eps")
    turtle.done()


def make_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('gif', type=str,
                        help="Filename/path for the gif file to save the drawing to")
    parser.add_argument('--length', required=False, type=int, default=200,
                        help='Side length of the heart')
    parser.add_argument('--angle', required=False, type=int, default=50,
                        help='Initial heading of the drawing, must be between 0 and 90 degrees')
    parser.add_argument('--inpointangle', required=False, type=int, default=90,
                        help='Angle (in degrees) where the round parts meet in heart type 2')
    parser.add_argument('--title', required=False, type=str,
                        default='Love', help='Title to be displayed on the top of the window')
    parser.add_argument('--message', required=False, type=str,
                        default=None, help='Message to display in the window')

    heart_type = parser.add_mutually_exclusive_group(required=True)
    heart_type.add_argument('--heart1', action='store_true',
                            help="Draw heart type 1 which has two semi circles ontop")
    heart_type.add_argument('--heart2', action='store_true',
                            help="Draw heart type 1 which has two semi circles ontop")

    parser.add_argument('--fontsize', required=False, type=int,
                        default=24, help='Message to display in the window')
    return parser.parse_args()


if __name__ == '__main__':
    args = make_args()

    try:
        if args.heart1:
            heart1(args.angle, args.length, args.title, args.message)
        elif args.heart2:
            heart2(args.angle, args.inpointangle,
                   args.length, args.title, args.message)
        else:
            pass  # this should not happen

        save_gif(Path(args.gif).absolute().resolve())
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        tmp = Path(__file__).parent / 'tmp'

        # clean up
        eps_files = sorted(tmp.glob('*.eps'))
        for f in eps_files:
            f.unlink()
        tmp.rmdir()
