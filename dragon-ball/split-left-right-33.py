import conf
from os import listdir

chapter = "ch-33"
source_path = conf.get_original_chapter_path(chapter)
target_path = conf.get_target_chapter_path(chapter)

f = listdir(source_path)
for filename in listdir(source_path):
    print(filename)
    im, basename = conf.get_source_file(source_path, filename)

    if basename in ("c13"):
        conf.copy_only(chapter, filename)
        continue

    ratio = 0.50
    if basename in ("a01", "a02", "a03", "a07", "a16", "b26", "b28"):
        ratio = 0.515
    elif basename in ("a30", "b16", "b20", "c20"):
        ratio = 0.505
    elif basename in ("c01", "d2"):
        ratio = 0.503
    elif basename in ("c05", "c07"):
        ratio = 0.495

    left_label = ""
    right_label = ""

    conf.split_and_save(target_path, basename, im, ratio, left_label, right_label)

conf.create_zip(chapter)
