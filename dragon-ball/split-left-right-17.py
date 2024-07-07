import conf
from os import listdir

chapter = "ch-17"
source_path = conf.get_original_chapter_path(chapter)
target_path = conf.get_target_chapter_path(chapter)

f = listdir(source_path)
for filename in listdir(source_path):
    print(filename)
    im, basename = conf.get_source_file(source_path, filename)

    ratio = 0.50
    if basename in ("a12"):
        ratio = 0.51
    elif basename in ("a13", "a26", "c03"):
        ratio = 0.505

    left_label = ""
    right_label = ""
    if basename in ("a01"):
        right_label = "-blank"

    conf.split_and_save(target_path, basename, im, ratio, left_label, right_label)

conf.create_zip(chapter)
