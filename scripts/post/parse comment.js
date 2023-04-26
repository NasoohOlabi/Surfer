const commentText = cursor.querySelector('p').parentElement.innerText;
const userUrl = Array.from(cursor.querySelectorAll('*')).filter(x => x.getAttribute('href'))[0].href;
const userName = Array.from(cursor.querySelectorAll('*')).filter(x => x.getAttribute('href'))[0].parentElement.parentElement.parentElement.innerText;

const up_votes = cursor.__score;

function uuid() {
	var lettersDigits = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
	var result = '';
	for (var i = 0; i < 20; i++) {
		var randomIndex = Math.floor(Math.random() * lettersDigits.length);
		result += lettersDigits.charAt(randomIndex);
	}
	return result;
}


const replyElement = Array.from(cursor.querySelectorAll('*')).filter(x => x.getAttribute('slot') === 'reply')[0];
const replyClass = uuid();
replyElement.classList.add(replyClass);

const depth = cursor.__depth;

return { commentText, userName, depth, userUrl, up_votes, replyClass };

