
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';


// Vite configuration
// Sets up React support for the Vite development environment

export default defineConfig({
  plugins: [react()], // Add the React plugin for Vite
});
