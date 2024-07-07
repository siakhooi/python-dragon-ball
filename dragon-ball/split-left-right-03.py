import conf
from os import listdir

chapter = "ch-03"
source_path = conf.get_original_chapter_path(chapter)
target_path = conf.get_target_chapter_path(chapter)

f = listdir(source_path)
for filename in listdir(source_path):
    print(filename)
    im, basename = conf.get_source_file(source_path, filename)

    ratio = 0.50
    if basename == "a01":
        ratio = 0.48

    left_label = ""
    right_label = ""
    if basename in ("d1"):
        right_label = "-blank"

    if basename in ("d5"):
        left_label= "-rotate90"
        conf.split_rotate_left_and_save(target_path, basename, im, ratio, left_label, right_label)
    else:
        conf.split_and_save(target_path, basename, im, ratio, left_label, right_label)

conf.create_zip(chapter)
