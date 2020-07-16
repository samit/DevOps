package com.automationpractice.pages;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class CompleteOrderPage extends BasePage {

	public CompleteOrderPage(WebDriver driver) {
		super(driver);
		// TODO Auto-generated constructor stub
	}
	public String completeOrderMsg(String orderMsg) throws Exception {
		List<WebElement> elements = driver.findElements(By.cssSelector("[class='box']"));
		for(WebElement elem: elements) {
			if(elem.getText().contains(orderMsg)) {
				return elem.getText();
			}
		} throw new Exception("can not find the element with name = "+orderMsg);
	}

}
