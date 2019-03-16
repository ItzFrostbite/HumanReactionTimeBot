import win32gui, win32api, win32con, webbrowser
from time import sleep
def get_pixel_colour(i_x, i_y):
	i_desktop_window_id = win32gui.GetDesktopWindow()
	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
	i_colour = int(long_colour)
	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

tries = 0
red = 0
blue = 0
beggining = input("Press Enter To Run: ")
webbrowser.open('https://www.humanbenchmark.com/tests/reactiontime')
sleep(5)
click(1250,200)
sleep(0.1)
while True:
    color = get_pixel_colour(1250,200)
    if color == (75, 219, 106):
        print("Green")
        sleep(0.08)
        click(1250,200)
        sleep(0.1)
        print("Blue")
        sleep(0.1)
        tries += 1
        print("Tries:",tries)
        if tries == 5:
            exit = input("Press Enter To Exit: ")
            quit()
        elif tries < 5:
            sleep(2)
            click(1250,200)
    elif color == (43, 135, 209):
        if blue == 0:
            blue += 1
            red = 0
    elif color == (206, 38, 54):
        if red == 0:
            print("Red")
            red += 1
            blue = 0
