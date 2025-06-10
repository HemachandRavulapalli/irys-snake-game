

# 🐍 Irys Snake Game

A custom snake game with a glowing hex background and animated food — themed after the Irys data network.

## ✨ Features

- Classic snake gameplay  
- Hex-tile styled grid background  
- Custom animated food  
- Themed snake body and corner shapes  
- Smooth gameplay with keyboard controls  

## 🎮 Controls

- Arrow keys / WASD to move  
- Eat food to grow and increase your score  
- Avoid hitting walls or yourself  

## 🖼 Media Folder

Make sure the `media/` folder contains:
- Resized `.gif` images for the snake head: `Up.gif`, `Down.gif`, `Left.gif`, `Right.gif`
- Snake body images: `Horizontal_.gif`, `Vertical.gif`
- Corner images: `Top_Right.gif`, `Bottom_Left.gif`, `Left_Top.gif`, `Right_Bottom_.gif`
- Food image: `food_resized.gif`
- Any additional `.gif` files used in `snake.py`

## 🚀 Run the Game

```bash
python snake.py
````

## 📦 Requirements

* Python 3.x
* Pillow (for image resizing)

Install Pillow if not already installed:

```bash
pip install pillow
```

## 📁 Folder Structure

```
Snake/
├── media/
│   ├── Up.gif
│   ├── Down.gif
│   ├── Left.gif
│   ├── Right.gif
│   ├── Horizontal_.gif
│   ├── Vertical.gif
│   ├── Top_Right.gif
│   ├── Bottom_Left.gif
│   ├── Left_Top.gif
│   ├── Right_Bottom_.gif
│   ├── food_resized.gif
│   └── ...
├── snake.py
├── resize.py
└── README.md
```
