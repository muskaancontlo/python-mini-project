import sys
import img2pdf
import os

def convert_to_pdf(filepath):
    output_file = "output.pdf"
    supported_formats = (".jpg", ".jpeg", ".png")

    if os.path.isdir(filepath):
        images = [os.path.join(filepath, fname) for fname in os.listdir(filepath)
                  if fname.lower().endswith(supported_formats) and os.path.isfile(os.path.join(filepath, fname))]
        if images:
            with open(output_file, "wb") as f:
                f.write(img2pdf.convert(images))
        else:
            print("No supported image files found in the directory.")
    elif os.path.isfile(filepath):
        if filepath.lower().endswith(supported_formats):
            with open(output_file, "wb") as f:
                f.write(img2pdf.convert(filepath))
        else:
            print("Unsupported file format. Please provide a JPG, JPEG, or PNG file.")
    else:
        print("Please input a valid file or directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_or_directory_path>")
    else:
        convert_to_pdf(sys.argv[1])
