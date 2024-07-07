import conf
from os import listdir

chapter = "ch-26"
source_path = conf.get_original_chapter_path(chapter)
target_path = conf.get_target_chapter_path(chapter)

f = listdir(source_path)
for filename in listdir(source_path):
    print(filename)
    im, basename = conf.get_source_file(source_path, filename)

    ratio = 0.50
    if basename in ("a20"):
        ratio = 0.49
    elif basename in ("a29", "b02", "b26", "b27", "b29", "c01", "c04"):
        ratio = 0.505
    elif basename in ("b13"):
        ratio = 0.495
    elif basename in ("b15", "c21", "d1"):
        ratio = 0.51

    left_label = ""
    right_label = ""

    conf.split_and_save(target_path, basename, im, ratio, left_label, right_label)

conf.create_zip(chapter)
