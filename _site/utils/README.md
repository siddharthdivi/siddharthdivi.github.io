# Travel Portfolio Utilities

This directory contains utility scripts for managing your travel portfolio content.

## HEIC to JPG Conversion

Convert HEIC images to JPG format for web compatibility.

### macOS (Recommended)

Use the bash script with macOS's built-in `sips` tool:

```bash
./convert_heic_to_jpg.sh /path/to/heic/files
./convert_heic_to_jpg.sh /path/to/heic/files /path/to/output
```

**Features:**
- Uses macOS built-in `sips` tool (no additional dependencies)
- Interactive option to remove original HEIC files
- Error handling and progress reporting
- Batch conversion of all HEIC files in directory

### Cross-Platform

Use the Python script for other platforms:

```bash
python convert_heic_to_jpg.py /path/to/heic/files
python convert_heic_to_jpg.py /path/to/heic/files /path/to/output
```

**Requirements:**
```bash
pip install pillow pillow-heif
```

**Features:**
- Cross-platform compatibility
- Automatic method selection (sips on macOS, pillow on others)
- High-quality JPG output with optimization
- Batch conversion with progress reporting

## Usage Examples

### Convert images for a new trip:

1. **Create directory structure:**
   ```bash
   mkdir -p assets/images/hiking/Your_Trip_Name_Date
   ```

2. **Copy HEIC images:**
   ```bash
   cp /path/to/source/*.HEIC assets/images/hiking/Your_Trip_Name_Date/
   ```

3. **Convert to JPG:**
   ```bash
   ./utils/convert_heic_to_jpg.sh assets/images/hiking/Your_Trip_Name_Date
   ```

4. **Create trip page:**
   - Copy an existing trip markdown file
   - Update frontmatter with new trip details
   - Update image paths and gallery structure

### Batch processing multiple trips:

```bash
# Process all hiking trip directories
for dir in assets/images/hiking/*/; do
    if ls "$dir"*.HEIC 1> /dev/null 2>&1; then
        echo "Converting HEIC files in $dir"
        ./utils/convert_heic_to_jpg.sh "$dir"
    fi
done
```

## Tips

- Always backup original images before conversion
- Use descriptive directory names: `Trip_Name_Month_Year`
- Convert images before creating the markdown page
- Remove HEIC files after successful conversion to save space
- Use high-quality JPG settings (95% quality) for web display

## Troubleshooting

### macOS sips issues:
- Ensure you're running on macOS
- Check that `sips` command is available: `which sips`

### Python pillow issues:
- Install dependencies: `pip install pillow pillow-heif`
- On some systems, you may need to install system libraries for HEIF support

### Permission issues:
- Make scripts executable: `chmod +x convert_heic_to_jpg.*`
- Ensure write permissions on output directory

