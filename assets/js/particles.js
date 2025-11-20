// ================================================================
// 🌟 PARTICLE BACKGROUND SYSTEM
// ================================================================

class ParticleBackground {
  constructor() {
    this.canvas = null;
    this.ctx = null;
    this.particles = [];
    this.animationId = null;
    this.resizeTimeout = null;
    
    // 設定
    this.config = {
      particleCount: 80, // パーティクルの数
      minSize: 2,        // 最小サイズ
      maxSize: 6,        // 最大サイズ
      minSpeed: 0.1,     // 最小速度
      maxSpeed: 0.3,     // 最大速度
      color: {
        r: 139,          // RGB - 紫色
        g: 92,
        b: 246,
        alpha: 0.3       // 透明度
      }
    };
  }

  // 初期化
  init() {
    // 動きを減らす設定の確認
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      return; // アニメーション無効化
    }

    this.createCanvas();
    this.createParticles();
    this.setupEventListeners();
    this.animate();
  }

  // キャンバス作成
  createCanvas() {
    // コンテナを作成
    const container = document.createElement('div');
    container.className = 'particles-container';
    container.setAttribute('aria-hidden', 'true'); // アクセシビリティ

    // キャンバスを作成
    this.canvas = document.createElement('canvas');
    this.canvas.className = 'particles-canvas';
    this.ctx = this.canvas.getContext('2d');

    // サイズ設定
    this.resizeCanvas();

    container.appendChild(this.canvas);
    document.body.insertBefore(container, document.body.firstChild);
  }

  // キャンバスのサイズ調整
  resizeCanvas() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }

  // パーティクルを作成
  createParticles() {
    this.particles = [];
    const count = this.config.particleCount;

    for (let i = 0; i < count; i++) {
      this.particles.push({
        x: Math.random() * this.canvas.width,
        y: Math.random() * this.canvas.height,
        size: Math.random() * (this.config.maxSize - this.config.minSize) + this.config.minSize,
        speedX: (Math.random() - 0.5) * (this.config.maxSpeed - this.config.minSpeed) + this.config.minSpeed,
        speedY: (Math.random() - 0.5) * (this.config.maxSpeed - this.config.minSpeed) + this.config.minSpeed,
        opacity: Math.random() * 0.5 + 0.3 // 0.3〜0.8の範囲
      });
    }
  }

  // イベントリスナー設定
  setupEventListeners() {
    // ウィンドウリサイズ
    window.addEventListener('resize', () => {
      clearTimeout(this.resizeTimeout);
      this.resizeTimeout = setTimeout(() => {
        this.resizeCanvas();
        this.createParticles();
      }, 250);
    });

    // ページの可視性変更
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        this.stopAnimation();
      } else {
        this.animate();
      }
    });
  }

  // パーティクルを描画
  drawParticle(particle) {
    this.ctx.beginPath();
    this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
    this.ctx.fillStyle = `rgba(${this.config.color.r}, ${this.config.color.g}, ${this.config.color.b}, ${particle.opacity})`;
    this.ctx.fill();
  }

  // パーティクルを更新
  updateParticle(particle) {
    // 位置を更新
    particle.x += particle.speedX;
    particle.y += particle.speedY;

    // 画面外に出たら反対側に
    if (particle.x > this.canvas.width + particle.size) {
      particle.x = -particle.size;
    } else if (particle.x < -particle.size) {
      particle.x = this.canvas.width + particle.size;
    }

    if (particle.y > this.canvas.height + particle.size) {
      particle.y = -particle.size;
    } else if (particle.y < -particle.size) {
      particle.y = this.canvas.height + particle.size;
    }
  }

  // アニメーション
  animate() {
    // キャンバスをクリア
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // すべてのパーティクルを更新・描画
    this.particles.forEach(particle => {
      this.updateParticle(particle);
      this.drawParticle(particle);
    });

    // 次のフレームをリクエスト
    this.animationId = requestAnimationFrame(() => this.animate());
  }

  // アニメーション停止
  stopAnimation() {
    if (this.animationId) {
      cancelAnimationFrame(this.animationId);
      this.animationId = null;
    }
  }

  // クリーンアップ
  destroy() {
    this.stopAnimation();
    if (this.canvas && this.canvas.parentElement) {
      this.canvas.parentElement.remove();
    }
  }
}

// ================================================================
// 🚀 INITIALIZATION
// ================================================================

// DOMContentLoadedで初期化
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    window.particleBackground = new ParticleBackground();
    window.particleBackground.init();
  });
} else {
  window.particleBackground = new ParticleBackground();
  window.particleBackground.init();
}

// デバッグ用（開発時のみ）
if (window.location.hash === '#particles-debug') {
  console.log('🌟 Particle Background System Loaded');
  console.log('To stop: window.particleBackground.destroy()');
  console.log('To restart: window.particleBackground.init()');
}
