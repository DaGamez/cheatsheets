import os
import pandas as pd

def agregar_mapeo_directorio(path_, file_set=None, contador=0):
    if file_set is None:
        file_set = set()
    
    archivos_df = pd.DataFrame(columns=['file', 'size', 'file_directory'])

    for root, dirs, files in os.walk(path_):
        for d in dirs:
            directorio = os.path.join(root, d)
            archivos_df_temp, file_set, contador = agregar_mapeo_directorio(directorio, file_set, contador)
            archivos_df = pd.concat([archivos_df, archivos_df_temp], ignore_index=True)

        archivos_df_temp2 = pd.DataFrame(columns=['file', 'size', 'file_directory'])
        for f in files:
            directory = os.path.join(root, f)
            if directory not in file_set:
                try:
                    size = os.stat(directory).st_size / 1000000
                    new_row = pd.DataFrame({'file': f, 'size': size, 'file_directory': directory}, index=[0])
                    archivos_df_temp2 = pd.concat([archivos_df_temp2, new_row], ignore_index=True)
                    file_set.add(directory)
                    contador += 1  # Increment contador for each valid file
                    print("num arch: " + str(contador))  # Print contador for debug purposes
                except Exception as e:
                    new_row = pd.DataFrame({'file': f, 'size': 0, 'file_directory': directory}, index=[0])
                    archivos_df_temp2 = pd.concat([archivos_df_temp2, new_row], ignore_index=True)
                    file_set.add(directory)

        archivos_df = pd.concat([archivos_df, archivos_df_temp2], ignore_index=True)

    return archivos_df, file_set, contador

# Set the path to the directory
directory_path = "C:"

# Get the directory tree with file sizes and count
archivos_df, file_set, contador = agregar_mapeo_directorio(directory_path)

# Print final contador value
print("Total number of files processed:", contador)

# Optionally, write the directory tree with file sizes to a CSV file
archivos_df.to_excel('archivos_df.xlsx', index=False)
