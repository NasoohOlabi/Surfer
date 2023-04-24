/* window.curser = [].slice.call(document.querySelectorAll(`div[data-scroller-first]`));
curser = curser.filter(x => x.querySelector('i.icon-upvote'))[0] || curser[0]; */

window.curser = null;

const intervalId = setInterval(() => {
	const elements = document.querySelectorAll(`div[data-scroller-first]`);
	const filteredElements = Array.from(elements).filter(x => x.querySelector('i.icon-upvote'));
	curser = filteredElements.length > 0 ? filteredElements[0] : elements[0];
	if (curser) {
		clearInterval(intervalId);
	}
}, 500);