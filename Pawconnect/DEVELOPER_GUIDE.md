# PawConnect White UI - Quick Developer Guide

## 🎨 Color Variables (Use These!)

All colors are defined in `static/accounts/variables.css` and can be used as CSS variables:

```css
:root {
  --primary: #20c997;           /* Teal - Main action color */
  --secondary: #1a374d;         /* Navy - Headers and text */
  --accent: #ff7f50;            /* Orange - Secondary actions */
  --light: #f8fafc;             /* Light gray - Section backgrounds */
  --light-gray: #f1f5f9;        /* Alternate light gray */
  --white: #ffffff;             /* White - Main background */
}
```

**Usage**: `background-color: var(--primary);`

---

## 📐 Applying the White Aesthetic

### To a New Page:

1. **Background Sections:**
   ```html
   <!-- White background section -->
   <section class="section section-white">
     <div class="container">...</div>
   </section>

   <!-- Light gray background section -->
   <section class="section section-light">
     <div class="container">...</div>
   </section>
   ```

2. **Cards:**
   ```html
   <div class="card">
     <div class="card-body">
       <!-- Content -->
     </div>
   </div>
   ```

3. **Forms:**
   ```html
   <form>
     <div class="form-group">
       <label class="form-label">
         <i class="fas fa-icon"></i> Label
       </label>
       <input class="form-control" type="text">
     </div>
   </form>
   ```

4. **Buttons:**
   ```html
   <!-- Primary button -->
   <button class="btn btn-theme">Action</button>

   <!-- Hero button -->
   <a class="btn btn-hero" href="#">Hero Button</a>

   <!-- Outline button -->
   <button class="btn btn-outline-primary">Outline</button>
   ```

---

## 🎯 CSS Classes & When to Use Them

| Class | Purpose | Example |
|-------|---------|---------|
| `.section-white` | White background section | Main content areas |
| `.section-light` | Light gray background | Stats, features |
| `.card` | Professional card container | Any grouped content |
| `.btn-hero` | Large hero button | Primary CTA buttons |
| `.btn-theme` | Primary teal button | Actions |
| `.form-control` | Input styling | All form inputs |
| `.form-label` | Label styling | Form labels |

---

## 🎨 Creating New Components

### Button
```css
.custom-btn {
  background-color: var(--primary);
  color: var(--white);
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.2);
  transition: all 0.3s ease;
}

.custom-btn:hover {
  background-color: #17a589;
  box-shadow: 0 4px 16px rgba(32, 201, 151, 0.3);
  transform: translateY(-1px);
}
```

### Card
```css
.custom-card {
  background-color: var(--white);
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.custom-card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}
```

### Section
```css
.custom-section {
  padding: 50px 20px;
  background-color: var(--light);  /* or --white */
}

@media (max-width: 768px) {
  .custom-section {
    padding: 40px 15px;
  }
}

@media (max-width: 576px) {
  .custom-section {
    padding: 35px 12px;
  }
}
```

---

## 📱 Responsive Breakpoints

```css
/* Desktop: 992px+ */
@media (min-width: 992px) {
  /* Full-width layouts, 4 columns */
}

/* Tablet: 768px - 991px */
@media (max-width: 991px) {
  /* Adjusted layouts, 2 columns */
}

/* Mobile: 576px - 767px */
@media (max-width: 767px) {
  /* Single column, smaller padding */
}

/* Small Mobile: < 576px */
@media (max-width: 575px) {
  /* Minimal styling, touch-friendly */
}
```

---

## 🎯 Shadow System

```css
/* Subtle shadow - default for cards */
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);

/* Light shadow - alternative */
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);

/* Hover shadow - on interaction */
box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);

/* Heavy shadow - special emphasis */
box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
```

---

## ✏️ Typography

```css
/* Heading (Fredoka One) */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Fredoka One', cursive;
  color: var(--secondary);
  font-weight: 700;
}

/* Body (Poppins) */
body, p, span {
  font-family: 'Poppins', sans-serif;
  color: var(--secondary);
}

/* Sizes */
.h1 { font-size: clamp(2.2rem, 5vw, 3.5rem); }
.h2 { font-size: 2.2rem; }
.h3 { font-size: 1.8rem; }
.h4 { font-size: 1.4rem; }
.h5 { font-size: 1.1rem; }
.h6 { font-size: 1rem; }

/* Weights */
.fw-bold { font-weight: 700; }
.fw-semibold { font-weight: 600; }
.fw-medium { font-weight: 500; }
.fw-normal { font-weight: 400; }
```

---

## 🔄 Form Field Example

```html
<div class="form-group">
  <label class="form-label">
    <i class="fas fa-envelope"></i> Email Address
  </label>
  <input 
    class="form-control" 
    type="email" 
    placeholder="you@example.com"
    required
  >
</div>
```

---

## 🎨 Hero Section Example

```html
<section class="hero">
  <div class="hero-content">
    <h1><i class="fas fa-paw"></i> Welcome</h1>
    <p>Subheading text here</p>
    <div class="mt-4">
      <a href="#" class="btn btn-hero">Primary Action</a>
      <a href="#" class="btn btn-hero btn-outline-primary">Secondary</a>
    </div>
  </div>
</section>
```

---

## 📊 Statistics Card Example

```html
<section class="section section-light">
  <div class="container">
    <div class="row g-4">
      <div class="col-md-3">
        <div class="card">
          <div class="card-body text-center">
            <i class="fas fa-icon fa-2x text-primary mb-3"></i>
            <h4 class="fw-bold mb-1">1,200+</h4>
            <p class="text-muted mb-0">Label</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## 🚫 DO's and DON'Ts

### ✅ DO:
- Use `var(--primary)` for teal accents
- Use `var(--secondary)` for navy text
- Use `background-color: var(--white)` for main content
- Use subtle shadows (0 2px 8px)
- Use 8px border-radius for buttons
- Use 10-12px border-radius for cards
- Alternate section backgrounds (white/light)
- Use proper spacing (15-20px margins)

### ❌ DON'T:
- Don't use gradients (unless in hero)
- Don't use heavy shadows (> 0 20px 60px)
- Don't use rounded buttons (> 8px)
- Don't use large padding (> 30px normal sections)
- Don't mix multiple accent colors
- Don't forget hover states
- Don't use light-colored text on light backgrounds
- Don't ignore responsive design

---

## 🎭 Light/Dark Mode Considerations

Future implementation for dark mode:
```css
@media (prefers-color-scheme: dark) {
  :root {
    --primary: #20c997;     /* Keep same */
    --secondary: #e0e0e0;   /* Light text */
    --white: #1a1a1a;       /* Dark background */
    --light: #2a2a2a;       /* Dark gray */
  }
}
```

---

## 🔗 File Structure

```
static/accounts/
├── variables.css    (Colors, fonts, spacing tokens)
├── components.css   (Reusable components)
└── main.css        (Layout and page-specific styles)

templates/accounts/
├── base.html       (Main template - home page)
├── login.html      (Login page)
├── signup.html     (Registration page)
├── donate.html     (Donation page)
└── ...other pages
```

---

## 🐛 Common Issues & Solutions

### Issue: Button looks wrong
**Solution**: Check that you're using `.btn-hero` or `.btn-theme` classes

### Issue: Background too dark/bright
**Solution**: Use `var(--light)` for light sections, `var(--white)` for main

### Issue: Form input has wrong styling
**Solution**: Ensure `.form-control` class is applied

### Issue: Card shadow too heavy
**Solution**: Use the provided shadow classes instead of custom values

### Issue: Text hard to read
**Solution**: Check contrast - use `var(--secondary)` on white backgrounds

---

## 📚 Resources

- Font: [Poppins](https://fonts.google.com/specimen/Poppins) & [Fredoka One](https://fonts.google.com/specimen/Fredoka+One)
- Icons: [FontAwesome 6.4.0](https://fontawesome.com/)
- CSS Framework: [Bootstrap 5.3](https://getbootstrap.com/)
- Color Reference: See color palette above

---

## 💾 Testing Your Changes

1. **Local Testing**: `python manage.py runserver`
2. **Check Responsiveness**: Use DevTools (F12) and resize
3. **Verify Colors**: Use color picker to confirm hex values
4. **Test Interactivity**: Hover over buttons, click forms
5. **Cross-browser**: Test in Chrome, Firefox, Safari
6. **Mobile**: Test on actual mobile devices

---

**Version**: 1.0 - Professional White Aesthetic  
**Last Updated**: November 30, 2025  
**Maintained By**: PawConnect Development Team
