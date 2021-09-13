import os

sources_path = "./"
exclusions = [""]

sources = os.listdir(sources_path)
sources_to_format = []

for source_file in sources:
    if source_file.endswith(".py"):
        if source_file not in exclusions:
            print("Found file '%s'" % source_file)

            sources_to_format.append(source_file)
        else:
            print("Found excluded file '%s'" % source_file)

files_to_format = ' '.join(sources_to_format)

print("Formatting file(s) '%s'" % files_to_format)

os.system("black %s" % files_to_format)
