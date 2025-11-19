/**
 * 括弧付き説明を自動的にツールチップに変換
 * 
 * 対象形式: 用語（説明：説明文）
 * 変換後: ツールチップ付きの用語
 */

(function() {
    'use strict';
    
    function convertToTooltips() {
        // プロスエリアを対象にする
        const contentAreas = document.querySelectorAll('.prose, article, .content, main');
        
        if (contentAreas.length === 0) return;
        
        // 正規表現: 用語（説明：説明文）の形式を検出
        // キャプチャグループ: 1=用語, 2=説明文
        const regex = /([^(（\s]+)\s*[（(]説明[：:]\s*([^)）]+)[)）]/g;
        
        contentAreas.forEach(area => {
            processNode(area);
        });
    }
    
    function processNode(node) {
        // テキストノードのみ処理
        if (node.nodeType === Node.TEXT_NODE) {
            const text = node.textContent;
            const regex = /([^(（\s]+)\s*[（(]説明[：:]\s*([^)）]+)[)）]/g;
            
            if (regex.test(text)) {
                // マッチした場合、HTMLに変換
                const html = text.replace(
                    /([^(（\s]+)\s*[（(]説明[：:]\s*([^)）]+)[)）]/g,
                    function(match, term, description) {
                        const tooltipId = 'auto-tooltip-' + Math.random().toString(36).substr(2, 9);
                        return createTooltipHTML(term.trim(), description.trim(), tooltipId);
                    }
                );
                
                // 新しい要素を作成して置き換え
                const wrapper = document.createElement('span');
                wrapper.innerHTML = html;
                
                // 元のテキストノードを新しい要素で置き換え
                node.parentNode.replaceChild(wrapper, node);
            }
        } else if (node.nodeType === Node.ELEMENT_NODE) {
            // スクリプト、スタイル、既存のツールチップはスキップ
            if (node.tagName === 'SCRIPT' || 
                node.tagName === 'STYLE' || 
                node.classList.contains('tooltip-wrapper')) {
                return;
            }
            
            // 子ノードを処理
            const children = Array.from(node.childNodes);
            children.forEach(child => processNode(child));
        }
    }
    
    function createTooltipHTML(term, description, tooltipId) {
        return `<span class="tooltip-wrapper relative inline-block group" 
                      role="button" 
                      tabindex="0" 
                      aria-describedby="${tooltipId}"
                      aria-expanded="false">
  <span class="tooltip-term text-primary-600 dark:text-primary-400 underline decoration-dotted cursor-help transition-colors duration-200 hover:text-primary-700 dark:hover:text-primary-300">
    ${escapeHtml(term)}
  </span>
  <span class="tooltip hidden md:block invisible opacity-0 group-hover:visible group-hover:opacity-100 group-focus:visible group-focus:opacity-100 absolute bottom-full left-1/2 -translate-x-1/2 -translate-y-2 bg-gray-900 dark:bg-gray-800 text-white text-sm leading-relaxed px-3 py-2 rounded-lg shadow-xl whitespace-normal max-w-xs w-max z-[1000] transition-all duration-300 ease-out transform group-hover:-translate-y-3 group-focus:-translate-y-3 pointer-events-none"
        id="${tooltipId}" 
        role="tooltip">
    ${escapeHtml(description)}
    <span class="absolute top-full left-1/2 -translate-x-1/2 border-[6px] border-transparent border-t-gray-900 dark:border-t-gray-800"></span>
  </span>
  <span class="tooltip-mobile md:hidden fixed inset-x-5 top-1/2 -translate-y-1/2 bg-gray-900/95 dark:bg-gray-800/95 backdrop-blur-sm text-white text-base leading-relaxed px-4 py-3 rounded-xl shadow-2xl z-[1000] transition-all duration-300 opacity-0 invisible pointer-events-none">
    ${escapeHtml(description)}
  </span>
</span>`;
    }
    
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    // DOM読み込み完了後に実行
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', convertToTooltips);
    } else {
        convertToTooltips();
    }
})();
