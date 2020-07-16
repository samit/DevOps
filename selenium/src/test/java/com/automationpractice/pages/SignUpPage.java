package com.automationpractice.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class SignUpPage extends BasePage {

	public SignUpPage(WebDriver driver) {
		super(driver);
	}

	public RegistrationPage createAccount(String email) {
		driver.findElement(By.id("email_create")).sendKeys(email);
		driver.findElement(By.id("SubmitCreate")).click();
		return new RegistrationPage(driver);
	}

	public String getErrMsg() {
		WebDriverWait wait = new WebDriverWait(driver, 30);
		wait.until(ExpectedConditions.textToBePresentInElementLocated(By.id("create_account_error"),
				"An account using this email address has already been registered. Please enter a valid password or request a new one."));
		return wait.until(ExpectedConditions.presenceOfElementLocated(By.id("create_account_error"))).getText();

	}

}
