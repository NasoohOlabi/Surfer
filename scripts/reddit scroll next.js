function slowScroll(third, fifth) {
	let elementToScroll = window.curser;
	const thresholded = (x) => (x > 0) ? Math.max(x, 10) : Math.min(x, -10);
	let viewHeight = window.innerHeight;

	let boundingClientRect = elementToScroll.getBoundingClientRect();
	let targetScrollPos = boundingClientRect.top + (third * boundingClientRect.height) - (viewHeight * fifth) + window.pageYOffset;

	function scroll() {
		let currentScrollPos = window.pageYOffset;
		let distanceToScroll = thresholded((targetScrollPos - currentScrollPos) * 0.4);
		window.scrollBy(0, distanceToScroll);
		if (Math.abs(window.pageYOffset - targetScrollPos) > 20) {
			requestAnimationFrame(scroll);
		}
	}

	scroll();
}

slowScroll(+'#0', +'#1');


curser = curser.nextSibling;