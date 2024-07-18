import pyautogui
import time


def reset_game():
    pyautogui.press('f2')

def get_region():
    print("Please move the mouse to the top-left corner of the region to capture and click.")
    time.sleep(2)

    # Capture the first click (top-left corner)
    top_left = pyautogui.position()
    
    print(f"Top-left corner selected at: {top_left}")

    # Give the user some time before capturing the second point
    time.sleep(1)
    print("Please move the mouse to the bottom-right corner of the region to capture and click.")
    time.sleep(2)

    # Capture the second click (bottom-right corner)
    bottom_right = pyautogui.position()
    
    print(f"Bottom-right corner selected at: {bottom_right}")

    # Define the region
    left = top_left.x
    top = top_left.y
    width = bottom_right.x - left
    height = bottom_right.y - top

    return left, top, width,height

def click_mine(left, top, patch_size, tile_number, offset_x, offset_y, rows, cols):
    top_left_mine_x = left + offset_x
    top_left_mine_y = top + offset_y
    row = (tile_number + 1) // rows
    col = (tile_number+ 1) % cols

    pos_x = top_left_mine_x + (patch_size * col) - (patch_size //2)
    pos_y = top_left_mine_y + (patch_size * row) + (patch_size //2)

    pyautogui.click(pos_x, pos_y )




def screen_grab(topleft, topright, bottomleft,bottomright):
    region = (topleft, topright, bottomleft,bottomright)

    screenshot = pyautogui.screenshot(region=region)

    return screenshot
