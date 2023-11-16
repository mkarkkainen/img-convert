from PIL import Image
import os
import argparse

def convert_to_webp(input_path, output_dir):
    try:
        with Image.open(input_path) as img:
            output_filename = os.path.splitext(os.path.basename(input_path))[0] + ".webp"
            output_path = os.path.join(output_dir, output_filename)
            img.save(output_path, 'WEBP')
            print(f"Conversion successful. Image saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert JPG or PNG image to WebP format.')
    parser.add_argument('input', help='Input image file path (JPG or PNG)')
    parser.add_argument('--output', '-o', help='Output directory for the WebP image (default: current directory)', default='.')
    
    args = parser.parse_args()

    input_path = args.input
    output_dir = args.output

    if not os.path.exists(input_path):
        print("Error: Input file does not exist.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_extension = os.path.splitext(input_path)[1].lower()

    if file_extension not in ['.jpg', '.jpeg', '.png']:
        print("Error: Unsupported file format. Supported formats: JPG, JPEG, PNG")
        return

    convert_to_webp(input_path, output_dir)

if __name__ == "__main__":
    main()
