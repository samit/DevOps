package com.automationpractice.pages;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class Table {
	protected WebElement element;

	public Table(WebElement element) {
		this.element = element;
	}
	private int findColIdx(String colItem) throws Exception {
		List<WebElement> els = element.findElements(By.cssSelector("thead>tr>th"));
		for (int i = 0; i < els.size(); i++) {
			if (els.get(i).getText().equals(colItem)) {
				return i;
			}
		}
		throw new Exception("Can not find the item = " + colItem);
	}
	
	public String getColItem(String selector, String colItem, String trowData, String returnColItem) throws Exception {
		int itemCol = findColIdx(colItem);
		System.out.println(itemCol);
		int retCol = findColIdx(returnColItem);
		System.out.println(retCol);
		List<WebElement> rows = element.findElements(By.cssSelector(selector));
		for(WebElement row: rows) {
			//System.out.println(row.findElements(By.tagName("td")).get(itemCol).getText());
			if(row.findElements(By.tagName("td")).get(itemCol).getText().contains(trowData)) {
				return row.findElements(By.tagName("td")).get(retCol).getText();
			}
		}
		
		throw new Exception("No item with given column found");
	}

}
