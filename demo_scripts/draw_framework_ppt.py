from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor


def add_rectangle(slide, left, top, width, height, text, color, font_size=16):
    """
    添加矩形框并设置文本和颜色
    """
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(*color)
    shape.line.color.rgb = RGBColor(0, 0, 0)  # 设置边框为黑色
    text_frame = shape.text_frame
    text_frame.text = text
    for paragraph in text_frame.paragraphs:
        paragraph.font.size = Pt(font_size)
        paragraph.font.bold = False
        paragraph.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体
    return shape


def add_arrow(slide, start_left, start_top, end_left, end_top):
    """
    添加箭头
    """
    connector = slide.shapes.add_connector(
        MSO_SHAPE.BENT_ARROW, start_left, start_top, end_left, end_top
    )
    connector.line.color.rgb = RGBColor(0, 0, 0)  # 黑色箭头
    connector.line.width = Pt(2.5)  # 设置箭头宽度
    return connector


def create_framework_ppt():
    # 创建演示文稿
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # 添加空白幻灯片

    # 定义矩形尺寸
    rect_width = Inches(1.5)
    rect_height = Inches(0.75)

    # 定义箭头偏移
    arrow_offset = Inches(0.3)

    # 添加框架图（框 + 箭头）

    # 文本部分
    text_rect = add_rectangle(slide, Inches(1), Inches(1), rect_width, rect_height, 
                               "Text", color=(255, 255, 255))
    bpe_tokenize_rect = add_rectangle(slide, Inches(3), Inches(1), rect_width, rect_height, 
                                      "BPE Tokenize", color=(135, 206, 250))  # 蓝色
    discrete_token_rect = add_rectangle(slide, Inches(5), Inches(1), rect_width, rect_height, 
                                        "Text Discrete\nTokens", color=(255, 255, 255))

    # 添加箭头
    add_arrow(slide, text_rect.left + rect_width, text_rect.top + rect_height / 2, 
              bpe_tokenize_rect.left, bpe_tokenize_rect.top + rect_height / 2)
    add_arrow(slide, bpe_tokenize_rect.left + rect_width, bpe_tokenize_rect.top + rect_height / 2, 
              discrete_token_rect.left, discrete_token_rect.top + rect_height / 2)

    # 图像部分
    image_rect = add_rectangle(slide, Inches(1), Inches(3), rect_width, rect_height, 
                               "Image", color=(255, 255, 255))
    vqvae_tokenize_rect = add_rectangle(slide, Inches(3), Inches(3), rect_width, rect_height, 
                                        "VQVAE Tokenize", color=(255, 165, 0))  # 橙色
    image_discrete_token = add_rectangle(slide, Inches(5), Inches(3), rect_width, rect_height, 
                                         "Image Discrete\nTokens", color=(255, 255, 255))

    # 添加箭头
    add_arrow(slide, image_rect.left + rect_width, image_rect.top + rect_height / 2, 
              vqvae_tokenize_rect.left, vqvae_tokenize_rect.top + rect_height / 2)
    add_arrow(slide, vqvae_tokenize_rect.left + rect_width, vqvae_tokenize_rect.top + rect_height / 2, 
              image_discrete_token.left, image_discrete_token.top + rect_height / 2)

    # Unified Token Space
    unified_token_space = add_rectangle(slide, Inches(7), Inches(2), Inches(2), Inches(1.5), 
                                        "Unified Token\nSpace\nLLMs", color=(211, 211, 211))  # 灰色
    add_arrow(slide, discrete_token_rect.left + rect_width, discrete_token_rect.top + rect_height / 2, 
              unified_token_space.left, unified_token_space.top + rect_height / 2)
    add_arrow(slide, image_discrete_token.left + rect_width, image_discrete_token.top + rect_height / 2, 
              unified_token_space.left, unified_token_space.top + rect_height / 2)

    # Detokenize部分
    bpe_detokenize = add_rectangle(slide, Inches(10), Inches(1), rect_width, rect_height, 
                                   "BPE Detokenize", color=(135, 206, 250))  # 蓝色
    vqvae_detokenize = add_rectangle(slide, Inches(10), Inches(3), rect_width, rect_height, 
                                     "VQVAE Detokenize", color=(255, 165, 0))  # 橙色
    add_arrow(slide, unified_token_space.left + Inches(2), unified_token_space.top + Inches(1), 
              bpe_detokenize.left, bpe_detokenize.top + rect_height / 2)
    add_arrow(slide, unified_token_space.left + Inches(2), unified_token_space.top + Inches(0.5), 
              vqvae_detokenize.left, vqvae_detokenize.top + rect_height / 2)

    # 输出部分
    output_text = add_rectangle(slide, Inches(12), Inches(1), rect_width, rect_height, 
                                 "Output Text", color=(255, 255, 255))
    output_image = add_rectangle(slide, Inches(12), Inches(3), rect_width, rect_height, 
                                  "Output Image", color=(255, 255, 255))
    add_arrow(slide, bpe_detokenize.left + rect_width, bpe_detokenize.top + rect_height / 2, 
              output_text.left, output_text.top + rect_height / 2)
    add_arrow(slide, vqvae_detokenize.left + rect_width, vqvae_detokenize.top + rect_height / 2, 
              output_image.left, output_image.top + rect_height / 2)

    # 保存PPT
    prs.save("framework_diagram.pptx")
    print("PPT 文件已生成：framework_diagram.pptx")


# 执行创建函数
create_framework_ppt()