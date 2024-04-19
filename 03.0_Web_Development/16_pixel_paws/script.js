class Pet {
    constructor(id) {
      this.id = id;
      this.fedLevel = 100;
      this.fedElement = document.getElementById(`hunger${id}`);
      this.messageElement = document.getElementById(`message${id}`);
      this.displayElement = document.getElementById(`pet${id}`);
    }
    feed(amount) {
      this.fedLevel += amount;
      if (this.fedLevel > 100) {
        this.fedLevel = 100;
      }
    }
    decreaseFedLevel() {
      this.fedLevel -= 10;
      if (this.fedLevel < 0) {
        this.fedLevel = 0;
      }
      console.log(this.fedLevel);
    }
  }
  let pet1 = new Pet(1);
  
  function feedPet(amount) {
    pet1.feed(amount);
  }