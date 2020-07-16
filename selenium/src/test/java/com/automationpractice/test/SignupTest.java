package com.automationpractice.test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import com.automationpractice.pages.HomePage;
import com.automationpractice.pages.RegistrationPage;
import com.automationpractice.pages.SignUpPage;

public class SignupTest extends BaseTestSuite {

	@Test
	void signUpEmailExistErrTest() {
		HomePage homePage = new HomePage(driver);
		SignUpPage signup = homePage.clickSignupPage();
		String email = "san6@gmail.com";
		signup.createAccount(email);
		Assertions.assertEquals(
				"An account using this email address has already been registered. Please enter a valid password or request a new one.",
				signup.getErrMsg());

	}

	@Test
	void SignUpMandatoryFieldErrTest() throws Exception {
		HomePage homePage = new HomePage(driver);
		SignUpPage signup = homePage.clickSignupPage();
		String email = "iamsdahal@sdahal.com";
		RegistrationPage register = signup.createAccount(email);
		register.setGender();
		register.clickSubmit();
		Assertions.assertEquals("firstname is required.", register.getFnameErrorMsg());
		Assertions.assertEquals("lastname is required.", register.getLnameErrorMsg());
		Assertions.assertEquals("passwd is required.", register.getPasswordErrorMsg());
		Assertions.assertEquals("city is required.", register.getCityErrorMsg());
		Assertions.assertEquals("address1 is required.", register.getAddr1ErrorMsg());
		Assertions.assertEquals("This country requires you to choose a State.", register.getCountryStateErrorMsg());
		Assertions.assertEquals("The Zip/Postal code you've entered is invalid. It must follow this format: 00000", register.getPostCodeFormatErrorMsg());
		Assertions.assertEquals("You must register at least one phone number.", register.getPhoneNumberErrorMsg());

	}

	/*@Test
	void SignUpUniqEmailTest() {
		HomePage homePage = new HomePage(driver);
		SignUpPage signup = homePage.clickSignupPage();
		String email = "samit@gmail.com";
		RegistrationPage register = signup.createAccount(email);
		String fname = "samit";
		String lname = "Dahal";
		String company = "myCompany";
		String address = "124 sunny road usa";
		register.setGender();
		register.setcustfname(fname);
		register.setcustlname(lname);
		register.setPassword("myPasssword");
		register.setdob();
		register.setAddressfname(fname);
		register.setAddresslname(lname);
		register.setAddressCompany(company);
		register.setAddress(address);
		register.selectCountry("United States");
		register.setCity("abc");
		register.selectState("Alaska");
		register.setPostalCode("12300");
		register.setMobilePhone("1234567890");
		register.clickSubmit();

	} */

}
