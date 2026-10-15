import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    host: '0.0.0.0',
    allowedHosts: [
      'mern-frontend-tien.onrender.com',
      '.onrender.com',
      'localhost'
    ]
  },
  preview: {
    host: '0.0.0.0',
    allowedHosts: [
      'mern-frontend-tien.onrender.com',
      '.onrender.com',
      'localhost'
    ]
  }
});
