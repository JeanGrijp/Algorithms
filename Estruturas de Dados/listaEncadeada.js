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

class LinkedList {
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

  remove(value) {
    if (this.first.value === null) {
      return null;
    } else {
      let aux = this.first;
      let auxBefore = aux;
      while (aux.next !== null) {
        if (aux.value === value) {
          auxBefore.next = aux.next;
        } else {
          auxBefore = aux;
          aux = aux.next;
        }
      }
    }
  }
}
