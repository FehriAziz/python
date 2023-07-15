/* 
Acronyms

Create a function that, given a string, returns the string’s acronym 
(first letter of each word capitalized). 

Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

function acronymize(str) {
    var str = 'object oriented programming';
    var str2 = str.charAt(0).toUpperCase();
    console.log(str2);
}

var str = "object oriented programming";

function acronymize(str2) {
    // var str = 'object oriented programming';
    
    var myArray = str.split(" ");
    console.log(myArray)
    for (var i=0 ; i<myArray.length ; i++)
    i = str.charAt(0).toUpperCase();
    console.log(i)
    return myArray
    
}
result = acronymize(str)