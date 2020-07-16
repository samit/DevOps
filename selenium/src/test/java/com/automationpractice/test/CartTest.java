package com.automationpractice.test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import com.automationpractice.pages.CartDialog;
import com.automationpractice.pages.CartPage;
import com.automationpractice.pages.HomePage;

public class CartTest extends BaseTestSuite {

	@Test
	public void addItemToCartTest() {
		HomePage homePage = new HomePage(driver);
		CartDialog cdialog = homePage.addItemToCart();
		Assertions.assertEquals("Product successfully added to your shopping cart", cdialog.checkIfItemAddedToCart());

	}

	@Test
	public void CartTableTest() throws Exception {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		String productName = cartPage.getCartTableItem("Total", "$16.51", "Description");
		Assertions.assertTrue(productName.contains("Faded Short Sleeve T-shirts"));

	}

	@Test
	public void CartQtyTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		Assertions.assertEquals(1, cartPage.getProductQuantity());
	}

	@Test
	public void addProductQtyTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		Assertions.assertEquals(2, cartPage.addProductQuantity());
	}

	@Test
	public void removeProductQtyTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		cartPage.addProductQuantity();
		Assertions.assertEquals(1, cartPage.removeProductQuantity());
	}
	@Test
	public void getProductAvilTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage  = homePage.clickCart();
		Assertions.assertEquals("In stock", cartPage.getProductAvailability());
		
	}
	@Test 
	public void getTotalProductTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		Assertions.assertEquals("$16.51", cartPage.getTotalProduct());
		
	}
	@Test
	public void getTotalShippingTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		Assertions.assertEquals("$2.00",cartPage.getTotalShipping());
		
	}
	@Test
	public void getProductTaxTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		Assertions.assertEquals("$0.00", cartPage.getTotalTax());
		
	}
	@Test
	public void getTotalPriceTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		Assertions.assertEquals("$18.51", cartPage.getTotalPrice());
		
	}
	
	@Test
	public void emptyCartTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.emptyCart();
		Assertions.assertEquals("Your shopping cart is empty.", cartPage.emptyCartPage());
	}
	/*@Test
	public void deleteProductQtyTest() {
		HomePage homePage = new HomePage(driver);
		CartPage cartPage = homePage.clickCart();
		
		
	}*/
	
}
