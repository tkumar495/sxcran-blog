function validate() {
	password1 = document.forms['signupform']['PASSWORD'].value;
	password2 = document.forms['signupform']['PASSWORD2'].value;
	if (password1 != password2) {
		alert('Passwords should be same');
		return false;
	}
	else return true;
}