package com.automationpractice.test;

import java.util.concurrent.TimeUnit;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
/* Selenium Grid Import 
import java.net.URL;
import org.openqa.selenium.remote.BrowserType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver; 
*/
class BaseTestSuite {
	public static WebDriver driver;
	@BeforeAll
	static void setUpBeforeClass() throws Exception {
		/* For Selenium grid 
		DesiredCapabilities cap = new DesiredCapabilities();
		cap.setBrowserName(BrowserType.CHROME);
		driver = new RemoteWebDriver(new URL("http://localhost:4545/wd/hub"), cap);
		driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
		   */
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
	}

	@AfterAll
	static void tearDownAfterClass() throws Exception {
		driver.quit();
	}

	@BeforeEach
	void setUp() throws Exception {
		driver.manage().deleteAllCookies();
		driver.manage().window().maximize();
		driver.get("http://automationpractice.com/index.php");
	}

}
