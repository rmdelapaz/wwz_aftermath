# World War Z Site - Phase 1 Improvements Script

## 🚀 Quick Start

This Python script automates Phase 1 improvements for the World War Z: Aftermath guide website.

## 📋 What It Does

### Phase 1 Tasks (Automated):
1. ✅ **Creates a backup** of your entire site before making changes
2. ✅ **Copies JavaScript files** from course_template (clipboard.js, course-enhancements.js)
3. ✅ **Standardizes HTML structure** across all pages:
   - Adds proper meta tags for SEO
   - Implements consistent navigation
   - Adds breadcrumb navigation
   - Includes accessibility features
   - Adds footer to all pages
4. ✅ **Removes inline styles** and consolidates them into main.css
5. ✅ **Generates a report** of all changes made

## 🛠️ Installation

### Prerequisites:
- Python 3.7 or higher
- pip (Python package manager)

### Setup:
```bash
# Install required packages
pip install -r requirements.txt
```

## 📦 Usage

### Option 1: Run with default path
```bash
python wwz_phase1_improvements.py
```

### Option 2: Specify custom path
```bash
python wwz_phase1_improvements.py /path/to/your/world_war_z/folder
```

### Windows Example:
```bash
python wwz_phase1_improvements.py "C:\Users\YourName\projects\world_war_z"
```

### WSL/Linux Example:
```bash
python wwz_phase1_improvements.py /home/practicalace/projects/world_war_z
```

## 📁 What Gets Changed

### Before:
```
world_war_z/
├── *.html files (inconsistent structure)
├── styles/main.css
└── (no js folder)
```

### After:
```
world_war_z/
├── *.html files (standardized)
├── styles/main.css (with consolidated styles)
├── js/
│   ├── clipboard.js
│   └── course-enhancements.js
├── backup_[timestamp]/ (full backup)
└── phase1_report.txt (summary of changes)
```

## 🎯 Features Added to Each Page

### Navigation:
- Consistent top navigation bar
- Mobile-responsive hamburger menu
- Dropdown menu for classes
- Theme toggle button (light/dark mode)

### Accessibility:
- Skip to main content link
- Proper ARIA labels
- Breadcrumb navigation
- Focus indicators

### Interactive:
- Progress indicator bar
- Copy code buttons
- Smooth scrolling
- Keyboard shortcuts (press ? for help)

### SEO:
- Meta descriptions
- Keywords
- Proper title structure
- Semantic HTML

## ⚠️ Important Notes

1. **Always created a backup** - The script automatically backs up your site before making changes
2. **Review changes** - After running, review your site in a browser
3. **Test functionality** - Check that all JavaScript features work
4. **Verify links** - Ensure all navigation links are correct

## 🔍 What's in the Report

After running, check `phase1_report.txt` for:
- Number of pages processed
- Backup location
- Number of styles consolidated
- Any errors encountered
- Next steps for Phase 2

## 🐛 Troubleshooting

### "Module not found" error:
```bash
pip install beautifulsoup4 lxml
```

### "Permission denied" error:
- Run as administrator (Windows)
- Use sudo (Linux/Mac): `sudo python wwz_phase1_improvements.py`

### "Path not found" error:
- Check the path to your world_war_z folder
- Use absolute path instead of relative

### JavaScript files not copied:
- Ensure course_template folder exists in parent directory
- Check that JS files exist in course_template/js/

## 📈 Next Steps (Phase 2)

After Phase 1 is complete:

1. **Test the site** thoroughly in multiple browsers
2. **Verify mobile responsiveness** on actual devices
3. **Check all Mermaid diagrams** render correctly
4. **Test interactive features**:
   - Theme toggle
   - Mobile menu
   - Copy buttons
   - Search (once implemented)

## 🤝 Manual Adjustments Needed

After running the script, you may want to:

1. **Update page titles** if they need refinement
2. **Adjust meta descriptions** for better SEO
3. **Add page-specific content** to the main sections
4. **Upload images** to the images/ folder
5. **Create a favicon.ico** if not present

## 📊 Success Indicators

You'll know Phase 1 was successful when:
- ✅ All pages have consistent navigation
- ✅ Mobile menu works on small screens
- ✅ No inline styles remain in HTML files
- ✅ Copy buttons appear on code blocks
- ✅ Theme toggle switches between light/dark
- ✅ Breadcrumbs show correct page hierarchy

## 💡 Tips

1. **Run on a test copy first** if you're concerned about changes
2. **Keep the backup** until you're satisfied with results
3. **Commit to git** before and after running for version control
4. **Test one page thoroughly** before checking all pages

## 🚨 Recovery

If something goes wrong:
1. Your original site is backed up in `backup_[timestamp]/`
2. Simply copy files back from backup to restore
3. Check `phase1_report.txt` for error details

---

## Example Output

```
============================================================
🚀 STARTING WORLD WAR Z SITE PHASE 1 IMPROVEMENTS
============================================================
📦 Creating backup at backup_20241209_143022
✅ Backup created successfully

📂 Copying JavaScript files from course_template...
  ✅ Copied clipboard.js
  ✅ Copied course-enhancements.js

📋 Found 24 HTML files to process

📄 Processing index.html...
  ✅ Standardized index.html

[... more files ...]

🎨 Consolidating inline styles to main.css...
  ✅ Added 15 style blocks to main.css

============================================================
✅ PHASE 1 COMPLETE!
📋 Processed 24 pages
📊 Full report: phase1_report.txt
============================================================
```

## 📝 License

This script is provided as-is for the improvement of the World War Z guide site.

---

**Ready to upgrade your WWZ guide? Run the script and transform your site in minutes!** 🎮
