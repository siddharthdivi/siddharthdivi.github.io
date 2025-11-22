#!/usr/bin/env python3
"""
HEIC to JPG Conversion Utility
Cross-platform script to convert HEIC images to JPG format

Requirements:
- macOS: Uses sips (built-in)
- Other platforms: Requires pillow and pillow-heif

Usage:
    python convert_heic_to_jpg.py <input_directory> [output_directory]
    
Examples:
    python convert_heic_to_jpg.py /path/to/heic/files
    python convert_heic_to_jpg.py /path/to/heic/files /path/to/output
"""

import os
import sys
import subprocess
import platform

def check_sips_available():
    """Check if sips is available (macOS only)"""
    try:
        subprocess.run(['sips', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def convert_with_sips(input_dir, output_dir):
    """Convert HEIC to JPG using macOS sips"""
    heic_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.heic')]
    
    if not heic_files:
        print("No HEIC files found in the directory")
        return 0, 0
    
    print(f"Found {len(heic_files)} HEIC files to convert")
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    print("")
    
    converted = 0
    failed = 0
    
    for filename in heic_files:
        input_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + '.jpg'
        output_path = os.path.join(output_dir, output_filename)
        
        print(f"Converting: {filename} -> {output_filename}")
        
        try:
            # Use sips to convert
            result = subprocess.run([
                'sips', '-s', 'format', 'jpeg', 
                input_path, '--out', output_path
            ], capture_output=True, text=True)
            
            if result.returncode == 0 and os.path.exists(output_path):
                print(f"✓ Successfully converted: {filename}")
                converted += 1
            else:
                print(f"✗ Failed to convert: {filename}")
                failed += 1
                
        except Exception as e:
            print(f"✗ Error converting {filename}: {str(e)}")
            failed += 1
    
    return converted, failed

def convert_with_pillow(input_dir, output_dir):
    """Convert HEIC to JPG using Python pillow (requires pillow-heif)"""
    try:
        from PIL import Image
        import pillow_heif
        
        # Register HEIF opener with Pillow
        pillow_heif.register_heif_opener()
        
    except ImportError:
        print("Error: pillow-heif is required for HEIC conversion on this platform.")
        print("Install with: pip install pillow pillow-heif")
        return 0, 0
    
    heic_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.heic')]
    
    if not heic_files:
        print("No HEIC files found in the directory")
        return 0, 0
    
    print(f"Found {len(heic_files)} HEIC files to convert")
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    print("")
    
    converted = 0
    failed = 0
    
    for filename in heic_files:
        input_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + '.jpg'
        output_path = os.path.join(output_dir, output_filename)
        
        print(f"Converting: {filename} -> {output_filename}")
        
        try:
            # Open HEIC file
            with Image.open(input_path) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Save as JPG
                img.save(output_path, 'JPEG', quality=95, optimize=True)
                print(f"✓ Successfully converted: {filename}")
                converted += 1
                
        except Exception as e:
            print(f"✗ Error converting {filename}: {str(e)}")
            failed += 1
    
    return converted, failed

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_heic_to_jpg.py <input_directory> [output_directory]")
        print("Examples:")
        print("  python convert_heic_to_jpg.py /path/to/heic/files")
        print("  python convert_heic_to_jpg.py /path/to/heic/files /path/to/output")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else input_dir
    
    # Validate input directory
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        print(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir)
    
    print("HEIC to JPG Conversion Utility")
    print("=" * 40)
    
    # Choose conversion method based on platform
    if platform.system() == "Darwin" and check_sips_available():
        print("Using macOS sips for conversion...")
        converted, failed = convert_with_sips(input_dir, output_dir)
    else:
        print("Using Python pillow for conversion...")
        converted, failed = convert_with_pillow(input_dir, output_dir)
    
    print("")
    print("Conversion complete!")
    print(f"Successfully converted: {converted} files")
    if failed > 0:
        print(f"Failed conversions: {failed} files")

if __name__ == "__main__":
    main()

