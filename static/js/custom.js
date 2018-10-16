/* Custom JS */

(function() {
    var pre = document.querySelectorAll('code.sourceCode'), pl = pre.length;
    for (var i = 0; i < pl; i++) {
        pre[i].innerHTML = '<span class="line-number"></span>' + pre[i].innerHTML + '<span class="cl"></span>';
        var num = pre[i].innerHTML.split(/\n/).length;
        for (var j = 0; j < num; j++) {
            var line_num = pre[i].getElementsByTagName('span')[0];
            line_num.innerHTML += '<span>' + (j + 1) + '</span>';
        }
    }
})();

$(document.links).filter(function () {
  return this.hostname != window.location.hostname;
}).attr('target', '_blank');

