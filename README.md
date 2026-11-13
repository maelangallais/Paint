# 🎨 Paint

A collection of interactive drawing and pixel-painting applications for the **NumWorks** calculator in MicroPython, including a full pixel-grid editor with flood fill and two earlier `turtle`-based drawing tools.

---

## 📂 Scripts Included

```
Paint/
├── paint.py                 # Full pixel-grid paint editor with RGB picker & flood fill
├── turtle_paint.py          # Turtle-based drawing tool with adjustable speed & brush size
└── turtle_paint_macros.py   # Turtle paint with preloaded shape/grid drawing macros
```

---

### 1. `paint.py` *(Created November 18, 2023)*
- **Pixel Grid & Resolution**: Configurable pixel scale via variable `m` (line 8, defaults to `3` to fit calculator memory limits).
- **RGB Color Picker & Eyedropper**: Adjust Red, Green, and Blue channels in steps of 5 with live color preview, or pick/copy an existing color directly from the canvas.
- **Flood Fill**: Fill enclosed regions or replace contiguous areas with the selected color.
- **Smart Cursor**: The selection square blinks between the active color and its inverse after 1 second so it remains visible over matching pixels.

### 2. `turtle_paint.py` *(Created March 31, 2023)*
- Freehand drawing powered by the `turtle` module, displaying live brush size and speed in the top-left corner.
- **Controls**: Arrows to move, `Toolbox` / `Backspace` (±1 size), `(` / `)` (±5 size), `×` / `÷` (±10 size), `π` / `tan` (speed), `0`–`9` & `.` (colors).

### 3. `turtle_paint_macros.py` *(Created March 15, 2023)*
- Early `turtle` paint variant featuring quick-draw macros: `Shift` (preset drawing), `Alpha` (full-screen grid), `X,N,T` (circle), `,` / `^` (show/hide turtle).

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `ion`, `turtle`, `time`).
