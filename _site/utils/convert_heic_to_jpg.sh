#!/bin/bash

# HEIC to JPG Conversion Script
# Usage: ./convert_heic_to_jpg.sh [input_directory] [output_directory]
# If output_directory is not provided, converts in place

# Function to display usage
usage() {
    echo "Usage: $0 [input_directory] [output_directory]"
    echo "  input_directory: Directory containing HEIC files"
    echo "  output_directory: Directory to save JPG files (optional, defaults to input_directory)"
    echo ""
    echo "Examples:"
    echo "  $0 /path/to/heic/files"
    echo "  $0 /path/to/heic/files /path/to/output"
    echo ""
    echo "This script converts all HEIC files in the input directory to JPG format using macOS sips."
}

# Check if sips is available
if ! command -v sips &> /dev/null; then
    echo "Error: sips command not found. This script requires macOS."
    exit 1
fi

# Check arguments
if [ $# -eq 0 ]; then
    echo "Error: No input directory provided."
    usage
    exit 1
fi

if [ $# -gt 2 ]; then
    echo "Error: Too many arguments."
    usage
    exit 1
fi

INPUT_DIR="$1"
OUTPUT_DIR="${2:-$INPUT_DIR}"

# Validate input directory
if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Input directory '$INPUT_DIR' does not exist."
    exit 1
fi

# Create output directory if it doesn't exist
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Creating output directory: $OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create output directory '$OUTPUT_DIR'"
        exit 1
    fi
fi

echo "Converting HEIC images to JPG format..."
echo "Input directory: $INPUT_DIR"
echo "Output directory: $OUTPUT_DIR"
echo ""

# Change to the input directory
cd "$INPUT_DIR"

# Count HEIC files
heic_count=$(ls -1 *.HEIC 2>/dev/null | wc -l)
if [ $heic_count -eq 0 ]; then
    echo "No HEIC files found in '$INPUT_DIR'"
    exit 0
fi

echo "Found $heic_count HEIC files to convert"
echo ""

# Convert all HEIC files to JPG
converted=0
failed=0

for file in *.HEIC; do
    if [ -f "$file" ]; then
        # Get filename without extension
        filename="${file%.*}"
        output_file="$OUTPUT_DIR/${filename}.jpg"
        
        echo "Converting: $file -> ${filename}.jpg"
        
        # Convert using sips
        sips -s format jpeg "$file" --out "$output_file" > /dev/null 2>&1
        
        # Check if conversion was successful
        if [ $? -eq 0 ] && [ -f "$output_file" ]; then
            echo "✓ Successfully converted: $file"
            ((converted++))
        else
            echo "✗ Failed to convert: $file"
            ((failed++))
        fi
    fi
done

echo ""
echo "Conversion complete!"
echo "Successfully converted: $converted files"
if [ $failed -gt 0 ]; then
    echo "Failed conversions: $failed files"
fi

# Optional: Ask if user wants to remove HEIC files
if [ $converted -gt 0 ]; then
    echo ""
    read -p "Would you like to remove the original HEIC files? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing HEIC files..."
        rm *.HEIC
        echo "HEIC files removed."
    fi
fi
