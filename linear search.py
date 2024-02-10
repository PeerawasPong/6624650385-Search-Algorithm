import pyglet
import random

# หน้าต่าง 810*150
window = pyglet.window.Window(width=810, height=150, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

# สร้างรายการด้วยตัวเลขสุ่มเพื่อให้แน่ใจว่ามี 40 รวมอยู่ด้วย
numbers = random.sample(range(1, 100), 19) + [40]
random.shuffle(numbers)

# ไล่หาตัวเลข
current_index = 0
found_index = -1
search_complete = False

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 40:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

# รันทุกๆ0.5วินาที
pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # กำหนดตำแหน่งและขนาดของแต่ละกล่อง
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # สีกล่อง
        if i == current_index and not search_complete:
            color = (153, 51, 255)  # สีม่วงคือกำลังเช็ค
        elif i == found_index:
            color = (102, 204, 0)  # เขียวคือเจอเลข40
        else:
            color = (200, 200, 200)  # เทาคือยังไม่เช็คหรือผ่านไปแล้ว
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # ตัวเลขในกล่อง
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()