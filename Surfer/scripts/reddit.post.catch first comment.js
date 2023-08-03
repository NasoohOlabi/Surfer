/*console.log(`document.querySelector('shreddit-comment') : `);
console.log(document.querySelector('shreddit-comment'));
window.cursor = document.querySelector('shreddit-comment');*/

/* window.cursor = [].slice.call(document.querySelectorAll(`div[data-scroller-first]`));
cursor = cursor.filter(x => x.querySelector('i.icon-upvote'))[0] || cursor[0]; */

window.cursor = null;

const intervalId = setInterval(() => {
	const elements = document.querySelectorAll(`div[data-scroller-first]`);
	console.log(`elements : `);
	console.log(elements);
	window.cursor = elements[elements.length - 1];
	console.log(`window.cursor : `);
	console.log(window.cursor);
	if (cursor) {
		clearInterval(intervalId);
	}
}, 500);