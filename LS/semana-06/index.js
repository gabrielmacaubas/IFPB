// class Student {
//   constructor(name, email) {
//     this.name = name;
//     this.email = email;
//   }
// }

// const student = new Student('John Doe', 'john@email.com');

// console.log(JSON.stringify(student));

const people = [
  {name:'Alice', email:'alice@email.com'},
  {name:'Bob', email:'bob@email.com'}
];

//const peopleString = JSON.stringify(people);

// console.log(JSON.parse(peopleString));

// Alice
// Bob
// people.forEach((person) => console.log(person.name));

// people.forEach((person) => {
//   const { email } = person;

//   const [name,] = email.split('@');

//   console.log(name);
// });

people.forEach(({ email }) => {
  const [name,] = email.split('@');
  
  console.log(name);
});

for (const {email} of people) {
  const [name,] = email.split('@');

  console.log(name);
}
