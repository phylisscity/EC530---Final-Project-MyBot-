
/** @type {import('tailwindcss').Config} */

// TailwindCSS configuration
// Specifies where Tailwind should look for class names to generate styles

export default {
  content: [
    "./index.html",            // Watch for Tailwind classes in index.html
    "./src/**/*.{js,ts,jsx,tsx}" // Watch all JS/TS/JSX/TSX files inside src/
  ],
  theme: {
    extend: {},                 // Extend Tailwind's default theme (empty for now)
  },
  plugins: [],                  // No extra Tailwind plugins yet
};
