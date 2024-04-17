/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          100: '#1A53FD',
          200: '#1262B1',
        },
        neutral: '#C6E3FF',
        secondary: {
          100: '#FD901A',
          200: '#B16512',
        },
      },
    },
  },
  plugins: [],
};
