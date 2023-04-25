/* window.cursor = [].slice.call(document.querySelectorAll(`div[data-scroller-first]`));
cursor = cursor.filter(x => x.querySelector('i.icon-upvote'))[0] || cursor[0]; */

window.cursor = null;

const intervalId = setInterval(() => {
	const elements = document.querySelectorAll(`div[data-scroller-first]`);
	const filteredElements = Array.from(elements).filter(x => x.querySelector('i.icon-upvote'));
	cursor = filteredElements.length > 0 ? filteredElements[0] : elements[0];
	if (cursor) {
		clearInterval(intervalId);
	}
}, 500);