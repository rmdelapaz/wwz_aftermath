#!/usr/bin/env python3
"""
Script to standardize all WWZ class HTML files to match the Slasher layout.
This will update the skill tree sections to use the cleaner segment-based structure.
Supports WSL pathing.
"""

import os
import re
from pathlib import Path
import shutil
from datetime import datetime

# Get the script directory - handles WSL paths
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

# Data files for each class
DATA_FILES = {
    'class_medic.html': 'medic_data.txt',
    'class_fixer.html': 'fixer_data.txt',
    'class_gunslinger.html': 'gunslinger_data.txt',
    'class_exterminator.html': 'exterminator_data.txt',
    'class_hellraiser.html': 'hellraiser_data.txt',
    'class_dronemaster.html': 'dronemaster_data.txt',
    'class_vanguard.html': 'vanguard_data.txt'
}

# Class-specific colors and details
CLASS_INFO = {
    'medic': {
        'gradient': 'linear-gradient(135deg, #28a745 0%, #20c997 100%)',
        'primary_color': '#28a745',
        'title': '🏥 Medic Class Guide',
        'icon': '🏥',
        'roles': ['Combat Medic', 'Team Support', 'Healing Specialist'],
        'core_role': 'Keep your team alive with healing stims and protective equipment'
    },
    'fixer': {
        'gradient': 'linear-gradient(135deg, #6f42c1 0%, #563d7c 100%)',
        'primary_color': '#6f42c1',
        'title': '🔧 Fixer Class Guide',
        'icon': '🔧',
        'roles': ['Support Specialist', 'Equipment Master', 'Team Buffer'],
        'core_role': 'Supply team with explosive ammo and masking gas for tactical advantages'
    },
    'gunslinger': {
        'gradient': 'linear-gradient(135deg, #dc3545 0%, #c82333 100%)',
        'primary_color': '#dc3545',
        'title': '🔫 Gunslinger Class Guide',
        'icon': '🔫',
        'roles': ['DPS Specialist', 'Precision Shooter', 'Ammo Efficient'],
        'core_role': 'Maximize damage output with enhanced weapon handling and headshot bonuses'
    },
    'exterminator': {
        'gradient': 'linear-gradient(135deg, #fd7e14 0%, #e8590c 100%)',
        'primary_color': '#fd7e14',
        'title': '💥 Exterminator Class Guide',
        'icon': '💥',
        'roles': ['Crowd Control', 'Explosive Expert', 'Defense Specialist'],
        'core_role': 'Clear swarms with molotovs, claymores, and defensive bonuses'
    },
    'hellraiser': {
        'gradient': 'linear-gradient(135deg, #e83e8c 0%, #d91a72 100%)',
        'primary_color': '#e83e8c',
        'title': '🔥 Hellraiser Class Guide',
        'icon': '🔥',
        'roles': ['Explosive DPS', 'Area Denial', 'Heavy Weapons'],
        'core_role': 'Rain destruction with C4, improved explosives, and heavy weapons'
    },
    'dronemaster': {
        'gradient': 'linear-gradient(135deg, #4a90e2 0%, #357abd 100%)',
        'primary_color': '#4a90e2',
        'title': '🤖 Dronemaster Class Guide',
        'icon': '🤖',
        'roles': ['Support DPS', 'Tactical Control', 'Team Buffer'],
        'core_role': 'Deploy an autonomous Quadrocopter drone for continuous support fire and team advantages'
    },
    'vanguard': {
        'gradient': 'linear-gradient(135deg, #17a2b8 0%, #138496 100%)',
        'primary_color': '#17a2b8',
        'title': '🛡️ Vanguard Class Guide',
        'icon': '🛡️',
        'roles': ['Tank', 'Shield Bearer', 'Team Protector'],
        'core_role': 'Lead from the front with an electric shield that stuns and blocks zombies'
    }
}

def parse_data_file(filepath):
    """Parse the class data file to extract perk information."""
    perks = {
        'core': None,
        'segments': {},
        'prestige': []
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse sections (this is a simplified parser - you may need to adjust based on actual data format)
        lines = content.split('\n')
        current_level = 0
        
        for i, line in enumerate(lines):
            # Skip empty lines and headers
            if not line.strip() or 'Perks List' in line or 'Level\tPerk' in line:
                continue
                
            # Look for level indicators
            if line.strip().isdigit() or re.match(r'^\d+\s+', line):
                # Extract level number
                level_match = re.match(r'^(\d+)', line.strip())
                if level_match:
                    current_level = int(level_match.group(1))
        
        return perks
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return perks

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
            print(f"Backed up {class_file} to {backup_dir}")
    
    return backup_dir

def extract_skill_tree_content(html_content, class_name):
    """Extract the current skill tree content from HTML."""
    # Find the skill tree section
    skill_tree_match = re.search(
        r'<section[^>]*>.*?<h2>[^<]*(?:Skill Tree|Complete.*?Skill Tree)[^<]*</h2>.*?</section>',
        html_content,
        re.DOTALL | re.IGNORECASE
    )
    
    if skill_tree_match:
        return skill_tree_match.group(0)
    return None

def extract_prestige_content(html_content):
    """Extract the prestige perks section from HTML."""
    prestige_match = re.search(
        r'<section[^>]*>.*?<h2>[^<]*Prestige[^<]*</h2>.*?</section>',
        html_content,
        re.DOTALL | re.IGNORECASE
    )
    
    if prestige_match:
        return prestige_match.group(0)
    return None

def get_slasher_styles():
    """Extract the Slasher-specific styles to use as template."""
    return """
        /* Skill Tree Styling */
        .skill-tree-container {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 2rem;
            margin: 2rem 0;
            overflow-x: auto;
        }
        
        .skill-segment {
            background: white;
            border-radius: 8px;
            padding: 1rem;
            margin: 1.5rem 0;
            border-left: 4px solid {PRIMARY_COLOR};
        }
        
        .skill-segment h4 {
            color: #495057;
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }
        
        .perk-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1rem;
        }
        
        .perk-card {
            background: white;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            padding: 1rem;
            transition: transform 0.2s;
        }
        
        .perk-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .perk-level {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            background: {PRIMARY_COLOR};
            color: white;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        .perk-name {
            font-weight: bold;
            color: #495057;
            margin: 0.5rem 0;
        }
        
        .perk-desc {
            color: #6c757d;
            font-size: 0.9rem;
            line-height: 1.4;
        }
        
        .perk-cost {
            display: flex;
            justify-content: space-between;
            margin-top: 0.75rem;
            padding-top: 0.75rem;
            border-top: 1px solid #e9ecef;
            font-size: 0.85rem;
        }
        
        .core-perk {
            background: #ffe4e1;
            border: 2px solid {PRIMARY_COLOR};
        }
        
        .prestige-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            margin: 2rem 0;
        }
        
        .prestige-section h3 {
            color: white;
            margin-bottom: 1.5rem;
        }
        
        .prestige-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1rem;
        }
        
        .prestige-perk {
            background: rgba(255, 255, 255, 0.95);
            color: #333;
            padding: 1rem;
            border-radius: 8px;
            border: 2px solid #9b59b6;
        }
        
        .prestige-rank {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            background: #9b59b6;
            color: white;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }"""

def update_class_file(class_file):
    """Update a single class file to match the Slasher layout."""
    filepath = SCRIPT_DIR / class_file
    class_key = class_file.replace('class_', '').replace('.html', '')
    
    if class_key not in CLASS_INFO:
        print(f"No class info found for {class_key}, skipping...")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        info = CLASS_INFO[class_key]
        
        # Update the class header gradient
        content = re.sub(
            r'\.class-header\s*\{[^}]*background:\s*linear-gradient[^;]+;',
            f'.class-header {{\n            background: {info["gradient"]};',
            content
        )
        
        # Get the slasher styles and customize for this class
        new_styles = get_slasher_styles()
        new_styles = new_styles.replace('{PRIMARY_COLOR}', info['primary_color'])
        
        # Find the style section and update it
        style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
        if style_match:
            old_styles = style_match.group(1)
            
            # Remove old skill tree related styles
            old_styles = re.sub(
                r'/\*\s*Skill Tree Styling\s*\*/.*?(?=/\*|$)',
                '',
                old_styles,
                flags=re.DOTALL
            )
            
            # Add new styles
            new_style_section = f"<style>{old_styles}\n{new_styles}\n    </style>"
            content = re.sub(r'<style>.*?</style>', new_style_section, content, flags=re.DOTALL)
        
        # Update the class header section with proper title and roles
        header_pattern = r'<header class="class-header">.*?</header>'
        header_replacement = f'''<header class="class-header">
            <h1>{info["icon"]} {info["title"].replace(" Class Guide", "")} Class Guide</h1>
            <div class="role-badges">
                {''.join(f'<span class="role-badge">{role}</span>' for role in info["roles"])}
            </div>
            <p><strong>Core Role:</strong> {info["core_role"]}</p>
        </header>'''
        
        content = re.sub(header_pattern, header_replacement, content, flags=re.DOTALL)
        
        # Save the updated file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated {class_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {class_file}: {e}")
        return False

def main():
    """Main function to standardize all class files."""
    print("=" * 60)
    print("WWZ Class File Layout Standardization Script")
    print("=" * 60)
    print(f"Working directory: {SCRIPT_DIR}")
    print()
    
    # Create backup
    print("Creating backup...")
    backup_dir = create_backup()
    print(f"Backup created in: {backup_dir}")
    print()
    
    # Update each class file
    print("Updating class files...")
    success_count = 0
    
    for class_file in CLASS_FILES:
        if update_class_file(class_file):
            success_count += 1
    
    print()
    print("=" * 60)
    print(f"Update complete! {success_count}/{len(CLASS_FILES)} files updated successfully.")
    print(f"Backup saved in: {backup_dir}")
    print("=" * 60)

if __name__ == "__main__":
    main()
