from PIL import Image, ImageEnhance



class ImageProcess:
    
    def __init__(self, img_path, has_sepia=False,has_grayscale=False) -> None:
        self.img_path = img_path
        self.image = Image.open(self.img_path)

        if has_sepia :
            self.sepia()
        
        if has_grayscale :
            self.grayscale()
    
    def contrast (self, num : float) : 
        enchancer = ImageEnhance.Contrast(self.image)
        self.image = enchancer.enhance(num)

    def brightness (self, num : float) : 
        enchancer = ImageEnhance.Brightness(self.image)
        self.image = enchancer.enhance(num)


    def sepia (self) :
        width, height = self.image.size

        pixels = self.image.load() # create the pixel map

        for py in range(height):
            for px in range(width):
                r, g, b = self.image.getpixel((px, py))

                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                if tr > 255:
                    tr = 255

                if tg > 255:
                    tg = 255

                if tb > 255:
                    tb = 255

                pixels[px, py] = (tr,tg,tb)


    def grayscale (self) : 
        self.image = self.image.convert('L')

    def saturate (self, sat_num : float) :
        converter = ImageEnhance.Color(self.image)
        self.image = converter.enhance(sat_num)

    def save (self) : 
        self.output_path = str(self.img_path).replace('original-images','done-images')
        self.image.save(self.output_path)

    def get_output (self) -> str: 
        img_name = self.output_path.split('\\')[-1]
        return f"/media/done-images/{img_name}"