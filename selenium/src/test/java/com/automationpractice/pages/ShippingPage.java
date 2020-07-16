package com.automationpractice.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class ShippingPage extends BasePage {

	public ShippingPage(WebDriver driver) {
		super(driver);
		// TODO Auto-generated constructor stub
	}

	public void clickAgree() {
		if (driver.findElement(By.cssSelector("p[class='fancybox-error']")) != null) {
			driver.findElement(By.cssSelector("[class='fancybox-item fancybox-close']")).click();
		}
		driver.findElement(By.id("uniform-cgv")).click();

	}

	public String getClickAgreeErr(){
		driver.findElement(By.cssSelector("[name='processCarrier']")).click();
		WebDriverWait wait = new WebDriverWait(driver,10);
		wait.until(ExpectedConditions.textToBePresentInElementLocated(By.cssSelector("p[class='fancybox-error']"), "You must agree to the terms of service before continuing."));
		return driver.findElement(By.cssSelector("p[class='fancybox-error']")).getText();
	}
	
	public String getDeleveryPrice() {
		return driver.findElement(By.cssSelector("[class='delivery_option_price']")).getText();
	}
	

	public PaymentPage proceedToCheckout() {
		driver.findElement(By.cssSelector("[name='processCarrier']")).click();
		return new PaymentPage(driver);

	}

}
