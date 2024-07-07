import conf
from os import listdir

chapter = "ch-27"
source_path = conf.get_original_chapter_path(chapter)
target_path = conf.get_target_chapter_path(chapter)

f = listdir(source_path)
for filename in listdir(source_path):
    print(filename)
    im, basename = conf.get_source_file(source_path, filename)

    ratio = 0.50
    if basename in ("a01"):
        ratio = 0.52
    elif basename in ("a08", "a13", "a19", "a24", "c01"):
        ratio = 0.51
    elif basename in ("a20", "a25", "b02"):
        ratio = 0.505
    elif basename in ("b01"):
        ratio = 0.515

    left_label = ""
    right_label = ""

    conf.split_and_save(target_path, basename, im, ratio, left_label, right_label)

conf.create_zip(chapter)
