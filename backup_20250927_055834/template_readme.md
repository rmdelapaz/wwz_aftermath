# Course Template Documentation

## 🎓 Quick Start Guide

This template provides a complete framework for creating professional, accessible, and interactive online courses. It includes responsive design, accessibility features, progress tracking, and many other enhancements out of the box.

## 📁 Directory Structure

```
course_template/
├── index.html              # Main course homepage
├── lesson_template.html    # Template for individual lessons
├── course-config.json      # Course configuration and metadata
├── favicon.ico            # Course favicon (replace with your own)
├── styles/
│   └── main.css           # Consolidated CSS (mobile-first, responsive)
├── js/
│   ├── clipboard.js       # Copy code functionality
│   └── course-enhancements.js  # Interactive features
├── images/                # Store course images here
└── assets/               # Additional assets (PDFs, downloads, etc.)
```

## 🚀 Getting Started

### Step 1: Configure Your Course

1. Open `course-config.json`
2. Update all placeholder values marked with `[brackets]`
3. Customize colors, fonts, and features to match your brand
4. Define your course structure (modules and lessons)

### Step 2: Customize the Homepage

1. Open `index.html`
2. Replace all `[bracketed placeholders]` with your content
3. Update the course title, description, and objectives
4. Modify the module structure to match your course
5. Add or remove sections as needed

### Step 3: Create Your Lessons

1. Copy `lesson_template.html` for each lesson
2. Rename to match your naming convention (e.g., `lesson_01.html`)
3. Update content, code examples, and exercises
4. Link lessons correctly in navigation

### Step 4: Add Your Content

1. Place images in the `images/` directory
2. Add downloadable resources to `assets/`
3. Update the favicon.ico with your course logo
4. Write your lesson content using the provided structure

## 🎨 Customization

### CSS Variables

The template uses CSS variables for easy theming. Key variables in `main.css`:

```css
:root {
    --primary-color: rgb(59, 130, 246);
    --primary-hover: rgb(37, 99, 235);
    --secondary-color: rgb(248, 250, 252);
    --text-color: rgb(51, 65, 85);
    --border-color: rgb(226, 232, 240);
    /* ... and more */
}
```

### Dark Mode

Dark mode is automatically supported. The theme toggle button allows users to switch between light and dark modes, with preferences saved locally.

### Mobile Responsiveness

The template is mobile-first and fully responsive. Key breakpoints:
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## 💡 Features

### Built-in Features

- ✅ **Responsive Design**: Works on all devices
- ✅ **Accessibility**: WCAG 2.1 AA compliant
- ✅ **Progress Tracking**: Automatic lesson progress saving
- ✅ **Code Highlighting**: Syntax highlighting ready
- ✅ **Copy Code Buttons**: One-click code copying
- ✅ **Search Functionality**: Client-side content search
- ✅ **Keyboard Shortcuts**: Navigation shortcuts (press ? to see them)
- ✅ **Print Friendly**: Optimized print styles
- ✅ **Theme Toggle**: Light/dark mode support
- ✅ **Smooth Scrolling**: Enhanced navigation experience
- ✅ **Interactive Quizzes**: Built-in quiz functionality
- ✅ **Breadcrumb Navigation**: Clear location indication
- ✅ **Mobile Menu**: Hamburger menu for mobile devices
- ✅ **SEO Ready**: Meta tags and structured data support

### Interactive Elements

#### Code Blocks
```html
<pre><code class="language-python">
# Your code here
print("Hello, World!")
</code></pre>
```

#### Exercise Cards
```html
<div class="exercise-card">
    <h3>Exercise Title</h3>
    <p>Exercise instructions...</p>
</div>
```

#### Quiz Questions
```html
<div class="quiz-container">
    <div class="quiz-question">
        <p>Your question here?</p>
        <div class="quiz-options">
            <button class="quiz-option" data-correct="true">Correct answer</button>
            <button class="quiz-option" data-correct="false">Wrong answer</button>
        </div>
    </div>
</div>
```

#### Info Cards
```html
<div class="card">
    <h3>Card Title</h3>
    <p>Card content...</p>
</div>
```

## 🔧 JavaScript Features

### Progress Tracking
- Automatically saves user progress
- Tracks visited lessons
- Saves scroll position
- Shows completion percentage

### Search Functionality
- Real-time content search
- Highlights matching text
- Navigates to results

### Keyboard Shortcuts
- `/` - Focus search
- `←` / `→` - Previous/Next lesson
- `H` - Go home
- `ESC` - Close search/modals
- `?` - Show shortcuts help

## 📝 Content Guidelines

### Lesson Structure

Each lesson should include:

1. **Learning Objectives**: Clear, measurable goals
2. **Introduction**: Context and importance
3. **Core Content**: Main teaching material
4. **Examples**: Practical demonstrations
5. **Exercises**: Hands-on practice
6. **Summary**: Key takeaways
7. **Resources**: Additional learning materials

### Writing Tips

- Use clear, concise language
- Break content into digestible sections
- Include plenty of examples
- Provide exercises with solutions
- Add visual aids where helpful
- Use consistent formatting

## 🚢 Deployment

### Static Hosting

This template creates static HTML files that can be hosted anywhere:

- **GitHub Pages**: Free hosting for GitHub repositories
- **Netlify**: Easy deployment with drag-and-drop
- **Vercel**: Fast global CDN
- **AWS S3**: Scalable static hosting
- **Any web server**: Apache, Nginx, etc.

### Deployment Steps

1. Complete all content creation
2. Test locally in a web browser
3. Verify all links work correctly
4. Check responsive design on multiple devices
5. Deploy to your chosen hosting service

## 🛠️ Troubleshooting

### Common Issues

**Issue**: JavaScript features not working
- **Solution**: Ensure JS files are properly linked and no console errors

**Issue**: Styles not applying
- **Solution**: Check that `main.css` is linked correctly

**Issue**: Images not showing
- **Solution**: Verify image paths are correct (relative to HTML file)

**Issue**: Mobile menu not working
- **Solution**: Ensure mobile-menu-toggle ID matches in HTML and JS

## 📚 Advanced Customization

### Adding New Features

1. **New JS functionality**: Add to `course-enhancements.js`
2. **Custom styles**: Add to end of `main.css` or create `custom.css`
3. **New components**: Create reusable HTML snippets
4. **Third-party libraries**: Add via CDN or local files

### Integration Options

- **Analytics**: Add Google Analytics or similar
- **Comments**: Integrate Disqus or similar
- **Video**: Embed YouTube/Vimeo players
- **Forms**: Add contact or feedback forms
- **Social Sharing**: Add social media buttons

## 🤝 Support

### Getting Help

1. Check this documentation first
2. Review the example files
3. Search for similar course implementations
4. Ask in web development forums

### Contributing

If you improve this template:
1. Document your changes
2. Test thoroughly
3. Share with the community

## 📄 License

This template is provided as-is for educational purposes. Feel free to modify and use for your own courses.

## ✨ Tips for Success

1. **Plan your content structure** before starting
2. **Keep lessons focused** on single topics
3. **Test on multiple devices** before deployment
4. **Get feedback** from early users
5. **Iterate and improve** based on usage data
6. **Keep accessibility in mind** for all users
7. **Maintain consistency** across all lessons
8. **Update regularly** with new content

---

## 🎉 Ready to Create Your Course!

You now have everything you need to create a professional online course. Remember:

- Start with the configuration
- Build your content incrementally
- Test frequently
- Deploy when ready

Good luck with your course! 🚀

**Improved Prompt**

You will create a series of HTML tutorial/lecture files. After producing each file, pause and ask whether to continue. Write as an amazing Instructor teaching new learners, with a friendly, accessible tone.

**Requirements**:

* The files must be **mobile-friendly**.
* Each file should link to `/favicon.png`.
* Filenames: use **underscores only** (no spaces or hyphens). Titles may include spaces.
* Do **not** number any headings.
* Include **plenty of real-world samples, analogies, and metaphors**.
* Illustrations: use **Mermaid diagrams, SVG, HTML5 canvas, and emojis** when useful.
* Every `<canvas>` element must have a **unique name/id**.
* Sample code must be:

  * Properly escaped (HTML entities where necessary).
  * Wrapped in `<pre><code>...</code></pre>`.
* Mermaid diagrams:

  * Must be properly formatted, especially when special characters are used.
* In the `<head>`, always include the following for Mermaid:

```html
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>
```
