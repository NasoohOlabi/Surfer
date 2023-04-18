console.log(`curser : `);
console.log(curser);
console.log(`window.curser : `);
console.log(window.curser);
curser = curser.nextSibling;
return curser.textContent;