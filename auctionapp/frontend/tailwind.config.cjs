/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.{vue,js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      colors:{
        'nav-blue': '#130E46'
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
