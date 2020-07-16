package com.automationpractice.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class HomePage extends BasePage {

	public HomePage(WebDriver driver) {
		super(driver);
		// TODO Auto-generated constructor stub
	}

	public CartDialog addItemToCart() {
		Actions action = new Actions(driver);
		WebElement element = driver.findElement(By.cssSelector("a[title='Faded Short Sleeve T-shirts']"));
		action.moveToElement(element).perform();
		driver.findElement(By.cssSelector("a[title='Add to cart']")).click();
		return new CartDialog(driver);

	}

	
	public CartPage clickCart() {
		Actions action = new Actions(driver);
		WebElement element = driver.findElement(By.cssSelector("a[title='Faded Short Sleeve T-shirts']"));
		action.moveToElement(element).perform();
		driver.findElement(By.cssSelector("a[title='Add to cart']")).click();
		WebDriverWait wait = new WebDriverWait(driver, 10);
		wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("[title='Continue shopping']")));
		wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("[title='Continue shopping']"))).click();
		driver.findElement(By.cssSelector("a[title='View my shopping cart']")).click();
		return new CartPage(driver);
	}
	
	public CartPage emptyCart() {
		driver.findElement(By.cssSelector("[title='View my shopping cart']")).click();
		return new CartPage(driver);

		
	}

}
