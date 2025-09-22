# GIF Creator

## Overview
This project generates an animated GIF from a sequence of PNG images using Python and the [`imageio`](https://imageio.readthedocs.io/) library.  

There are two ways to use the script:
1. **Manual GIF Maker (main)** – list the image filenames yourself.  
2. **Pathlib (auto-pull)** – automatically gather all `.png` images from a folder.  

---

## Requirements
- Python 3.x  
- [imageio](https://pypi.org/project/imageio/)  
  Install with:
  ```bash
  pip install imageio
