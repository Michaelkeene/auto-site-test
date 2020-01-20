import os
import pandas as pd


cwd = os.getcwd()
print(len(cwd), cwd)
data = []
for path, folders, files in os.walk(cwd):
    folder_ext = path[len(cwd):]
    if len(folder_ext) > 0:
        if folder_ext[0] == "\\":
            good_shit = folder_ext[1:]
            # we got good shit unless we go deeper
            if good_shit.find("\\") == -1:
                temp_dict = {"major folder": good_shit, "minor folders": folders}
                data.append(temp_dict)

df = pd.DataFrame(data)
df = df.explode("minor folders")
df.dropna(inplace=True)
print(df.head())
df.to_csv("locationFolders.csv", index=False)



