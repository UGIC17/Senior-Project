from helper import *

def do_style_transfer():
    content_filename = 'test.jpg'
    content_image = load_image(content_filename, max_size=None)

    style_filename = 'style.jpg'
    style_image = load_image(style_filename, max_size=300)

    content_layer_ids = [4]

        # The VGG16-model has 13 convolutional layers.
        # This selects all those layers as the style-layers.
        # This is somewhat slow to optimize.
    #style_layer_ids = list(range(13))
    style_layer_ids = [1,3,5,7,9]
        # You can also select a sub-set of the layers, e.g. like this:
        # style_layer_ids = [1, 2, 3, 4]

    mg = style_transfer(content_image=content_image,
                            style_image=style_image,
                            content_layer_ids=content_layer_ids,
                            style_layer_ids=style_layer_ids,
                            weight_content=1.5,
                            weight_style=10.0,
                            weight_denoise=0.3,
                            num_iterations=100,
                            step_size=5)

do_style_transfer()
