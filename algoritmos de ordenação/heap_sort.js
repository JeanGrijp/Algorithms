/*
Copyright: GRIJP, Jean.
(04/2020)

*/
const heapSort = (data) => {
  const newdata = data;
  let tamanho = newdata.length;
  let indice = Math.floor(tamanho / 2);
  let pai = 0;
  let filho = 0;
  let temp = 0;
  let flag = true;
  while (flag) {
    if (indice > 0) {
      indice -= 1;
      temp = newdata[indice];
    } else {
      tamanho -= 1;
      if (tamanho === 0) {
        flag = false;
        return;
      }
      temp = data[tamanho];
      // eslint-disable-next-line prefer-destructuring
      newdata[tamanho] = newdata[0];
    }
    pai = indice;
    filho = indice * 2 + 1;
    while (filho < tamanho) {
      if (filho + 1 < tamanho && newdata[filho + 1] > newdata[filho]) {
        filho += 1;
      }
      if (newdata[filho] > temp) {
        newdata[pai] = newdata[filho];
        pai = filho;
        filho = pai * 2 + 1;
      } else {
        break;
      }
    }
    newdata[pai] = temp;
  }
};

const data = [8, 5, 2, 8, 7, 7, 88, 1];
heapSort(data);
