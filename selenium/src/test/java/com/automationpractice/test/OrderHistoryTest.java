package com.automationpractice.test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import com.automationpractice.pages.HomePage;
import com.automationpractice.pages.LoginPage;
import com.automationpractice.pages.OrderHistoryPage;
import com.automationpractice.pages.UserHomePage;

public class OrderHistoryTest extends BaseTestSuite {
	@Test
	public void checkOrderHistroy() throws Exception {
		HomePage homePage = new HomePage(driver);
		LoginPage login = homePage.clickSignInPage();
		String email = "san6@gmail.com";
		String password = "myPasssword";
		UserHomePage uhomepage = login.Login(email, password);
		OrderHistoryPage ohisPage = uhomepage.orderPage();
		Assertions.assertEquals("RAADVJKHJ", ohisPage.getOrderHistoryItem("Total price", "$54.00", "Order reference"));

	}

}
