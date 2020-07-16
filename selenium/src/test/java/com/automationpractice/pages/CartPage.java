package com.automationpractice.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class CartPage extends BasePage {

	public CartPage(WebDriver driver) {
		super(driver);
		// TODO Auto-generated constructor stub
	}

	public String getCartTableItem(String total, String trowData, String product) throws Exception {
		WebElement element = driver.findElement(By.id("cart_summary"));
		Table table = new Table(element);
		return table.getColItem("tbody tr", total, trowData, product);
	}

	public Integer removeProductQuantity() {
		driver.findElement(By.id("cart_quantity_down_1_1_0_0")).click();
		WebDriverWait wait = new WebDriverWait(driver, 10);
		wait.until(ExpectedConditions.textToBePresentInElementValue(
				driver.findElement(By.cssSelector("[class='cart_quantity_input form-control grey']")), "1"));
		return Integer.parseInt(driver.findElement(By.cssSelector("[class='cart_quantity_input form-control grey']"))
				.getAttribute("value"));
	}

	public Integer getProductQuantity() {
		return Integer.parseInt(driver.findElement(By.cssSelector("[class='cart_quantity_input form-control grey']"))
				.getAttribute("value"));
	}

	public String getTotalPrice() {
		return driver.findElement(By.id("total_price_container")).getText();
	}

	public String getProductAvailability() {
		return driver.findElement(By.cssSelector("[class='cart_avail']")).getText();
	}

	public Integer addProductQuantity() {
		driver.findElement(By.id("cart_quantity_up_1_1_0_0")).click();
		WebDriverWait wait = new WebDriverWait(driver, 10);
		wait.until(ExpectedConditions.textToBePresentInElementValue(
				driver.findElement(By.cssSelector("[class='cart_quantity_input form-control grey']")), "2"));
		return Integer.parseInt(driver.findElement(By.cssSelector("[class='cart_quantity_input form-control grey']"))
				.getAttribute("value"));

	}

	public String getTotalProduct() {
		return driver.findElement(By.id("total_product")).getText();
	}

	public String getTotalShipping() {
		return driver.findElement(By.id("total_shipping")).getText();
	}

	public String getTotalTax() {
		
		return driver.findElement(By.id("total_tax")).getText();

	}
	public String  emptyCartPage() {
		return driver.findElement(By.cssSelector("[class='alert alert-warning']")).getText();
	}
	
	public LoginPage clickCheckOut() {
		WebDriverWait wait = new WebDriverWait(driver, 10);
		wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("[class='button btn btn-default standard-checkout button-medium']")));
		driver.findElement(By.cssSelector("[class='button btn btn-default standard-checkout button-medium']")).click();
		return new LoginPage(driver);
	}

}
