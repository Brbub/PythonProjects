from numba import jit
import arcade
import PIL
from threading import Thread

#Numba Array
#Change Iterations
#Pictures/Video(PIL)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"
@jit
def fractal_core(curx, cury):
    z = 0j
    c = curx + cury*1j
    for i in range(1200):
        z = z**2 + c
        if abs(z) > 2:
            break

    if i >= 254:
        color = 0
    else:
        color = (i << 21) + (i << 10) + i*8
    return color
class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title, antialiasing = False)

        arcade.set_background_color(arcade.color.AMAZON)
        self.originX, self.originY = 0.0, 0.0
        self.cY, self.cX = 0.27015, -0.7
        self.maxIter = 128
        self.zoom = 1.5
        self.x = 0
        self.y = 0
        self.color = 0
        self.xmin = -2.0
        self.xmax = 1.0
        self.ymin = -1.5
        self.ymax = 1.5

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        self.off_screen_image = PIL.Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), (128,128,128))
        self.bitmap = self.off_screen_image.load()  # Load the image into a writable byte object
        self.texture = arcade.Texture('background', self.off_screen_image)
        self.background_sprite = arcade.Sprite()
        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        self.background_sprite.texture = self.texture
        self.y = 1
        self.Drawing = False
        t = Thread(target = self.thread, daemon = True )
        t.start()
    def on_draw(self):
       
        arcade.start_render()
        self.background_sprite.draw()
        
        #print(self.x, self.y, self.color)
    def _point_to_screen(self, cx, cy):
        x = ((cx - self.xmin) * (SCREEN_WIDTH - 1)) / (self.xmax - self.xmin)
        y = ((cy - self.ymin) * (SCREEN_HEIGHT - 1)) / (self.ymax - self.ymin)
        return x, SCREEN_HEIGHT - y

    def _screen_to_point(self, x, y):
        cy = (SCREEN_HEIGHT - y) * (self.ymax - self.ymin) / (SCREEN_HEIGHT - 1) + self.ymin
        cx = x * (self.xmax - self.xmin) / (SCREEN_WIDTH - 1) + self.xmin
        return cx, cy

    def update(self, delta_time):
        self.texture = arcade.Texture('background', self.off_screen_image)
        self.background_sprite.texture = self.texture




    
    def thread(self):
        self.Drawing = True
        for x in range(SCREEN_WIDTH):
            for y in range(SCREEN_HEIGHT):   
                curx, cury = self._screen_to_point(x, y)
                color = fractal_core(curx, cury)
                self.bitmap[x, y] = color
        self.Drawing = False

    def on_key_press(self, key, key_modifiers):
        
        
            
        
        
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        

    def on_key_release(self, key, key_modifiers):
        #print(key_modifiers)
        if key == arcade.key.S:
            print("S")
            photo = arcade.window
            photo.save("C:\Users\Brandon\Desktop\Brandon B", ".jpeg")
                
            
        
        
        
        """
        Called whenever the user lets off a previously pressed key.
        """
        

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        
        
        cx, cy = self._screen_to_point(x, SCREEN_HEIGHT-y)
        height = self.ymax - self.ymin
        width = self.xmax - self.xmin
        if not self.Drawing :
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.xmax = cx + width/4
                self.xmin = cx - width/4
                self.ymax = cy + height/4
                self.ymin = cy - height/4
                t = Thread(target = self.thread, daemon = True )
                t.start()
            if button == arcade.MOUSE_BUTTON_RIGHT:    
                self.xmax = cx + width
                self.xmin = cx - width
                self.ymax = cy + height
                self.ymin = cy - height
                t = Thread(target = self.thread, daemon = True )
                t.start()

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
