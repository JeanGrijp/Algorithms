/*
Copyright: GRIJP, Jean.
(04/2020)

*/
class No {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = new No(null);
  }

  insert(value) {
    if (this.first.value === null) {
      this.first = new No(value);
    } else {
      let aux = this.first;
      while (aux.next !== null) {
        aux = aux.next;
      }
      aux.next = new No(value);
    }
  }

  remove() {
    if (this.first.value === null) {
      return null;
    } else {
      let aux = this.first;
      if (this.first.next === null) {
        this.first = new No(null);
      } else {
        this.first = aux.next;
      }
    }
  }

  show() {
    if (this.first.value === null) {
      console.log("Fila vazia");
    } else {
      let aux = this.first;
      while (aux.next !== null) {
        console.log(aux.value);
        aux = aux.next;
      }
    }
  }
}
