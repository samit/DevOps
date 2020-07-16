package com.automationpractice.pages;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class UserHomePage extends BasePage {

	public UserHomePage(WebDriver driver) {
		super(driver);
		// TODO Auto-generated constructor stub
	}

	public String getUserPageUrl() {
		return driver.getCurrentUrl();
	}
	
	public OrderHistoryPage orderPage() {
		driver.findElement(By.cssSelector("a[title='Orders']")).click();
		return new OrderHistoryPage(driver);
	}

	public String getBillingOrDeliveryAddress(String addressType) throws Exception {
		List<WebElement> element = driver.findElements(By.cssSelector("div>ul>li"));
		for (WebElement elem : element) {
			if (elem.getText().equals(addressType)) {
				return elem.getText();
			}
		}
		throw new Exception("can not find the element with name = " + addressType);
	}

	public void addComment(String comment) {
		driver.findElement(By.cssSelector("[name='message']")).sendKeys(comment);

	}

	public ShippingPage proceedToCheckOut() {
		driver.findElement(By.cssSelector("[name='processAddress']")).click();
		return new ShippingPage(driver);
	}

}
