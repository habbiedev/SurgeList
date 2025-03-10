const url = $request.url;
const isHTML = $response.headers?.['Content-Type']?.includes('text/html');

if (isHTML) {
    let body = $response.body
        .replace(/<body\s[^>]*?data-href[^>]*?>/gi, '<body>')
        .replace(/<div[^>]*id="betting[^>]*>([\s\S]*?)<\/div>/gi, '')
        .replace(/<div class="\w*?yabo\w*?"[^>]*>([\s\S]*?)<\/div>/gi, '');

    const adFilters = `
        <style>
            /* 基础选择器过滤 */
            [class*="yabo"],
            [href*="bet"]:not([href^="/"]),
            [class*="regional"],
            [class*="world"],
            [class*="accumulator"],
            [class*="bg-sidebar"],
            [data-link-tracking-page="Widget"],
            [class*="widget"],
            [rel="nofollow"],
            [class^="column-"]:not([class*="col-box"]) {
                display: none !important;
                visibility: hidden !important;
            }

            /* 顶部广告容器处理 */
            .logoCon > :not(:first-child) {
                display: none !important;
            }

            /* 背景样式修复 */
            body {
                background-color: #0e1219 !important;
                position: static !important;
                overflow: visible !important;
            }
        </style>
    `;

    body = body.replace('</head>', `${adFilters}</head>`);
    $done({ body });
} else {
    $done({});
}
