import os
import zipfile
from pathlib import Path
from huggingface_hub import hf_hub_download

def ensure_file(
    local_path: str,
    repo_id: str,
    filename: str,
) -> str:
    """
    本地没有则从 Hugging Face 自动下载。
    """
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        print(f"使用本地数据: {local_path}", flush=True)
        return local_path

    print(f"本地未找到 {local_path}", flush=True)
    print(f"正在从 Hugging Face 下载: {filename}", flush=True)
    print(f"  repo: {repo_id}", flush=True)

    os.makedirs(os.path.dirname(local_path) or ".", exist_ok=True)

    downloaded = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        repo_type="dataset",
        local_dir=os.path.dirname(os.path.abspath(local_path)) or ".",
    )

    if os.path.abspath(downloaded) != os.path.abspath(local_path):
        if not os.path.exists(local_path):
            os.replace(downloaded, local_path)

    print(f"下载完成: {local_path}", flush=True)
    return local_path

def download_pdf():
    path = ensure_file('./data/pdf.zip', 'xiaochuan-dev/pdf', 'pdf.zip')

    zip_path = Path(path)
    output_dir = Path("./input")

    output_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)

    print("解压完成")