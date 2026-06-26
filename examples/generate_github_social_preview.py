from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


WIDTH = 1280
HEIGHT = 640
OUTPUT = Path(__file__).with_name("github-social-preview.png")


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    windows_fonts = Path("C:/Windows/Fonts")
    candidates = []
    if bold:
        candidates.extend(
            [
                windows_fonts / "msyhbd.ttc",
                windows_fonts / "msyhbd.ttf",
                windows_fonts / "seguisb.ttf",
                windows_fonts / "segoeuib.ttf",
            ]
        )
    candidates.extend(
        [
            windows_fonts / "msyh.ttc",
            windows_fonts / "msyh.ttf",
            windows_fonts / "segoeui.ttf",
            windows_fonts / "arial.ttf",
        ]
    )

    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def hex_color(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def draw_vertical_gradient(
    draw: ImageDraw.ImageDraw,
    top: tuple[int, int, int],
    bottom: tuple[int, int, int],
) -> None:
    for y in range(HEIGHT):
        ratio = y / (HEIGHT - 1)
        color = tuple(int(top[i] * (1 - ratio) + bottom[i] * ratio) for i in range(3))
        draw.line([(0, y), (WIDTH, y)], fill=color)


def draw_card(base: Image.Image) -> None:
    card = Image.new("RGBA", (1060, 500), (255, 255, 255, 0))
    card_draw = ImageDraw.Draw(card)

    card_draw.rounded_rectangle(
        (0, 0, 1060, 500),
        radius=28,
        fill=(248, 248, 245, 235),
        outline=(24, 24, 24, 26),
        width=2,
    )

    header_font = load_font(24)
    title_font = load_font(54, bold=True)
    body_font = load_font(25)
    chip_font = load_font(22, bold=True)
    mini_title_font = load_font(19, bold=True)
    mini_body_font = load_font(24, bold=True)

    card_draw.text((54, 44), "Codex Retro Studio / GitHub Social Preview", fill="#5F5F5B", font=header_font)

    title_lines = [
        "把 Codex 复盘、报告重组、",
        "长图 / 页面包装串成一条交付链",
    ]
    y = 108
    for line in title_lines:
        card_draw.text((54, y), line, fill="#151515", font=title_font)
        y += 68

    body_lines = [
        "不是只做“这周干了什么”，而是继续压成",
        "能汇报、能展示、能交接的复盘成品。",
    ]
    y = 252
    for line in body_lines:
        card_draw.text((54, y), line, fill="#5F5F5B", font=body_font)
        y += 38

    card_draw.rounded_rectangle((54, 344, 420, 392), radius=24, fill="#EAF1FF")
    card_draw.text((84, 356), "review -> report -> visual", fill="#2B62D9", font=chip_font)

    card_draw.rounded_rectangle(
        (446, 344, 636, 392),
        radius=24,
        fill=(255, 255, 255, 190),
        outline=(24, 24, 24, 28),
        width=1,
    )
    card_draw.text((482, 356), "适合公开展示", fill="#5F5F5B", font=chip_font)

    boxes = [
        ((54, 414, 350, 450), "#1F7A46", "真正产出", "不是聊天总结"),
        ((382, 414, 678, 450), "#A96A00", "结构重组", "不是信息堆砌"),
        ((710, 414, 1006, 450), "#5F5F5B", "继续交付", "不是停在复盘"),
    ]

    for (x1, y1, x2, y2), accent, mini_title, mini_body in boxes:
        card_draw.rounded_rectangle(
            (x1, y1 - 30, x2, y2 + 62),
            radius=18,
            fill=(255, 255, 255, 225),
            outline=(24, 24, 24, 22),
            width=1,
        )
        card_draw.text((x1 + 18, y1 - 10), mini_title, fill=accent, font=mini_title_font)
        card_draw.text((x1 + 18, y1 + 22), mini_body, fill="#151515", font=mini_body_font)

    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((110, 96, 1170, 596), radius=28, fill=(24, 24, 24, 32))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    base.alpha_composite(shadow)
    base.alpha_composite(card, (110, 96))


def draw_glow(base: Image.Image, box: tuple[int, int, int, int], color: tuple[int, int, int, int], blur: int) -> None:
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    layer_draw = ImageDraw.Draw(layer)
    layer_draw.ellipse(box, fill=color)
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))


def main() -> None:
    image = Image.new("RGBA", (WIDTH, HEIGHT), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)

    draw_vertical_gradient(draw, hex_color("#F7F7F5"), hex_color("#E9ECEF"))
    draw_glow(image, (-120, -80, 420, 320), (255, 255, 255, 180), 40)
    draw_glow(image, (880, 340, 1360, 760), (146, 174, 255, 90), 56)
    draw_glow(image, (760, -20, 1180, 300), (255, 238, 214, 80), 54)

    draw_card(image)
    image.convert("RGB").save(OUTPUT, quality=95)
    print(OUTPUT)


if __name__ == "__main__":
    main()
