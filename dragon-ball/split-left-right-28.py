import conf
from os import listdir

chapter = "ch-28"
source_path = conf.get_original_chapter_path(chapter)
target_path = conf.get_target_chapter_path(chapter)

f = listdir(source_path)
for filename in listdir(source_path):
    print(filename)
    im, basename = conf.get_source_file(source_path, filename)

    if basename in ("c24"):
        conf.copy_only(chapter, filename)
        continue

    ratio = 0.50
    if basename in ("a01"):
        ratio = 0.51
    elif basename in ("b02"):
        ratio = 0.505

    left_label = ""
    right_label = ""

    conf.split_and_save(target_path, basename, im, ratio, left_label, right_label)

conf.create_zip(chapter)
