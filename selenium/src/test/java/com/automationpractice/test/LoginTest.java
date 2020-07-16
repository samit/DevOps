package com.automationpractice.test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import com.automationpractice.pages.HomePage;
import com.automationpractice.pages.LoginPage;
import com.automationpractice.pages.UserHomePage;

public class LoginTest extends BaseTestSuite {

	@Test
	public void loginTest() {
		String email = "san6@gmail.com";
		String password = "myPasssword";
		HomePage homepage = new HomePage(driver);
		LoginPage login = homepage.clickSignInPage();
		UserHomePage uhomepage = login.Login(email, password);
		String expectedurl = "http://automationpractice.com/index.php?controller=my-account";
		Assertions.assertEquals(expectedurl, uhomepage.getUserPageUrl());
	}
	
	@Test
	public void authFailedTest() {
		String email = "san6@gmail.com";
		String password = "Password";
		HomePage homepage = new HomePage(driver);
		LoginPage login = homepage.clickSignInPage();
		login.Login(email, password);
		Assertions.assertEquals("Authentication failed.", login.getAuthFailedErrMsg());
	}
	
	@Test
	public void passwordReqFieldTest() {
		String email = "san6@gmail.com";
		String password = "";
		HomePage homepage = new HomePage(driver);
		LoginPage login = homepage.clickSignInPage();
		login.Login(email, password);
		Assertions.assertEquals("Password is required.", login.getPasswordErrMsg());
	}
	
	@Test
	public void emailFieldReqTest() {
		String email = "";
		String password = "";
		HomePage homepage = new HomePage(driver);
		LoginPage login = homepage.clickSignInPage();
		login.Login(email, password);
		Assertions.assertEquals("An email address required.", login.getEmailErrMsg());
		
	}
	

}