import conf
from os import listdir

chapter = "ch-18"
source_path = conf.get_original_chapter_path(chapter)
target_path = conf.get_target_chapter_path(chapter)

f = listdir(source_path)
for filename in listdir(source_path):
    print(filename)
    im, basename = conf.get_source_file(source_path, filename)

    ratio = 0.50
    if basename in ("a16", "b01", "b15", "b29", "c01", "c02"):
        ratio = 0.505
    elif basename in ("a18", "c03"):
        ratio = 0.495

    left_label = ""
    right_label = ""

    conf.split_and_save(target_path, basename, im, ratio, left_label, right_label)

conf.create_zip(chapter)
