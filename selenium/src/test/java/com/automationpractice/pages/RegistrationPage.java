package com.automationpractice.pages;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

public class RegistrationPage extends BasePage {

	public RegistrationPage(WebDriver driver) {
		super(driver);
		// TODO Auto-generated constructor stub
	}

	public void setcustfname(String fname) {
		driver.findElement(By.id("customer_firstname")).sendKeys(fname);

	}

	public void setcustlname(String lname) {
		driver.findElement(By.id("customer_lastname")).sendKeys(lname);
	}

	public void setdob() {
		Select dobday = new Select(driver.findElement(By.id("days")));
		dobday.selectByIndex(12);
		Select dobmonth = new Select(driver.findElement(By.id("months")));
		dobmonth.selectByIndex(4);
		Select dobyr = new Select(driver.findElement(By.id("years")));
		dobyr.selectByIndex(10);
	}

	public void setPassword(String password) {
		driver.findElement(By.id("passwd")).sendKeys(password);

	}

	public void setAddressfname(String fname) {
		driver.findElement(By.id("firstname")).sendKeys(fname);

	}

	public void setAddresslname(String lname) {
		driver.findElement(By.id("lastname")).sendKeys(lname);

	}

	public void setAddressCompany(String company) {
		driver.findElement(By.id("company")).sendKeys(company);

	}

	public void setAddress(String address) {
		driver.findElement(By.id("address1")).sendKeys(address);

	}

	public void setCity(String city) {
		driver.findElement(By.id("city")).sendKeys(city);

	}

	public void setPostalCode(String postalcode) {
		driver.findElement(By.id("postcode")).sendKeys(postalcode);

	}

	public void selectState(String state) {
		Select states = new Select(driver.findElement(By.id("id_state")));
		states.selectByVisibleText(state);

	}

	public void selectCountry(String country) {
		Select count = new Select(driver.findElement(By.id("id_country")));
		count.selectByIndex(1);
	}

	public void setMobilePhone(String mobile) {
		driver.findElement(By.id("phone_mobile")).sendKeys(mobile);

	}

	public void clickSubmit() {
		driver.findElement(By.id("submitAccount")).click();

	}

	public void setGender() {
		WebDriverWait wait = new WebDriverWait(driver, 30);
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("id_gender1"))).click();

	}

	public List<WebElement> getErrMsg() {
		WebDriverWait wait = new WebDriverWait(driver, 30);
		List<WebElement> elem = wait.until(ExpectedConditions.presenceOfAllElementsLocatedBy(By.cssSelector("div>ol>li")));
		return elem;
	}

	public String getFnameErrorMsg() throws Exception {
		for (WebElement elem: getErrMsg()) {
			if (elem.getText().equals("firstname is required.")){
				return elem.getText();
			}
		} throw new Exception("No fname error message found");
	}
	
	public String getLnameErrorMsg() throws Exception {
		for (WebElement elem: getErrMsg()) {
			if (elem.getText().equals("lastname is required.")){
				return elem.getText();
			}
		} throw new Exception("No lname error message found");

	}
	
	public String getPasswordErrorMsg() throws Exception {
		for (WebElement elem: getErrMsg()) {
			if (elem.getText().equals("passwd is required.")){
				return elem.getText();
			}
		} throw new Exception("No passwd error message found");
		
	}
	public String getAddr1ErrorMsg() throws Exception {
		for (WebElement elem: getErrMsg()) {
			if (elem.getText().equals("address1 is required.")){
				return elem.getText();
			}
		} throw new Exception("No address error message found");
	}
	
	public String getCityErrorMsg() throws Exception {
		for (WebElement elem: getErrMsg()) {
			if (elem.getText().equals("city is required.")){
				return elem.getText();
			}
		} throw new Exception("No city error message found");
	}
	
	public String getPostCodeFormatErrorMsg() throws Exception {
		for (WebElement elem: getErrMsg()) {
			if (elem.getText().equals("The Zip/Postal code you've entered is invalid. It must follow this format: 00000")){
				return elem.getText();
			}
		} throw new Exception("No postal error message found");
		
		
	}
	
	public String getCountryStateErrorMsg() throws Exception {
		for (WebElement elem: getErrMsg()) {
			if (elem.getText().equals("This country requires you to choose a State.")){
				return elem.getText();
			}
		} throw new Exception("No country error message found");
		
		
	}
	
	public String getPhoneNumberErrorMsg() throws Exception {
		for (WebElement elem: getErrMsg()) {
			if (elem.getText().equals("You must register at least one phone number.")){
				return elem.getText();
			}
		} throw new Exception("No phone number error message found");

	}
}
