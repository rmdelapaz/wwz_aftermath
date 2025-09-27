#!/usr/bin/env python3
"""
World War Z Site Phase 1 Improvements Script
Handles: JS file copying, HTML standardization, navigation fixes, style consolidation
Modified for Windows WSL path compatibility
"""

import os
import re
import shutil
from pathlib import Path, PureWindowsPath, PurePosixPath
from bs4 import BeautifulSoup, Comment
import json
from datetime import datetime
import platform
import sys

class WWZSiteImprover:
    def __init__(self, base_path):
        # Handle Windows WSL paths properly
        self.base_path = self.normalize_path(base_path)
        
        # Get parent directory for course_template
        parent_dir = self.base_path.parent
        self.course_template_path = parent_dir / 'course_template'
        
        # Create backup directory name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.backup_dir = self.base_path / f'backup_{timestamp}'
        
        self.inline_styles = []
        self.pages_processed = 0
        self.errors = []
        
        # Check if we're on Windows or WSL
        self.is_windows = platform.system() == 'Windows' or 'microsoft' in platform.uname().release.lower()
        
        print(f"📍 Working directory: {self.base_path}")
        print(f"📍 Course template: {self.course_template_path}")
        print(f"🖥️  Platform: {'Windows/WSL' if self.is_windows else 'Unix/Linux'}")
        
        # Define the standard navigation structure
        self.nav_structure = {
            'main_links': [
                {'text': 'Home', 'href': 'index.html'},
                {'text': 'Beginner Guide', 'href': 'beginner_guide.html'},
                {'text': 'Classes', 'href': 'classes_overview.html', 'dropdown': True},
                {'text': 'Weapons', 'href': 'weapons_upgrades.html'},
                {'text': 'Progression', 'href': 'currencies_progression.html'},
                {'text': 'Endgame', 'href': 'horde_endgame.html'}
            ],
            'class_links': [
                {'text': 'Overview', 'href': 'classes_overview.html'},
                {'text': 'Medic', 'href': 'class_medic.html'},
                {'text': 'Fixer', 'href': 'class_fixer.html'},
                {'text': 'Gunslinger', 'href': 'class_gunslinger.html'},
                {'text': 'Exterminator', 'href': 'class_exterminator.html'},
                {'text': 'Slasher', 'href': 'class_slasher.html'},
                {'text': 'Hellraiser', 'href': 'class_hellraiser.html'},
                {'text': 'Dronemaster', 'href': 'class_dronemaster.html'},
                {'text': 'Vanguard', 'href': 'class_vanguard.html'}
            ]
        }
    
    def normalize_path(self, path_str):
        """Normalize path for Windows WSL compatibility"""
        # Convert string to Path object
        if isinstance(path_str, str):
            # Handle WSL paths (\\wsl$\... or \\wsl.localhost\...)
            if path_str.startswith('\\\\wsl'):
                # Keep as is, Path can handle it
                return Path(path_str)
            # Handle regular Windows paths
            elif '\\' in path_str or ':' in path_str:
                return Path(path_str)
            # Handle Unix paths
            else:
                return Path(path_str)
        return Path(path_str)
    
    def create_backup(self):
        """Create a backup of the entire site before making changes"""
        print(f"\n📦 Creating backup at {self.backup_dir.name}")
        try:
            # Ensure we can create the backup directory
            self.backup_dir.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy everything except existing backups and .git
            ignore_patterns = shutil.ignore_patterns('backup_*', '.git', '__pycache__', '*.pyc')
            
            # For WSL paths, we need to ensure proper copying
            shutil.copytree(
                str(self.base_path), 
                str(self.backup_dir),
                ignore=ignore_patterns
            )
            
            print("✅ Backup created successfully")
            return True
        except Exception as e:
            print(f"❌ Error creating backup: {e}")
            self.errors.append(f"Backup creation failed: {e}")
            return False
    
    def copy_js_files(self):
        """Copy JavaScript files from course_template"""
        print("\n📂 Copying JavaScript files from course_template...")
        
        js_source = self.course_template_path / 'js'
        js_dest = self.base_path / 'js'
        
        # Check if source exists
        if not js_source.exists():
            print(f"  ⚠️ Source JS directory not found: {js_source}")
            print(f"  📍 Looking for course_template at: {self.course_template_path}")
            self.errors.append(f"JS source directory not found: {js_source}")
            return
        
        # Create js directory if it doesn't exist
        try:
            js_dest.mkdir(parents=True, exist_ok=True)
            print(f"  📁 Created/verified JS directory: {js_dest.name}")
        except Exception as e:
            print(f"  ❌ Error creating JS directory: {e}")
            self.errors.append(f"Could not create JS directory: {e}")
            return
        
        # Files to copy
        js_files = ['clipboard.js', 'course-enhancements.js']
        
        for file_name in js_files:
            source_file = js_source / file_name
            dest_file = js_dest / file_name
            
            try:
                if source_file.exists():
                    # Read and write to handle WSL paths better
                    with open(str(source_file), 'r', encoding='utf-8') as src:
                        content = src.read()
                    with open(str(dest_file), 'w', encoding='utf-8') as dst:
                        dst.write(content)
                    print(f"  ✅ Copied {file_name}")
                else:
                    print(f"  ⚠️ Source file not found: {file_name}")
                    self.errors.append(f"JS file not found: {file_name}")
            except Exception as e:
                self.errors.append(f"Error copying {file_name}: {e}")
                print(f"  ❌ Error copying {file_name}: {e}")
    
    def extract_inline_styles(self, soup):
        """Extract inline styles from HTML and return them"""
        styles = []
        
        # Find all <style> tags
        for style_tag in soup.find_all('style'):
            style_content = style_tag.string
            if style_content:
                styles.append(style_content)
            style_tag.decompose()  # Remove the style tag
        
        return '\n'.join(styles)
    
    def create_standard_nav(self):
        """Create standardized navigation HTML"""
        nav_html = '''
    <!-- Navigation -->
    <nav class="main-nav">
        <div class="nav-container">
            <a href="index.html" class="nav-logo">⚔️ WWZ: Aftermath Guide</a>
            <button id="mobile-menu-toggle" class="mobile-menu-toggle" aria-expanded="false">☰</button>
            <div class="nav-links" id="nav-links">
                <a href="index.html">Home</a>
                <a href="beginner_guide.html">Beginner Guide</a>
                <div class="dropdown">
                    <a href="classes_overview.html" class="dropdown-toggle">Classes ▼</a>
                    <div class="dropdown-content">
                        <a href="classes_overview.html">Overview</a>
                        <a href="class_medic.html">Medic</a>
                        <a href="class_fixer.html">Fixer</a>
                        <a href="class_gunslinger.html">Gunslinger</a>
                        <a href="class_exterminator.html">Exterminator</a>
                        <a href="class_slasher.html">Slasher</a>
                        <a href="class_hellraiser.html">Hellraiser</a>
                        <a href="class_dronemaster.html">Dronemaster</a>
                        <a href="class_vanguard.html">Vanguard</a>
                    </div>
                </div>
                <a href="weapons_upgrades.html">Weapons</a>
                <a href="currencies_progression.html">Progression</a>
                <a href="horde_endgame.html">Endgame</a>
                <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
            </div>
        </div>
    </nav>'''
        return nav_html
    
    def create_breadcrumb(self, current_page):
        """Create breadcrumb navigation based on current page"""
        page_name = Path(current_page).stem
        
        # Define breadcrumb paths
        breadcrumbs = {
            'index': [],
            'beginner_guide': [('Home', 'index.html')],
            'classes_overview': [('Home', 'index.html')],
            'weapons_upgrades': [('Home', 'index.html')],
            'currencies_progression': [('Home', 'index.html')],
            'horde_endgame': [('Home', 'index.html')],
            'missions_maps': [('Home', 'index.html')],
            'team_tactics': [('Home', 'index.html')],
            'troubleshooting_performance': [('Home', 'index.html')],
            'controls_xbox_pc': [('Home', 'index.html'), ('Beginner Guide', 'beginner_guide.html')],
            'printables': [('Home', 'index.html')]
        }
        
        # Class pages
        for class_name in ['medic', 'fixer', 'gunslinger', 'exterminator', 'slasher', 'hellraiser', 'dronemaster', 'vanguard']:
            breadcrumbs[f'class_{class_name}'] = [
                ('Home', 'index.html'),
                ('Classes', 'classes_overview.html')
            ]
        
        if page_name not in breadcrumbs:
            return ''
        
        crumbs = breadcrumbs[page_name]
        if not crumbs and page_name == 'index':
            return ''  # No breadcrumb for homepage
        
        html = '\n    <!-- Breadcrumb Navigation -->\n    <nav class="breadcrumb" aria-label="Breadcrumb">\n        <ul>\n'
        
        for text, href in crumbs:
            html += f'            <li><a href="{href}">{text}</a></li>\n'
        
        # Add current page
        current_title = page_name.replace('_', ' ').title()
        if page_name.startswith('class_'):
            current_title = page_name.replace('class_', '').title()
        
        html += f'            <li aria-current="page">{current_title}</li>\n'
        html += '        </ul>\n    </nav>'
        
        return html
    
    def standardize_html_file(self, file_path):
        """Standardize a single HTML file"""
        print(f"\n📄 Processing {file_path.name}...")
        
        try:
            # Read file with explicit encoding
            with open(str(file_path), 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract page-specific information
            original_title = soup.find('title')
            title_text = original_title.string if original_title else file_path.stem.replace('_', ' ').title()
            
            # Extract main content
            main_content = soup.find('body')
            if not main_content:
                print(f"  ⚠️ No body tag found in {file_path.name}")
                return
            
            # Extract and save inline styles
            inline_styles = self.extract_inline_styles(soup)
            if inline_styles:
                self.inline_styles.append(f"/* Styles from {file_path.name} */\n{inline_styles}")
            
            # Get the main content (everything except nav and scripts)
            # Remove old navigation if exists
            for nav in soup.find_all('nav'):
                nav.decompose()
            
            # Get remaining body content
            body_content = []
            for element in soup.body.children if soup.body else []:
                if element.name and element.name not in ['script', 'style']:
                    body_content.append(str(element))
            
            # Create new standardized HTML
            new_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title_text} - Comprehensive guide for World War Z: Aftermath">
    <meta name="keywords" content="World War Z, Aftermath, zombie, guide, {file_path.stem.replace('_', ', ')}">
    <meta name="author" content="WWZ Guide Team">
    <title>{title_text}</title>
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="styles/main.css">
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true,
            theme: 'default'
        }});
    </script>
</head>
<body>
    <!-- Skip to main content for accessibility -->
    <a href="#main-content" class="skip-to-main">Skip to main content</a>
    
    <!-- Progress indicator -->
    <div class="progress-indicator" role="progressbar" aria-label="Page scroll progress">
        <div class="progress-bar"></div>
    </div>
    
{self.create_standard_nav()}
    
{self.create_breadcrumb(file_path.name)}
    
    <!-- Main Content -->
    <main id="main-content">
        {''.join(body_content)}
    </main>
    
    <!-- Footer -->
    <footer class="site-footer">
        <div class="footer-content">
            <p>&copy; 2024 WWZ: Aftermath Guide. Unofficial fan resource.</p>
            <p><small>Use alongside in-game tutorials | <a href="printables.html">Print Cheatsheets</a> | Press ? for shortcuts</small></p>
        </div>
    </footer>
    
    <!-- JavaScript -->
    <script src="js/clipboard.js"></script>
    <script src="js/course-enhancements.js"></script>
</body>
</html>'''
            
            # Write the standardized file with explicit encoding
            with open(str(file_path), 'w', encoding='utf-8') as f:
                f.write(new_html)
            
            print(f"  ✅ Standardized {file_path.name}")
            self.pages_processed += 1
            
        except Exception as e:
            self.errors.append(f"Error processing {file_path.name}: {e}")
            print(f"  ❌ Error: {e}")
    
    def append_extracted_styles(self):
        """Append all extracted inline styles to main.css"""
        print("\n🎨 Consolidating inline styles to main.css...")
        
        css_file = self.base_path / 'styles' / 'main.css'
        
        # Check if CSS file exists
        if not css_file.exists():
            print(f"  ⚠️ main.css not found at {css_file}")
            # Create styles directory if needed
            css_file.parent.mkdir(parents=True, exist_ok=True)
            # Create empty CSS file
            css_file.touch()
            print(f"  📁 Created new main.css")
        
        if not self.inline_styles:
            print("  ℹ️ No inline styles to consolidate")
            # Still add the navigation styles
            self.inline_styles = []
        
        try:
            # Read existing CSS
            with open(str(css_file), 'r', encoding='utf-8', errors='ignore') as f:
                existing_css = f.read()
            
            # Append new styles
            with open(str(css_file), 'w', encoding='utf-8') as f:
                f.write(existing_css)
                
                if self.inline_styles:
                    f.write('\n\n/* ===========================\n   Extracted Inline Styles\n   =========================== */\n\n')
                    f.write('\n'.join(self.inline_styles))
                
                # Add dropdown styles for navigation
                f.write('''

/* ===========================
   Dropdown Navigation Styles
   =========================== */

.main-nav {
    background-color: var(--secondary-color, #fff);
    border-bottom: 1px solid var(--border-color, #e5e5e5);
    padding: 1rem;
    position: sticky;
    top: 0;
    z-index: 100;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-logo {
    font-size: 1.25rem;
    font-weight: bold;
    text-decoration: none;
    color: var(--primary-color, #3b82f6);
}

.nav-links {
    display: flex;
    gap: 1.5rem;
    align-items: center;
}

.nav-links a {
    text-decoration: none;
    color: var(--text-color, #333);
    transition: color 0.2s;
}

.nav-links a:hover {
    color: var(--primary-color, #3b82f6);
}

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: var(--secondary-color, #fff);
    min-width: 160px;
    box-shadow: 0px 8px 16px rgba(0,0,0,0.2);
    border-radius: 4px;
    z-index: 1000;
    top: 100%;
    left: 0;
}

.dropdown-content a {
    color: var(--text-color, #333);
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.dropdown-content a:hover {
    background-color: var(--border-color, #f0f0f0);
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown-toggle {
    cursor: pointer;
}

/* Mobile menu toggle button */
.mobile-menu-toggle {
    display: none;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
}

/* Mobile dropdown adjustments */
@media (max-width: 767px) {
    .mobile-menu-toggle {
        display: block;
    }
    
    .nav-links {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background-color: var(--secondary-color, #fff);
        flex-direction: column;
        padding: 1rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .nav-links.active {
        display: flex;
    }
    
    .dropdown-content {
        position: static;
        display: block;
        box-shadow: none;
        margin-left: 1rem;
    }
}

/* WWZ Theme Additions */
.zombie-theme {
    background: linear-gradient(135deg, #1a1a1a, #4a5d23);
    color: #f0f0f0;
    padding: 2rem;
    border-radius: 8px;
}

.site-footer {
    margin-top: 4rem;
    padding: 2rem;
    text-align: center;
    border-top: 1px solid var(--border-color, #e5e5e5);
    background: var(--secondary-color, #fff);
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
}

/* Class page enhancements */
.class-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
}

.class-meta {
    display: flex;
    gap: 2rem;
    font-size: 0.9rem;
    color: var(--text-light, #666);
}

.difficulty-rating {
    font-size: 1.2rem;
    color: #ffd700;
}

/* Skip to main content (accessibility) */
.skip-to-main {
    position: absolute;
    left: -10000px;
    top: 30px;
    z-index: 999;
    padding: 0.5rem 1rem;
    background: var(--primary-color, #3b82f6);
    color: white;
    text-decoration: none;
    border-radius: 0 5px 5px 0;
}

.skip-to-main:focus {
    left: 0;
}

/* Progress indicator */
.progress-indicator {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: var(--border-color, #e5e5e5);
    z-index: 1000;
}

.progress-bar {
    height: 100%;
    background: linear-gradient(90deg, var(--primary-color, #3b82f6), var(--primary-hover, #2563eb));
    width: 0;
    transition: width 0.3s ease;
}

/* Breadcrumb navigation */
.breadcrumb {
    padding: 1rem;
    font-size: 0.9rem;
}

.breadcrumb ul {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 0;
    flex-wrap: wrap;
}

.breadcrumb li::after {
    content: " / ";
    margin: 0 0.5rem;
    color: var(--text-light, #666);
}

.breadcrumb li:last-child::after {
    content: "";
}

.breadcrumb a {
    color: var(--primary-color, #3b82f6);
    text-decoration: none;
}

.breadcrumb [aria-current="page"] {
    color: var(--text-color, #333);
    font-weight: 500;
}
''')
            
            if self.inline_styles:
                print(f"  ✅ Added {len(self.inline_styles)} style blocks to main.css")
            else:
                print(f"  ✅ Added navigation and theme styles to main.css")
            
        except Exception as e:
            self.errors.append(f"Error updating main.css: {e}")
            print(f"  ❌ Error: {e}")
    
    def process_all_html_files(self):
        """Process all HTML files in the directory"""
        try:
            html_files = list(self.base_path.glob('*.html'))
        except Exception as e:
            print(f"❌ Error listing HTML files: {e}")
            self.errors.append(f"Could not list HTML files: {e}")
            return
        
        # Skip template files
        skip_files = ['lesson_template.html', 'index_template.html']
        html_files = [f for f in html_files if f.name not in skip_files]
        
        print(f"\n📋 Found {len(html_files)} HTML files to process")
        
        for file in html_files:
            self.standardize_html_file(file)
    
    def create_summary_report(self):
        """Create a summary report of changes made"""
        report_path = self.base_path / 'phase1_report.txt'
        
        try:
            with open(str(report_path), 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write("WORLD WAR Z SITE - PHASE 1 IMPROVEMENTS REPORT\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                
                f.write(f"✅ Pages Processed: {self.pages_processed}\n")
                f.write(f"📦 Backup Location: {self.backup_dir}\n")
                f.write(f"🎨 Inline Styles Consolidated: {len(self.inline_styles)}\n")
                f.write(f"🖥️  Platform: {'Windows/WSL' if self.is_windows else 'Unix/Linux'}\n\n")
                
                if self.errors:
                    f.write("⚠️ ERRORS ENCOUNTERED:\n")
                    for error in self.errors:
                        f.write(f"  - {error}\n")
                else:
                    f.write("✅ No errors encountered!\n")
                
                f.write("\n" + "=" * 60 + "\n")
                f.write("NEXT STEPS (Phase 2):\n")
                f.write("1. Review the updated pages in a browser\n")
                f.write("2. Test mobile responsiveness\n")
                f.write("3. Verify all navigation links work\n")
                f.write("4. Check that Mermaid diagrams render correctly\n")
                f.write("5. Test JavaScript functionality (copy buttons, theme toggle)\n")
                f.write("=" * 60 + "\n")
            
            print(f"\n📊 Report saved to {report_path.name}")
            return report_path
        except Exception as e:
            print(f"❌ Error creating report: {e}")
            return None
    
    def run_phase1(self):
        """Execute all Phase 1 improvements"""
        print("=" * 60)
        print("🚀 STARTING WORLD WAR Z SITE PHASE 1 IMPROVEMENTS")
        print("=" * 60)
        
        # Verify paths exist
        if not self.base_path.exists():
            print(f"\n❌ Error: Base path does not exist: {self.base_path}")
            return False
        
        if not self.course_template_path.exists():
            print(f"\n⚠️ Warning: Course template path not found: {self.course_template_path}")
            print("  JavaScript files will not be copied.")
            print("  Continue anyway? (y/n): ", end="")
            response = input().strip().lower()
            if response != 'y':
                print("Aborting...")
                return False
        
        # Step 1: Create backup
        if not self.create_backup():
            print("\n❌ Backup failed. Aborting to prevent data loss.")
            return False
        
        # Step 2: Copy JavaScript files
        self.copy_js_files()
        
        # Step 3: Process all HTML files
        self.process_all_html_files()
        
        # Step 4: Consolidate styles
        self.append_extracted_styles()
        
        # Step 5: Create report
        report_path = self.create_summary_report()
        
        print("\n" + "=" * 60)
        print("✅ PHASE 1 COMPLETE!")
        print(f"📋 Processed {self.pages_processed} pages")
        if self.errors:
            print(f"⚠️ {len(self.errors)} errors encountered - check report")
        print(f"📊 Full report: {report_path.name if report_path else 'Not created'}")
        print("=" * 60)
        
        return True


def main():
    """Main execution function"""
    # Get the path to the world_war_z directory
    if len(sys.argv) > 1:
        wwz_path = sys.argv[1]
    else:
        # Default WSL path for your system
        wwz_path = r"\\wsl$\Ubuntu\home\practicalace\projects\world_war_z"
        
        # Alternative WSL path format
        # wwz_path = r"\\wsl.localhost\Ubuntu\home\practicalace\projects\world_war_z"
        
        print(f"📍 Using default path: {wwz_path}")
        print("   (You can specify a different path as an argument)\n")
    
    # Check if path exists
    if not os.path.exists(wwz_path):
        print(f"❌ Error: Path not found: {wwz_path}")
        print("\nTrying alternative WSL path formats...")
        
        # Try alternative WSL path formats
        alt_paths = [
            r"\\wsl.localhost\Ubuntu\home\practicalace\projects\world_war_z",
            r"\\wsl$\Ubuntu\home\practicalace\projects\world_war_z",
            "/mnt/c/Users/practicalace/projects/world_war_z",  # If running from WSL
            "world_war_z"  # Relative path if in parent directory
        ]
        
        for alt_path in alt_paths:
            if os.path.exists(alt_path):
                print(f"✅ Found at: {alt_path}")
                wwz_path = alt_path
                break
        else:
            print("\n❌ Could not find the world_war_z directory.")
            print("\nUsage: python wwz_phase1_improvements.py [path_to_world_war_z_folder]")
            print("\nExample paths:")
            print("  Windows: C:\\Users\\YourName\\projects\\world_war_z")
            print("  WSL: \\\\wsl$\\Ubuntu\\home\\username\\projects\\world_war_z")
            print("  WSL Alt: \\\\wsl.localhost\\Ubuntu\\home\\username\\projects\\world_war_z")
            return 1
    
    # Run the improvements
    improver = WWZSiteImprover(wwz_path)
    success = improver.run_phase1()
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
