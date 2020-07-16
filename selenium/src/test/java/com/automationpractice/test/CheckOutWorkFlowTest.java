package com.automationpractice.test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import com.automationpractice.pages.BankWirePage;
import com.automationpractice.pages.CartPage;
import com.automationpractice.pages.CompleteOrderPage;
import com.automationpractice.pages.HomePage;
import com.automationpractice.pages.LoginPage;
import com.automationpractice.pages.PaymentPage;
import com.automationpractice.pages.ShippingPage;
import com.automationpractice.pages.UserHomePage;

public class CheckOutWorkFlowTest extends BaseTestSuite {
	@Test
	public void checkOutWOrkFlowTest() throws Exception {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		LoginPage loginPage = cartPage.clickCheckOut();
		UserHomePage userHomePage = loginPage.Login("san6@gmail.com", "myPasssword");
		Assertions.assertEquals("YOUR BILLING ADDRESS",
				userHomePage.getBillingOrDeliveryAddress("YOUR BILLING ADDRESS"));
		Assertions.assertEquals("YOUR BILLING ADDRESS",
				userHomePage.getBillingOrDeliveryAddress("YOUR BILLING ADDRESS"));
		Assertions.assertEquals("samitsamit DahalDahal",
				userHomePage.getBillingOrDeliveryAddress("samitsamit DahalDahal"), "user fname and lname");
		Assertions.assertEquals("myCompany", userHomePage.getBillingOrDeliveryAddress("myCompany"),
				"user registered company");
		Assertions.assertEquals("124 sunny road usa", userHomePage.getBillingOrDeliveryAddress("124 sunny road usa"),
				"user address 1 ");
		Assertions.assertEquals("abc, Alaska 12300", userHomePage.getBillingOrDeliveryAddress("abc, Alaska 12300"),
				"user city, state and postal code");
		Assertions.assertEquals("United States", userHomePage.getBillingOrDeliveryAddress("United States"),
				"user country");
		Assertions.assertEquals("1234567890", userHomePage.getBillingOrDeliveryAddress("1234567890"),
				"user Mobile number");
		userHomePage.addComment("This is my first comment.");
		ShippingPage shippingPage = userHomePage.proceedToCheckOut();
		Assertions.assertEquals("$2.00", shippingPage.getDeleveryPrice());
		Assertions.assertEquals("You must agree to the terms of service before continuing.",
				shippingPage.getClickAgreeErr());
		shippingPage.clickAgree();
		PaymentPage paymentPage = shippingPage.proceedToCheckout();
		String productName = paymentPage.validateItemBeforePayment("Total", "$16.51", "Description");
		Assertions.assertTrue(productName.contains("Faded Short Sleeve T-shirts"));
		BankWirePage bankWirePage = paymentPage.clickBankWire();
		String BankWireMsg = "BANK-WIRE PAYMENT.\n" + 
				"You have chosen to pay by bank wire. Here is a short summary of your order:\n" + 
				"- The total amount of your order comes to: $18.51 (tax incl.)\n" + 
				"- We allow the following currency to be sent via bank wire: Dollar\n" + 
				"- Bank wire account information will be displayed on the next page.\n" + 
				"- Please confirm your order by clicking \"I confirm my order.\".";
		Assertions.assertEquals(BankWireMsg, bankWirePage.getBankWireMsg("BANK-WIRE PAYMENT."));
		CompleteOrderPage completeOrderPage = bankWirePage.confirmOrder();
		String completeOrderMsg = "Your order on My Store is complete.\n" + 
				"Please send us a bank wire with\n" + 
				"- Amount $18.51\n" + 
				"- Name of account owner Pradeep Macharla\n" + 
				"- Include these details xyz\n" + 
				"- Bank name RTP\n";
		Assertions.assertTrue(completeOrderPage.completeOrderMsg("Your order on My Store is complete.").contains(completeOrderMsg));
	}

}
