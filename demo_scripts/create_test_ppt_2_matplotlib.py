import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Rectangle, Circle, FancyBboxPatch

def add_rectangle(ax, xy, width, height, text, facecolor, edgecolor="black", fontsize=10):
    """
    添加矩形框到绘图中
    """
    rect = Rectangle(xy, width, height, linewidth=1.5, edgecolor=edgecolor, facecolor=facecolor)
    ax.add_patch(rect)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha='center',
        va='center',
        fontsize=fontsize,
        color="black",
    )

def add_arrow(ax, xy_start, xy_end, color="black", width=0.02, head_width=0.1, head_length=0.2):
    """
    添加箭头
    """
    ax.annotate(
        "",
        xy=xy_end,
        xytext=xy_start,
        arrowprops=dict(arrowstyle="->", color=color, lw=1.5),
    )

def draw_framework():
    # 初始化绘图框架
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # ========================================================================
    # 定义尺寸
    rect_width, rect_height = 1.5, 0.8

    # ========================================================================
    # 绘制 View 1 和 View 2
    add_rectangle(ax, (1, 8), width=3, height=1.5, text="View 1\nView 2", facecolor="white")
    add_arrow(ax, (4, 8.75), (6, 8.75))  # 箭头 -> Clip

    # Clip 模块
    add_rectangle(ax, (6, 8.4), rect_width, rect_height, text="clip", facecolor="skyblue")

    # ========================================================================
    # VAE 和 Repeat 模块
    add_rectangle(ax, (1, 5.5), rect_width, rect_height, text="VAE", facecolor="skyblue")
    add_rectangle(ax, (4, 5.5), rect_width, rect_height, text="Repeat n times", facecolor="skyblue")
    add_arrow(ax, (2.5, 6), (4, 6))  # 箭头从 VAE -> Repeat

    # Noise Latents 和连接到 c
    add_rectangle(ax, (5.5, 4), rect_width, rect_height, text="Noise\nLatents", facecolor="skyblue")
    ax.add_patch(Circle((7.5, 4.5), radius=0.3, color="skyblue"))  # Circle for "c"
    ax.text(7.5, 4.5, "c", va="center", ha="center", fontsize=10, color="black")
    add_arrow(ax, (5, 5), (5.75, 4.75))  # Repeat -> latents
    add_arrow(ax, (6.75, 4.5), (7.2, 4.5))  # Noise Latents -> c

    # ========================================================================
    # Embedding 模块
    add_rectangle(ax, (8.8, 6.5), rect_width, rect_height, text="Embedding 1", facecolor="lightgreen")
    add_rectangle(ax, (8.8, 4.9), rect_width, rect_height, text="Embedding 2", facecolor="lightgreen")
    add_arrow(ax, (7.8, 4.5), (9.1, 6.9))
    add_arrow(ax, (7.8, 4.5), (9.1, 5.3))

    # ========================================================================
    # Conv Blocks 和后续模块
    add_rectangle(ax, (11, 6), rect_width, rect_height, text="Conv Blocks", facecolor="skyblue")
    add_arrow(ax, (9.6, 6.9), (11, 6.4))  # Embedding 1 -> Conv Blocks

    # Spatial Attention
    add_rectangle(ax, (12.5, 6), rect_width, rect_height, text="Spatial Att.", facecolor="lightcoral")
    add_arrow(ax, (11 + rect_width, 6.4), (12.5, 6.4))  # Conv Blocks -> Spatial Att

    # Temporal Attention
    add_rectangle(ax, (14, 6), rect_width, rect_height, text="Temporal Att.", facecolor="yellow")
    add_arrow(ax, (12.5 + rect_width, 6.4), (14, 6.4))  # Spatial Att -> Temporal Att

    # View Attention
    add_rectangle(ax, (15.5, 6), rect_width, rect_height, text="View Att.", facecolor="yellow")
    add_arrow(ax, (14 + rect_width, 6.4), (15.5, 6.4))  # Temporal Att -> View Att

    # ========================================================================
    # 展示结果
    plt.tight_layout()
    plt.show()


# 绘制框架图
draw_framework()