package com.automationpractice.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class BasePage {
	protected WebDriver driver;
	public BasePage(WebDriver driver) {
		this.driver = driver;	
			}
	public SignUpPage clickSignupPage() {
		driver.findElement(By.cssSelector("[title='Log in to your customer account']")).click();
		return new SignUpPage(driver);
	}
	
	public LoginPage clickSignInPage() {
		driver.findElement(By.cssSelector("[title='Log in to your customer account']")).click();
		return new LoginPage(driver);
	}
	
	public ContactPage clickContactPage() {
		driver.findElement(By.cssSelector("[title = 'Contact Us']")).click();
		return new ContactPage(driver);
	}

}
