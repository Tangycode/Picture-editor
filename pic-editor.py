from PIL import Image, ImageOps, ImageEnhance
import gradio as gr

def image_filter(img,bright,contrast,saturate,sharp):
  if img is None:
    return None
  img1 = ImageEnhance.Brightness(img).enhance(bright)
  img2 = ImageEnhance.Contrast(img1).enhance(contrast)
  img3 = ImageEnhance.Sharpness(img2).enhance(sharp)
  img4 = ImageEnhance.Color(img3).enhance(saturate)
  return img4

inter = gr.Interface(
    fn = image_filter,
    inputs = [gr.Image(type = 'pil', label = 'Upload an image'),
              gr.Slider(0,10, value = 1, label='Enter the brightness level'),
              gr.Slider(0,10, value = 1, label='Enter the contrast level'),
              gr.Slider(0,10, value = 1, label='Enter the saturate level'),
              gr.Slider(0,10, value = 1, label='Enter the sharpness level')],
    
    outputs = gr.Image(type = 'pil' , label = 'edited image'),
    title = 'Edited image'

)

inter.launch()
