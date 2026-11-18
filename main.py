
from pathlib import Path
import fitz

# =========================
# 配置
# =========================

PDF_PATH = Path("./input/李林.pdf")
OUTPUT_DIR = Path("./output/李林/images")

DPI = 250
IMAGE_FORMAT = "png"

# =========================
# PDF 转图片
# =========================

def pdf_to_images(pdf_path, output_dir, dpi=250):
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF 不存在: {pdf_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)

    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)

    total_pages = len(doc)

    print(f"PDF: {pdf_path}")
    print(f"总页数: {total_pages}")
    print(f"DPI: {dpi}")
    print("-" * 40)

    for page_index, page in enumerate(doc):
        pix = page.get_pixmap(
            matrix=matrix,
            colorspace=fitz.csRGB,
            alpha=False
        )

        output_path = (
            output_dir /
            f"page_{page_index + 1:04d}.{IMAGE_FORMAT}"
        )

        pix.save(str(output_path))

        print(
            f"[{page_index + 1}/{total_pages}] "
            f"{pix.width}x{pix.height} "
            f"-> {output_path.name}"
        )

    doc.close()

    print("-" * 40)
    print(f"完成！图片保存在: {output_dir.resolve()}")


if __name__ == "__main__":
    pdf_to_images(
        PDF_PATH,
        OUTPUT_DIR,
        dpi=DPI
    )
