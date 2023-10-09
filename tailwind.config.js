/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './library_col/**/*.{html,js}', 
    './static/**/*.{html,js}', './templates/**/*.{html,js}', 
    './main/**/*.{html,js}',
    './node_modules/flowbite/**/*.{html,js}',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

