const CACHE_NAME = 'carsev-pwa-v1';
self.addEventListener('install', (e) => {
  self.skipWaiting();
});
self.addEventListener('activate', (e) => {
  self.clients.claim();
});
self.addEventListener('fetch', (e) => {
  // Service Worker activo
});
