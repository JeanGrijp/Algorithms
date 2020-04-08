function bubble_sort(lista) {
  let elementos = lista.length;
  let ordenados = false;
  while (!ordenados) {
    ordenados = true;
    for (let i = 0; i < elementos; i++) {
      if (lista[i] > lista[i + 1]) {
        let a = lista[i];
        let b = lista[i + 1];
        lista[i] = b;
        lista[i + 1] = a;
        ordenados = false;
      }
    }
  }
  return lista;
}

let lista = [];
for (let i = 0; i < 100; i++) {
  lista = [i, ...lista];
}
console.log(lista);
bubble_sort(lista);
console.log(lista);
