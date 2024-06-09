# Heart

Just a little coding project I made for my girlfriend ❤️

## Running

### Designing your Heart

In the `Heart.py` function there are two functions.

- `draw1` which works by drawing a heart with two full semi-circles at the top.
  - `angle` parameter to set initial angle in degrees from horizontal (must be between 0 and 90, default `50`)
  - `length` length of the straight side of the heart, default `200`
  - `Title` string name to label the window, default `Love`
- `draw2` Draws a heart with a variable angle between the two bulbs at the top of the heart.
  - `angle` parameter to set initial angle in degrees from horizontal (must be between 0 and 90, default `50`)
  - `inpointangle` the angle in degrees between the two bulbs at the top of the heart about their intersection point, default `90`
  - `length` length of the straight side of the heart, default `200`
  - `Title` string name to label the window, default `Love`

To costomize your heart call one of these functions in the main section of the file like so:

```python
if __name__ == '__main__':
    draw1(angle=50, length=400, Title='Love')
```
or
```python
if __name__ == '__main__':
    draw2(angle=50, inpointangle=70, length=400, Title='Love')
```

### Compiling Executable

Be sure to have python installed as well as the `turtle` and `pyinstaller`.

To install these if you do not have them, run `pip install turtle` and `pip install pyinstaller` for `turtle` and `pyinstaller` respectively.

Then run the following commands based on your operating system.

### Windows

```.\build.bat```

### MacOS

```./build.command```

## Final Product

After building, the executable file should be in the `/dist` directory. 

WARNING: You won't be able to send the executable file over email, so you will need to either transfer the file with a flash drive or clone this repo and run the commands.

