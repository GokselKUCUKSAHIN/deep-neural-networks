from typing import List

from libs.os_utils import is_windows


def check_file_extension(path: str, filter_ext_list: List[str]) -> bool:
    for ext in filter_ext_list:
        if path.endswith(ext):
            return True
    return False


def filter_path(path_list: List[str], filter_ext_list: List[str]) -> List[str]:
    return [path for path in path_list if check_file_extension(path, filter_ext_list)]


def get_name_from_path(img_path: str) -> str:
    return img_path.split('\\' if is_windows() else '/')[-1].split(".")[0]
