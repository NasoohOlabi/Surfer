const commentText = cursor.querySelector('p').parentElement.innerText;
console.log(`commentText : `);
console.log(commentText);
const userUrl = Array.from(cursor.querySelectorAll('*')).filter(x => x.getAttribute('href'))[0].href;
console.log(`userUrl : `);
console.log(userUrl);
const userName = Array.from(cursor.querySelectorAll('*')).filter(x => x.getAttribute('href'))[0].parentElement.parentElement.parentElement.innerText;
console.log(`userName : `);
console.log(userName);

const up_votes = cursor.__score;
console.log(`up_votes : `);
console.log(up_votes);

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

const post = { commentText, userName, depth, userUrl, up_votes, replyClass };

console.log(`post : `);
console.log(post);

return post;