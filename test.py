import shutil
import os

test_file = "\\\\ps-storage01\\Rebellion_films\\RVFX\\Others\\Arda\\testScenesForArda\\20_MS_1000\\20_MS_1000_ANM_Animation_v011.ma"
test_output = "\\\\ps-storage01\\Rebellion_films\\RVFX\\Others\\Arda\\testScenesForArda\\20_MS_1000\\testOutput.ma"
compare_line = "L:\\eg2\\"
target_root = "/mnt/ps-storage01/vfx_hgd_000/SG_ROOT/eg2/"

def _loadContent(filePath):
    f = open(filePath, "r")
    if f.mode == "r":
        contentList = f.readlines()
    else:
        return None
    f.close()
    return contentList

def _dumpContent(filePath, contentList, backup=False):
    # if backup:
    #     shutil.copyfile(filePath)
    name, ext = os.path.splitext(filePath)
    if backup:
        if os.path.isfile(filePath):
            backupFile = "{0}.bak".format(name)
            shutil.copyfile(filePath, backupFile)
            print("Backup complete\n%s => %s" %(filePath, backupFile))
    tempFile = "{0}_TMP{1}".format(name, ext)
    f = open(tempFile, "w+")
    f.writelines(contentList)
    f.close()
    shutil.copyfile(tempFile, filePath)
    os.remove(tempFile)

contents = _loadContent(test_file)

print("finito")
# print(contents)
type(contents)
print(contents[12])

for line in range(len(contents)):
    compare_line_forw = compare_line.replace("\\", "/")
    if compare_line_forw in contents[line]:
        print(contents[line])
        contents[line] = contents[line].replace(compare_line_forw, target_root)

_dumpContent(test_output, contents)