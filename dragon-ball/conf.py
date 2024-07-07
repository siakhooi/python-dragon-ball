import shutil
from os import path
from pathlib import Path

from PIL import Image

original_path = "original"
target_path = "target"

def get_original_chapter_path(chapter):
    return original_path + "/" + chapter

def get_target_chapter_path(chapter):
    target_chapter_path = target_path + "/" + chapter
    p = Path(target_chapter_path)
    if p.exists() and p.is_dir():
        shutil.rmtree(p)
    p.mkdir(parents=True, exist_ok=True)

    return target_chapter_path

def get_target_filename_left(target_path, basename, left_label):
    return target_path + "/" + basename + ".split-2-left" + left_label + ".jpeg"

def get_target_filename_right(target_path, basename, right_label):
    return target_path + "/" + basename + ".split-1-right" + right_label + ".jpeg"

def get_source_file(source_path, filename):
    source_file = source_path + "/" + filename
    im = Image.open(source_file)
    basename = path.splitext(filename)[0]
    return im, basename

def split_and_save(target_path, basename, im, ratio, left_label, right_label):
    left = get_target_filename_left(target_path, basename, left_label)
    right = get_target_filename_right(target_path, basename, right_label)

    mid = int(im.width * ratio)

    nim = im.crop((0, 0, mid, im.height - 1))
    nim.save(left)
    nim = im.crop((mid + 1, 0, im.width - 1, im.height - 1))
    nim.save(right)

def split_rotate_left_and_save(
    target_path, basename, im, ratio, left_label, right_label
):
    left = get_target_filename_left(target_path, basename, left_label)
    right = get_target_filename_right(target_path, basename, right_label)

    mid = int(im.width * ratio)

    nim = im.crop((0, 0, mid, im.height - 1))
    nim = nim.rotate(90, expand=True)
    nim.save(left)
    nim = im.crop((mid + 1, 0, im.width - 1, im.height - 1))
    nim.save(right)

def split_rotate_right_and_save(
    target_path, basename, im, ratio, left_label, right_label
):
    left = get_target_filename_left(target_path, basename, left_label)
    right = get_target_filename_right(target_path, basename, right_label)

    mid = int(im.width * ratio)

    nim = im.crop((0, 0, mid, im.height - 1))
    nim.save(left)
    nim = im.crop((mid + 1, 0, im.width - 1, im.height - 1))
    nim = nim.rotate(90, expand=True)
    nim.save(right)

def create_zip(chapter):
    target_chapter_path = target_path + "/" + chapter
    shutil.make_archive(target_chapter_path, "zip", target_path, chapter)

def copy_only(chapter, filename):
    shutil.copy(
        get_original_chapter_path(chapter) + "/" + filename, target_path + "/" + chapter
    )

def rotate_right(target_path, basename, im, label):
    nim = im.rotate(90, expand=True)
    filename = target_path + "/" + basename + label + ".jpeg"
    nim.save(filename)
