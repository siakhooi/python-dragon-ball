import conf
from os import listdir

chapter = "ch-31"
source_path = conf.get_original_chapter_path(chapter)
target_path = conf.get_target_chapter_path(chapter)

f = listdir(source_path)
for filename in listdir(source_path):
    print(filename)
    im, basename = conf.get_source_file(source_path, filename)

    ratio = 0.50
    if basename in ("a01"):
        ratio = 0.51
    elif basename in( "c11"):
        ratio = 0.49

    left_label = ""
    right_label = ""

    if basename in ("c10"):
        right_label="-rotate90"
        conf.split_rotate_right_and_save(target_path, basename, im, ratio, left_label, right_label)
    else:
        conf.split_and_save(target_path, basename, im, ratio, left_label, right_label)

conf.create_zip(chapter)
