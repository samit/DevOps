package com.automationpractice.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class LoginPage extends BasePage {

	public LoginPage(WebDriver driver) {
		super(driver);
	}
	
	public UserHomePage Login(String email, String password) {
		driver.findElement(By.id("email")).sendKeys(email);
		driver.findElement(By.id("passwd")).sendKeys(password);
		driver.findElement(By.id("SubmitLogin")).click();
		return new UserHomePage(driver);
		
	}
	
	public String getLoginErrMsg(By locater, String text) {
		WebDriverWait wait  = new WebDriverWait(driver, 10);
		wait.until(ExpectedConditions.textToBePresentInElementLocated(locater, text));
		return wait.until(ExpectedConditions.presenceOfElementLocated(locater)).getText();
	}
	
	public String getEmailErrMsg() {
		return getLoginErrMsg(By.cssSelector("div>ol>li"), "An email address required.");
	}
	
	public String getPasswordErrMsg() {
		return getLoginErrMsg(By.cssSelector("div>ol>li"), "Password is required.");
	}
	
	public String getAuthFailedErrMsg() {
		return getLoginErrMsg(By.cssSelector("div>ol>li"),"Authentication failed.");
	}

}
