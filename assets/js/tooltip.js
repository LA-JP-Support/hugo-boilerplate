/**
 * Smart Tooltip System - JavaScript
 * hugo-boilerplate用に最適化
 * Tailwind CSSクラスベースの実装
 */

(function() {
    'use strict';
    
    const TooltipSystem = {
        settings: {
            touchDevice: false,
            initialized: false,
            mobileBreakpoint: 768,
            activeTooltip: null,
            // Tailwindのブレークポイントに合わせる
            breakpoint: window.matchMedia('(max-width: 768px)')
        },
        
        /**
         * システム初期化
         */
        init: function() {
            if (this.settings.initialized) return;
            
            // タッチデバイス検出
            this.detectTouchDevice();
            
            // DOM読み込み完了後に初期化
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', () => {
                    this.setup();
                });
            } else {
                this.setup();
            }
            
            this.settings.initialized = true;
        },
        
        /**
         * セットアップ
         */
        setup: function() {
            this.setupTooltips();
            this.bindEvents();
            
            // デバッグ用
            if (window.location.hash === '#tooltip-debug') {
                document.body.classList.add('tooltip-debug');
                this.debug();
            }
        },
        
        /**
         * タッチデバイス検出
         */
        detectTouchDevice: function() {
            this.settings.touchDevice = (
                'ontouchstart' in window ||
                navigator.maxTouchPoints > 0 ||
                navigator.msMaxTouchPoints > 0
            );
        },
        
        /**
         * ツールチップセットアップ
         */
        setupTooltips: function() {
            const wrappers = document.querySelectorAll('.tooltip-wrapper');
            
            wrappers.forEach((wrapper) => {
                if (wrapper.dataset.tooltipInitialized) return;
                wrapper.dataset.tooltipInitialized = 'true';
            });
        },
        
        /**
         * イベントバインド
         */
        bindEvents: function() {
            const self = this;
            
            if (!this.settings.touchDevice) {
                this.bindDesktopEvents();
            } else {
                this.bindMobileEvents();
            }
            
            // キーボードイベント（共通）
            this.bindKeyboardEvents();
            
            // レスポンシブ対応
            this.settings.breakpoint.addListener(() => {
                this.hideAllTooltips();
            });
            
            // 画面回転対応
            window.addEventListener('orientationchange', () => {
                this.hideAllTooltips();
            });
        },
        
        /**
         * デスクトップイベント
         */
        bindDesktopEvents: function() {
            // Tailwindのgroupクラスでホバーは自動処理されるため、
            // ここではフォーカス管理とARIA属性の更新のみ
            document.addEventListener('focusin', (e) => {
                const wrapper = e.target.closest('.tooltip-wrapper');
                if (wrapper) {
                    wrapper.setAttribute('aria-expanded', 'true');
                }
            });
            
            document.addEventListener('focusout', (e) => {
                const wrapper = e.target.closest('.tooltip-wrapper');
                if (wrapper) {
                    wrapper.setAttribute('aria-expanded', 'false');
                }
            });
        },
        
        /**
         * モバイルイベント
         */
        bindMobileEvents: function() {
            const self = this;
            
            // タップイベント
            document.addEventListener('click', function(e) {
                const wrapper = e.target.closest('.tooltip-wrapper');
                const link = e.target.closest('a');
                if (wrapper && link && wrapper.contains(link)) {
                    return;
                }
                
                if (wrapper) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    if (wrapper.classList.contains('active')) {
                        self.hideTooltip(wrapper);
                    } else {
                        self.hideAllTooltips();
                        self.showTooltip(wrapper);
                    }
                } else {
                    // 外部クリックで閉じる
                    self.hideAllTooltips();
                }
            });
            
            // スワイプで閉じる
            let touchStartY = 0;
            
            document.addEventListener('touchstart', function(e) {
                touchStartY = e.touches[0].clientY;
            }, { passive: true });
            
            document.addEventListener('touchmove', function(e) {
                const touchEndY = e.touches[0].clientY;
                const diff = Math.abs(touchEndY - touchStartY);
                
                if (diff > 50) {
                    self.hideAllTooltips();
                }
            }, { passive: true });
        },
        
        /**
         * キーボードイベント
         */
        bindKeyboardEvents: function() {
            const self = this;
            
            document.addEventListener('keydown', function(e) {
                const wrapper = e.target.closest('.tooltip-wrapper');
                const link = e.target.closest('a');
                if (wrapper && link && wrapper.contains(link)) {
                    return;
                }
                
                if (!wrapper) {
                    if (e.key === 'Escape') {
                        self.hideAllTooltips();
                    }
                    return;
                }
                
                switch(e.key) {
                    case 'Enter':
                    case ' ':
                        e.preventDefault();
                        if (self.isMobile()) {
                            if (wrapper.classList.contains('active')) {
                                self.hideTooltip(wrapper);
                            } else {
                                self.showTooltip(wrapper);
                            }
                        }
                        break;
                        
                    case 'Escape':
                        e.preventDefault();
                        self.hideTooltip(wrapper);
                        break;
                        
                    case 'Tab':
                        self.hideAllTooltips();
                        break;
                }
            });
        },
        
        /**
         * ツールチップ表示
         */
        showTooltip: function(wrapper) {
            if (!wrapper || wrapper.classList.contains('active')) return;
            
            wrapper.classList.add('active');
            wrapper.setAttribute('aria-expanded', 'true');
            
            this.settings.activeTooltip = wrapper;
            
            // カスタムイベント発火
            this.triggerEvent(wrapper, 'tooltip:show');
        },
        
        /**
         * ツールチップ非表示
         */
        hideTooltip: function(wrapper) {
            if (!wrapper) return;
            
            wrapper.classList.remove('active');
            wrapper.setAttribute('aria-expanded', 'false');
            
            if (this.settings.activeTooltip === wrapper) {
                this.settings.activeTooltip = null;
            }
            
            // カスタムイベント発火
            this.triggerEvent(wrapper, 'tooltip:hide');
        },
        
        /**
         * 全てのツールチップを非表示
         */
        hideAllTooltips: function() {
            const activeWrappers = document.querySelectorAll('.tooltip-wrapper.active');
            activeWrappers.forEach((wrapper) => {
                this.hideTooltip(wrapper);
            });
        },
        
        /**
         * モバイル判定
         */
        isMobile: function() {
            return this.settings.breakpoint.matches;
        },
        
        /**
         * カスタムイベント発火
         */
        triggerEvent: function(element, eventName) {
            const event = new CustomEvent(eventName, {
                bubbles: true,
                cancelable: true,
                detail: { element: element }
            });
            element.dispatchEvent(event);
        },
        
        /**
         * デバッグ情報表示
         */
        debug: function() {
            console.group('Tooltip System Debug Info');
            console.log('Initialized:', this.settings.initialized);
            console.log('Touch Device:', this.settings.touchDevice);
            console.log('Is Mobile:', this.isMobile());
            console.log('Active Tooltip:', this.settings.activeTooltip);
            console.log('Total Tooltips:', document.querySelectorAll('.tooltip-wrapper').length);
            console.groupEnd();
        }
    };
    
    // グローバルに公開
    window.TooltipSystem = TooltipSystem;
    
    // 自動初期化
    TooltipSystem.init();
    
    // キーボードショートカット: Ctrl+Shift+T でデバッグ
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.shiftKey && e.key === 'T') {
            e.preventDefault();
            document.body.classList.toggle('tooltip-debug');
            TooltipSystem.debug();
        }
    });
    
})();
