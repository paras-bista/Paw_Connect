# Quick Reference - PawConnect Professional UI

## 🎨 Color Palette Quick Lookup

### Primary Colors (Use for CTAs)
```css
--color-primary: #20c997;        /* Teal - Main actions */
--color-primary-dark: #17a589;   /* Darker teal - Hover */
--color-primary-darker: #0d6d4f; /* Dark teal - Active */
```

### Secondary Colors (Use for Headers)
```css
--color-secondary: #1a374d;      /* Navy - Main text */
--color-secondary-light: #2d5a75;
```

### Status Colors
```css
--color-success: #10b981;        /* Green - Success states */
--color-danger: #ef4444;         /* Red - Errors */
--color-warning: #f59e0b;        /* Orange - Warnings */
--color-info: #3b82f6;           /* Blue - Info */
```

---

## 📦 Common Component Patterns

### Button Examples
```html
<!-- Primary Button (Most Common) -->
<button class="btn btn-primary">
  <i class="fa-solid fa-check"></i> Save
</button>

<!-- Button with Loading State -->
<button class="btn btn-primary" disabled>
  <i class="fa-solid fa-spinner fa-spin"></i> Saving...
</button>

<!-- Outline Button -->
<button class="btn btn-outline-primary">Cancel</button>

<!-- Danger Button (Destructive) -->
<button class="btn btn-danger">
  <i class="fa-solid fa-trash"></i> Delete
</button>

<!-- Large Full Width -->
<button class="btn btn-primary btn-lg btn-w-100">Submit Form</button>
```

### Card Examples
```html
<!-- Basic Card -->
<div class="card">
  <div class="card-body">
    <h5 class="card-title">
      <i class="fa-solid fa-paw"></i> Title
    </h5>
    <p class="card-text">Content here</p>
  </div>
</div>

<!-- Card with Header & Footer -->
<div class="card">
  <div class="card-header">
    <h5 class="card-title">Header</h5>
  </div>
  <div class="card-body">Content</div>
  <div class="card-footer">Footer</div>
</div>
```

### Form Examples
```html
<!-- Input Group -->
<div class="form-group">
  <label class="form-label">
    <i class="fa-solid fa-envelope"></i> Email
  </label>
  <input type="email" class="form-control" placeholder="Enter email">
</div>

<!-- Select Dropdown -->
<div class="form-group">
  <label class="form-label">
    <i class="fa-solid fa-filter"></i> Category
  </label>
  <select class="form-select">
    <option>Choose option...</option>
  </select>
</div>

<!-- Textarea -->
<div class="form-group">
  <label class="form-label">
    <i class="fa-solid fa-message"></i> Message
  </label>
  <textarea class="form-control" rows="4"></textarea>
</div>
```

### Alert Examples
```html
<!-- Success Alert -->
<div class="alert alert-success">
  <i class="fa-solid fa-check-circle"></i> Operation completed successfully!
</div>

<!-- Error Alert -->
<div class="alert alert-danger">
  <i class="fa-solid fa-exclamation-circle"></i> Something went wrong. Please try again.
</div>

<!-- Info Alert -->
<div class="alert alert-info">
  <i class="fa-solid fa-info-circle"></i> This is informational.
</div>
```

---

## 📱 Responsive Classes

```css
/* Hide on mobile, show on tablet+ */
.d-none .d-md-block

/* Full width on mobile, 50% on desktop */
<div class="col-12 col-md-6">

/* Stack on mobile, side-by-side on desktop */
<div class="row">
  <div class="col-12 col-md-6">Left</div>
  <div class="col-12 col-md-6">Right</div>
</div>
```

---

## 🎬 Animation Classes

```html
<!-- Fade In Effects -->
<div style="animation: fadeInDown 0.8s ease-out;">Fade from top</div>
<div style="animation: fadeInUp 0.8s ease-out;">Fade from bottom</div>
<div style="animation: slideInLeft 0.8s ease-out;">Slide from left</div>

<!-- Hover Animations (Built-in) -->
<button class="btn btn-primary"><!-- Auto translateY on hover --></button>
<div class="card"><!-- Auto translateY on hover --></div>
```

---

## 🔐 Security Reminders

### Never Commit These:
```python
# ❌ DON'T hardcode credentials
EMAIL_HOST_PASSWORD = 'your-password'

# ✅ DO use environment variables
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
```

### Environment Variables Setup:
```bash
# 1. Create .env file
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
SECRET_KEY=your-secret-key

# 2. Never commit .env file
# Add to .gitignore:
echo ".env" >> .gitignore

# 3. Use .env.example as template
```

---

## 📐 Spacing Utilities

```html
<!-- Margin -->
<div class="mt-4">Margin top 16px</div>
<div class="mb-8">Margin bottom 32px</div>
<div class="mx-auto">Center horizontally</div>

<!-- Padding -->
<div class="p-4">Padding 16px all sides</div>
<div class="px-8">Padding X-axis 32px</div>
<div class="py-6">Padding Y-axis 24px</div>

<!-- Gaps -->
<div class="gap-4">Gap between flex items</div>
```

---

## 🎯 Icon Quick Reference

### Common Icons (FontAwesome)
```html
<!-- Navigation -->
<i class="fa-solid fa-house"></i>        <!-- Home -->
<i class="fa-solid fa-user"></i>         <!-- Profile -->
<i class="fa-solid fa-heart"></i>        <!-- Favorite -->
<i class="fa-solid fa-paw"></i>          <!-- Paw (PawConnect) -->

<!-- Actions -->
<i class="fa-solid fa-check"></i>        <!-- Checkmark -->
<i class="fa-solid fa-trash"></i>        <!-- Delete -->
<i class="fa-solid fa-edit"></i>         <!-- Edit -->
<i class="fa-solid fa-plus"></i>         <!-- Add -->

<!-- Status -->
<i class="fa-solid fa-check-circle"></i>      <!-- Success -->
<i class="fa-solid fa-exclamation-circle"></i> <!-- Error -->
<i class="fa-solid fa-info-circle"></i>       <!-- Info -->

<!-- Animals -->
<i class="fa-solid fa-dog"></i>          <!-- Dog -->
<i class="fa-solid fa-cat"></i>          <!-- Cat -->
<i class="fa-solid fa-heart-pulse"></i>  <!-- Health -->

<!-- Business -->
<i class="fa-solid fa-hand-holding-heart"></i>    <!-- Donate -->
<i class="fa-solid fa-hand-holding-dollar"></i>   <!-- Support -->
<i class="fa-solid fa-triangle-exclamation"></i>  <!-- Alert -->
```

---

## 🔨 Common Patterns

### Centered Content
```html
<div class="text-center">
  <h2>Centered Title</h2>
  <p>Centered paragraph</p>
</div>
```

### Two-Column Layout
```html
<div class="row">
  <div class="col-lg-6">Left Column</div>
  <div class="col-lg-6">Right Column</div>
</div>
```

### Hero Section
```html
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <h1>Main Title</h1>
      <p>Subtitle</p>
      <a href="#" class="btn btn-hero">CTA Button</a>
    </div>
  </div>
</section>
```

### Statistics Section
```html
<div class="stat-card">
  <i class="fa-solid fa-icon fa-2x"></i>
  <div class="stat-number">100+</div>
  <div class="stat-label">Label</div>
</div>
```

---

## 🧪 Testing Checklist

Before deploying any page:
- [ ] Test on mobile (375px width)
- [ ] Test on tablet (768px width)
- [ ] Test on desktop (1920px width)
- [ ] Check button hover states
- [ ] Verify form validation
- [ ] Test navigation responsiveness
- [ ] Check all images load
- [ ] Verify all icons display
- [ ] Test form submission
- [ ] Check accessibility (tab key navigation)

---

## 📚 Documentation Links

- **Full Design Guide**: See `UI_DESIGN_GUIDE.md`
- **Changes Summary**: See `CLEANUP_SUMMARY.md`
- **CSS Variables**: Check `static/accounts/variables.css`
- **Components**: Check `static/accounts/components.css`
- **Main Styles**: Check `static/accounts/main.css`

---

## 💡 Pro Tips

1. **Use CSS Variables**: Reference colors via `var(--color-primary)` instead of hardcoding
2. **Follow the Grid**: Use 8px spacing units for consistency
3. **Icon Everything**: Add icons to buttons and labels for clarity
4. **Animate Subtly**: Use 250ms transitions for smooth feel
5. **Mobile First**: Design for mobile, enhance for desktop
6. **Test Early**: Check responsiveness during development
7. **Use Utilities**: Leverage Bootstrap and custom utility classes
8. **Documentation**: Update docs when adding new components

---

## 🚀 Quick Start for New Pages

1. **Copy base template structure**
2. **Import all CSS files**
3. **Use navbar pattern from base.html**
4. **Follow component patterns from this guide**
5. **Add icon to every button/label**
6. **Test responsiveness**
7. **Deploy with confidence!**

---

**Last Updated**: November 30, 2025
**Version**: 1.0 - Professional UI Release
