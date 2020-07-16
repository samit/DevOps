package com.automationpractice.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;


public class CartDialog extends BasePage {

	public CartDialog (WebDriver driver) {
		super(driver);
		// TODO Auto-generated constructor stub
	}
	public String checkIfItemAddedToCart() {
		WebDriverWait  wait = new WebDriverWait(driver, 10);
		wait.until(ExpectedConditions.presenceOfElementLocated(By.id("layer_cart")));
		return wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("[class='layer_cart_product col-xs-12 col-md-6']>h2"))).getText();
	}
	
	
}
