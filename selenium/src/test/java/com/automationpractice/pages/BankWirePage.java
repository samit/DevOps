package com.automationpractice.pages;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class BankWirePage extends BasePage {

	public BankWirePage(WebDriver driver) {
		super(driver);
		// TODO Auto-generated constructor stub
	}
	
	public String getBankWireMsg(String bankwireMsg) throws Exception{
		List<WebElement> elements = driver.findElements(By.cssSelector("[class='box cheque-box']"));
		for(WebElement elem: elements) {
			if(elem.getText().contains(bankwireMsg)) {
				return elem.getText();
			}
		} throw new Exception("can not find the element with text = "+bankwireMsg);
	}

	public CompleteOrderPage confirmOrder() {
		driver.findElement(By.cssSelector("[class='button btn btn-default button-medium']")).click();
		return new CompleteOrderPage(driver);
		
	}

}
