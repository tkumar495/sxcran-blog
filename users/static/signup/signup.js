function password_validate() {
	password1 = document.forms['signupform']['PASSWORD'].value;
	password2 = document.forms['signupform']['PASSWORD2'].value;
	if (password1 != password2)
		return false;
	else return true;
}
function roll_validate() {
	var roll = document.forms['signupform']['USERNAME'].value;
	var valid = true;
	if (roll.length != 12)
		valid = false;
	if (isNaN(roll.match(/^[0-9][0-9]/)))
		valid = false;
	if (!isNaN(roll.slice(2,5)))
		valid = false;
	if (isNaN(roll.slice(5).match(/[0-9]/)))
		valid = false;
	return valid;
}
function validate() {
	var password_valid = password_validate();
	var roll_valid = roll_validate();
	if !password_valid {
		document.getElementById('demo').innerHTML = "Passwords must be same";
		return false;
	}
	if !roll_valid {
		document.getElementById('demo').innerHTML = "Enter correct exam roll number [12 digits]";
		return false;
	}
	return true;
}
