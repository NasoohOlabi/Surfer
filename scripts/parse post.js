function selectPostTitle(post) {
	return Array.from(post.querySelectorAll('*')).filter(x => x.getAttribute('href') && x.querySelector('h3'))[0];
};
function parsePost(post) {
	let tmp = post.querySelector('.icon-upvote');
	while (tmp.innerText.length === 0) {
		tmp = tmp.parentElement;
	}
	const up_votes = tmp.innerText;
	/**
	 * @type {string[]} data
	 */
	const texts = Array
		.from(post.querySelectorAll('*'))
		.filter(x => x.getAttribute('href'))
		.map(x => x.innerText);
	let data = texts;
	const links = Array
		.from(post.querySelectorAll('*'))
		.filter(x => x.getAttribute('href'))
		.map(x => x.getAttribute('href'));
	const sub_reddit = data.filter(x => x.startsWith('r/'))[0];
	const user = data.filter(x => x.startsWith('u/'))[0];
	const comments = data.reverse().filter(x => x.toLowerCase().includes('comments'))[0];
	const title = selectPostTitle(post)?.innerText;
	const excerpt = Array.from(post.querySelectorAll('*')).filter(x => x.getAttribute('href') && x.querySelector('p') && !x.querySelector('h3'))[0]?.innerText;
	data = data.filter(str => str !== title && str !== excerpt && str !== sub_reddit && str !== user && str !== comments && str !== '');
	data.reverse();

	const obj = { up_votes, rest: data, sub_reddit, user, title, excerpt, comments, links: texts.map((elm, i) => { return { text: elm, link: links[i] }; }) };
	console.log(`post read😊 : `);
	console.log(obj);
	return obj
};

return parsePost(window.curser)