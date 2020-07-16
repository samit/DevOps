package com.automationpractice.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class OrderHistoryPage extends BasePage {

	public OrderHistoryPage(WebDriver driver) {
		super(driver);
		// TODO Auto-generated constructor stub
	}
	
	public String getOrderHistoryItem(String payment, String trowdata, String retcolItem) throws Exception {
		WebElement element = driver.findElement(By.id("order-list"));
		Table table = new Table(element);
		return table.getColItem("tbody tr", payment, trowdata, retcolItem);
	}
	

}
