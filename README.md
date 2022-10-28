Hi! My name is Daria, I'm Ukrainian who currently lives in Poland. This repository is my study project devoted to web-application testing. 

Practice of finding unique xPath locators:

**header_xpath**
```
//h5    
//*[text()='Scouts Panel']   
//*/div[1]/h5    
//*/div/child::div/h5 
```
**login_field_xpath**
```
//*[@id='login']  
//input[@type='text']  
//input[@name='login']
```
**password_field_xpath**
```
//*[@id='password']  
//*[@name='password']  
//*[@type='password']  
```
**remind_password_hyperlink_xpath**
```
//a  
//a[text()='Remind password']  
//div/*/a  
//a[text()='Remind password' or 'Przypomnij hasło']  
```
**language_button_xpath**
```
//*[@role='button']  
//*[text()='Polski']   
//*[contains(@aria-haspopup, 'listbox')]  
```
**sign_in_button_xpath**
```
//*/button[@type='submit']  
//*[text()='Sign in']  
//button/span[1]  
```
