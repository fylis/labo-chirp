import os
import bz2


def unzip_bz2_in_folder(folder_path):
    # Klasördeki tüm dosyaları al
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        # Sadece .bz2 uzantılı dosyaları seç
        if file_name.endswith(".bz2"):
            bz2_file_path = os.path.join(folder_path, file_name)

            # .bz2 uzantısını çıkararak hedef dosya ismini belirle
            # Örneğin "00.json.bz2" -> "00.json"
            output_file_path = bz2_file_path[:-4]  # ".bz2" 4 karakterli

            print(f"Extracting: {bz2_file_path} -> {output_file_path}")

            # bz2 dosyasını aç ve içeriğini hedefe yaz
            with bz2.open(bz2_file_path, "rb") as bz2_file, \
                    open(output_file_path, "wb") as output_file:
                # İçeriği parça parça okuyup yazabilirsiniz
                for chunk in iter(lambda: bz2_file.read(1024 * 1024), b''):
                    output_file.write(chunk)


if __name__ == "__main__":
    # Örnek kullanım: 23 klasöründeki bütün .bz2 dosyalarını aç
    unzip_bz2_in_folder("23")
