var sepsisPatient;
var sepsisPatientList = [];
var temp="";
var resRate ="";
var heartRate="";
var lactic = "";
var userName = "";
var infected = "";
var Patient = "";
const prompt = require("prompt-sync")();


sepsis();
function tempature() {
  temp = prompt("What is the patients tempature? ");
  if ((temp>100.4) || (temp < 96.8)) {
    temp = "Yes";
  } else {
    temp = "No";
  }
}
// calculate how long someone has been in the hospital (MAYBE???)
// add to a list of people who may have 
// heart rate greater than 90
function Respiratory() {
  resRate = prompt("What is the patients respiratory rate? ");
  if (resRate > 20 ) {
    resRate = "Yes";
  } else {
    resRate = "No";
  }
}
function heart() {
  heartRate = prompt("What is the patients heart rate? ");
  if (heartRate > 90 ) {
    heartRate = "Yes";
  } else {
    heartRate = "No";
  }
}
function severeSepsis() {
  lactic = prompt("What is the patients lactic acidosis? ");
  if (lactic < 90 ) {
    lactic = "Yes";
  } else {
    lactic = "No";
  }
}
function sepsis() {
  userName = prompt("What is the patitent's name? Write No to stop ");
  while (userName != "No") {
    tempature();
    Respiratory();
    heart();
    severeSepsis();
    infected = prompt("Does the patient have an infection? Yes or No ");
    sepsisPatient = (userName + " meets severe sepsis criteria. Follow your guidelines for sepsis, which typically include aggressive fluid resuscitation, early, broad-spectrum antibiotics, ICU consultation, CVP evaluation, and occasionally pressors and transfusion.");
    Patient = userName + " meets severe sepsis criteria";
    if (temp=="Yes" && (heartRate == "Yes") && (resRate == "Yes") && (infected == "Yes") && (lactic == "Yes" || lactic == "No")) {
      console.log(sepsisPatient);
      sepsisPatientList.push(userName);
    } else if ((temp == "Yes") && heartRate == "Yes" && (lactic == "Yes") && infected == "No") {
      console.log(sepsisPatient);
      appendItem(sepsisPatientList, userName);
    } else if ((temp == "No" && heartRate == "Yes" && lactic == "Yes" && infected == "No")) {
      console.log(Patient);
      sepsisPatientList.push(userName);
    } else {
      console.log(userName + " does not have sepsis");
    }
    userName = prompt("What is the patitent's name? Write No to stop ");
  }

  if (sepsisPatientList.length > 0) {
    console.log("Here is a list of all the patients that have sepsis \n" + sepsisPatientList.join("\n"));
  } else {
    console.log("There are no patients with sepsis")
  }
  
}
