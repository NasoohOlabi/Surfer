window.curser = [].slice.call(document.querySelectorAll(`div[data-scroller-first]`));
curser = curser.filter(x => x.querySelector('i.icon-upvote'))[0] || curser[0];
let x = curser.querySelector(`#0`);
console.log(x);
return x.textContent;