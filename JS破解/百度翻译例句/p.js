let gtk = '320305.131321201';
function rl(num, rule) {
    for (let i = 0; i < rule.length - 2; i += 3) {
        let d = rule.charAt(i + 2);
        d = 'a' <= d ? d.charCodeAt(0) - 87 : Number(d);
        d = '+' === rule.charAt(i + 1) ? num >>> d : num << d;
        num = '+' === rule.charAt(i) ? num + d & 4294967295 : num ^ d;
    }
    return num;
}
function tl(query) {
    // 非 BMP 的 unicode 在 js 会以高低位保存在，导致 string.length 返回是 2，与后端不一致
    // https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt
    let noBMPChar = query.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
    if (noBMPChar === null) {
        let qLen = query.length;
        if (qLen > 30) {
            query = `${query.substr(0, 10)}${query.substr(Math.floor(qLen / 2) - 5, 10)}${query.substr(-10, 10)}`;
        }
    } else {
        let bmpPart = query.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/);
        let i = 0;
        let len = bmpPart.length;
        let qArray = [];
        for (; i < len; i++) {
            if (bmpPart[i] !== '') {
                qArray.push(...bmpPart[i].split(''));
            }
            if (i !== len - 1) {
                qArray.push(noBMPChar[i]);
            }
        }
        let qLen = qArray.length;
        // query 截取
        if (qLen > 30) {
            // query = `${query.substr(0, 10)}${query.substr(Math.floor(qLen / 2) - 5, 10)}${query.substr(-10, 10)}`;
            query = qArray.slice(0, 10).join('')
                + qArray.slice(Math.floor(qLen / 2) - 5, Math.floor(qLen / 2) + 5).join('')
                + qArray.slice(-10).join('');
        }
    }
    let tk;
    // key - gtk
    let key = `${String.fromCharCode(103)}${String.fromCharCode(116)}${String.fromCharCode(107)}`;

    if (gtk !== null) {
        tk = gtk;
    } else {
        tk = (gtk = window[key] || '') || '';
    }

    let tkArr = tk.split('.');
    let tk0 = Number(tkArr[0]) || 0;
    let tk1 = Number(tkArr[1]) || 0;

    let e = [];
    for (let f = 0, g = 0; g < query.length; g++) {
        let ucode = query.charCodeAt(g);
        // 将 unicode 对应 utf8 各字节存入 array e
        if (ucode < 128) {
            // utf 编码为变字节，参考 http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html
            // 单字节 操作
            e[f++] = ucode;
        } else {
            if (ucode < 2048) {
                // 双字节 操作
                e[f++] = ucode >> 6 | 192;
            } else {
                // charCodeAt 总是返回一个小于 65,536 的值。
                // 这是因为高位编码单元（higher code point）使用一对（低位编码（lower valued））代理伪字符（"surrogate" pseudo-characters）来表示，从而构成一个真正的字符。
                // 因此，为了查看或复制（reproduce）65536 及以上编码字符的完整字符，需要在获取 charCodeAt(i) 的值的同时获取 charCodeAt(i+1) 的值
                // 貌似是因为一个 char 两个字节（16位），支持 unicode \u0000 - \uffff
                if (55296 === (ucode & 64512)
                    && g + 1 < query.length
                    && 56320 === (query.charCodeAt(g + 1) & 64512)
                ) {
                    // 四字节 操作
                    ucode = 65536 + ((ucode & 1023) << 10) + (query.charCodeAt(++g) & 1023);
                    e[f++] = ucode >> 18 | 240;
                    e[f++] = ucode >> 12 & 63 | 128;
                } else {
                    // 三字节 操作
                    e[f++] = ucode >> 12 | 224;
                }
                e[f++] = ucode >> 6 & 63 | 128;
            }
            // 末字节
            e[f++] = ucode & 63 | 128;
        }
    }

    let rlt = tk0;
    // let rule1 = '+-a^+6';
    let rule1 = `${String.fromCharCode(43)}${String.fromCharCode(45)}${String.fromCharCode(97)}`
        + `${String.fromCharCode(94)}${String.fromCharCode(43)}${String.fromCharCode(54)}`;
    // let rule2 = '+-3^+b+-f'
    let rule2 = `${String.fromCharCode(43)}${String.fromCharCode(45)}${String.fromCharCode(51)}`
        + `${String.fromCharCode(94)}${String.fromCharCode(43)}${String.fromCharCode(98)}`
        + `${String.fromCharCode(43)}${String.fromCharCode(45)}${String.fromCharCode(102)}`;
    for (let i = 0; i < e.length; i++) {
        rlt += e[i];
        // +-a^+6
        rlt = rl(rlt, rule1);
    }
    rlt = rl(rlt, rule2);
    rlt ^= tk1;
    rlt < 0 && (rlt = (rlt & 2147483647) + 2147483648);
    rlt %= 1E6;
    return `${rlt.toString()}.${rlt ^ tk0}`;
}

console.log(tl('阳光'))