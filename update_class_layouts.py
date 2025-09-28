#!/usr/bin/env python3
"""
Simplified script to update class HTML files to match Slasher layout.
This script will update the skill tree section to use the segment-based structure.
"""

import os
import re
from pathlib import Path
import shutil
from datetime import datetime

# Get the script directory
SCRIPT_DIR = Path(__file__).parent.resolve()

# Class files to update (all except slasher which is our template)
CLASS_FILES = [
    'class_medic.html',
    'class_fixer.html', 
    'class_gunslinger.html',
    'class_exterminator.html',
    'class_hellraiser.html',
    'class_dronemaster.html',
    'class_vanguard.html'
]

def create_backup():
    """Create a backup of all class files before modification."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = SCRIPT_DIR / f'backup_{timestamp}'
    backup_dir.mkdir(exist_ok=True)
    
    for class_file in CLASS_FILES:
        src = SCRIPT_DIR / class_file
        if src.exists():
            dst = backup_dir / class_file
            shutil.copy2(src, dst)
            print(f"Backed up {class_file}")
    
    print(f"\nBackup created in: {backup_dir}")
    return backup_dir

def check_file_layout(filepath):
    """Check if a file has the old or new layout."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_old_grid = 'skill-tree-grid' in content
        has_skill_column = 'skill-column' in content
        has_new_segment = 'skill-segment' in content
        has_perk_card = 'perk-card' in content
        
        return {
            'has_old': has_old_grid or has_skill_column,
            'has_new': has_new_segment or has_perk_card
        }
    except Exception as e:
        print(f"Error checking {filepath}: {e}")
        return {'has_old': False, 'has_new': False}

def main():
    """Main function to check which files need updating."""
    print("=" * 60)
    print("WWZ Class File Layout Check")
    print("=" * 60)
    print(f"Working directory: {SCRIPT_DIR}\n")
    
    # First, check which files need updating
    files_to_update = []
    
    print("Checking file layouts...")
    print("-" * 40)
    
    for class_file in CLASS_FILES:
        filepath = SCRIPT_DIR / class_file
        if filepath.exists():
            layout = check_file_layout(filepath)
            
            if layout['has_old'] and not layout['has_new']:
                status = "❌ OLD LAYOUT - Needs update"
                files_to_update.append(class_file)
            elif layout['has_new']:
                status = "✅ NEW LAYOUT - Already updated"
            else:
                status = "⚠️  UNKNOWN - Manual check needed"
            
            print(f"{class_file}: {status}")
        else:
            print(f"{class_file}: ❌ FILE NOT FOUND")
    
    print("-" * 40)
    print(f"\nFiles needing update: {len(files_to_update)}")
    
    if files_to_update:
        print("\nFiles to update:")
        for f in files_to_update:
            print(f"  - {f}")
        
        print("\n" + "=" * 60)
        print("MANUAL UPDATE REQUIRED")
        print("=" * 60)
        print("\nThe skill tree sections in these files need to be manually updated")
        print("to match the segment-based layout used in class_slasher.html")
        print("\nKey changes needed:")
        print("1. Replace .skill-tree-grid with .skill-segment structure")
        print("2. Replace .skill-column with .perk-grid")
        print("3. Replace .perk-slot with .perk-card")
        print("4. Update CSS classes accordingly")
        print("\nRefer to class_slasher.html for the correct structure.")
        
        # Create backup
        response = input("\nCreate backup before making changes? (y/n): ")
        if response.lower() == 'y':
            create_backup()
    else:
        print("\n✅ All files are already using the new layout!")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
