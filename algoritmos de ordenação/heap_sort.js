const heap_sort = (data) => {
	let tamanho = data.length;
	let indice = Math.floor(tamanho / 2);
	let pai = 0;
	let filho = 0;
	let temp = 0;
	while (true) {
		if (indice > 0) {
			indice -= 1;
			temp = data[indice];
		} else {
			tamanho -= 1;
			if (tamanho == 0) {
				return;
			}
			temp = data[tamanho];
			data[tamanho] = data[0];
		}
		pai = indice;
		filho = indice * 2 + 1;
		while (filho < tamanho) {
			if (filho + 1 < tamanho && data[filho + 1] > data[filho]) {
				filho += 1;
			}
			if (data[filho] > temp) {
				data[pai] = data[filho];
				pai = filho;
				filho = pai * 2 + 1;
			} else {
				break;
			}
		}
		data[pai] = temp;
	}
};

data = [8, 5, 2, 8, 7, 7, 88, 1];
heap_sort(data);
console.log(data);
