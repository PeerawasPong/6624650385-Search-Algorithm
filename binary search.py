import pyglet
import random

# หน้าต่าง 800*200
window = pyglet.window.Window(width=800, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# สร้างรายการด้วยตัวเลขสุ่มเพื่อให้แน่ใจว่ามี 42 รวมอยู่ด้วย
numbers = sorted(random.sample(range(1, 100), 19) + [42])

# ไล่หาตัวเลข
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 42:
            found = True
        elif numbers[mid] < 42:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

# รันทุกๆ0.5วินาที
pyglet.clock.schedule_interval(lambda dt: binary_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # กำหนดตำแหน่งและขนาดของแต่ละกล่อง
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # Draw the box
        if left <= i <= right and not search_complete:
            color = (153, 51, 255)  # สีม่วงคือกำลังเช็ค
        elif i == mid and not search_complete:
            color = (255, 0, 0)  # แดงคือเจอเลขอื่นที่ไม่ใช่42
        elif found and i == mid:
            color = (0, 255, 0)  # เขียวคือเจอเลข42
        else:
            color = (200, 200, 200)  # เทาคือยังไม่เช็คหรือผ่านไปแล้ว
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # ตัวเลขในกล่อง
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()