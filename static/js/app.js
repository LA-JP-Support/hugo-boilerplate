// Global JavaScript for SmartWeb site.
// ============================================

/**
 * Lite YouTube - Click to load
 * YouTubeの動画をサムネイルとして表示し、クリック時にiframeを読み込む
 * パフォーマンス向上のため、ページ読み込み時にはYouTube JSを読み込まない
 */
(function() {
  'use strict';
  
  function initLiteYouTubeFeature() {
    document.querySelectorAll('.lite-youtube-feature:not(.lite-youtube-activated)').forEach(function(el) {
      el.addEventListener('click', function() {
        if (el.classList.contains('lite-youtube-activated')) return;
        
        var videoId = el.dataset.videoid;
        var title = el.dataset.title || 'YouTube video';
        
        // Create iframe
        var iframe = document.createElement('iframe');
        iframe.src = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1&rel=0';
        iframe.title = title;
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
        iframe.allowFullscreen = true;
        iframe.referrerPolicy = 'strict-origin-when-cross-origin';
        iframe.className = 'absolute inset-0 w-full h-full';
        iframe.style.border = '0';
        
        // Hide thumbnail and play button
        var img = el.querySelector('img');
        var button = el.querySelector('button');
        var picture = el.querySelector('picture');
        if (img) img.style.display = 'none';
        if (button) button.style.display = 'none';
        if (picture) picture.style.display = 'none';
        
        // Add iframe
        el.appendChild(iframe);
        el.classList.add('lite-youtube-activated');
        el.style.cursor = 'default';
      });
    });
  }
  
  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLiteYouTubeFeature);
  } else {
    initLiteYouTubeFeature();
  }
})();

/**
 * Lite YouTube Shortcode
 * youtube.htmlショートコード用のlite-youtube初期化
 */
(function() {
  'use strict';
  
  function initLiteYouTube() {
    document.querySelectorAll('.lite-youtube:not(.lite-youtube-activated)').forEach(function(el) {
      el.addEventListener('click', function() {
        if (el.classList.contains('lite-youtube-activated')) return;
        
        var videoId = el.dataset.videoid;
        var title = el.dataset.title || 'YouTube video';
        
        var iframe = document.createElement('iframe');
        iframe.src = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1&rel=0';
        iframe.title = title;
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
        iframe.allowFullscreen = true;
        iframe.referrerPolicy = 'strict-origin-when-cross-origin';
        
        el.appendChild(iframe);
        el.classList.add('lite-youtube-activated');
      });
    });
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLiteYouTube);
  } else {
    initLiteYouTube();
  }
})();
