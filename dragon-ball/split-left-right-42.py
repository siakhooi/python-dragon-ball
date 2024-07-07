import conf
from os import listdir

chapter = "ch-42"
source_path = conf.get_original_chapter_path(chapter)
target_path = conf.get_target_chapter_path(chapter)

f = listdir(source_path)
for filename in listdir(source_path):
    print(filename)
    im, basename = conf.get_source_file(source_path, filename)

    if basename in ("h16"):
        label = "-rotate-right"
        conf.rotate_right(target_path, basename, im, label)
    else:
        conf.copy_only(chapter, filename)


conf.create_zip(chapter)
