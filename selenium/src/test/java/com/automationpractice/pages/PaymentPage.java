package com.automationpractice.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class PaymentPage extends BasePage {

	public PaymentPage(WebDriver driver) {
		super(driver);
	}
	public String validateItemBeforePayment(String total, String trowData, String product) throws Exception {
		WebElement elem = driver.findElement(By.id("cart_summary"));
		Table table = new Table(elem);
		return table.getColItem("tbody tr", total, trowData, product);
		
	}

	public BankWirePage clickBankWire() {
		driver.findElement(By.cssSelector("a[class='bankwire']")).click();
		return new BankWirePage(driver);
	}
	
	public CheckPaymentPage clickPayByCheck() {
		driver.findElement(By.cssSelector("a[class='cheque']")).click();
		return new CheckPaymentPage(driver);
	}


}
