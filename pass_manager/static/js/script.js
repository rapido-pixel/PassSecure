const symbols = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd', '1', '2', '3', '4', '!', '@', '#', '$']


const changeValue = () => {
	let countEl = document.querySelector('.range-slider')
	let currentCount = document.querySelector('#current-value')
	currentCount.innerHTML = countEl.value
	return countEl.value
}

document.querySelector('.gen-btn').addEventListener('click', () => {

	const genPass = (symbols, count) => {
		let password = ''
		for (let i=0; i < count; i++) {
			let randomSymbol = Math.floor(Math.random() * symbols.length)
			password += symbols[randomSymbol]
		}

		document.querySelector('.new-password').value = password
	}


	genPass(symbols, changeValue())
})

// document.querySelector('.copy').addEventListener('click', () => {
// 	const copyEl = document.querySelector('.password').value
// 	navigator.clipboard.writeText(copyEl)
// })


