/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './mainApp/static/js/**/*.js',
    './mainApp/static/css/**/*.css',
    './mainApp/templates/**/*.html'
  ],
  theme: {
    screens: {
      'sm': '576px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    extend: {},
  },
  plugins: [],
}
