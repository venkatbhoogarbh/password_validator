self.addEventListener("install", e => {
  e.waitUntil(
    caches.open("password-tool").then(cache => {
      return cache.addAll([
        "./",  // Cache root
        "style.css",
        "script.js"
      ].catch(() => console.log("Some files failed to cache")))  // Graceful fallback
        .catch(() => console.log("Cache failed"))
    })
  );
});

self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request).then(response => {
      return response || fetch(e.request);
    }).catch(() => fetch(e.request))
  );
});
