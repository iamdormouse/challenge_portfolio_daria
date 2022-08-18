# **Task 1: Software configuration**

<details>
  <summary>### Subtask 1: Why did I choose to participate in the challenge portfolio?</summary>

First of all, I would like to thank my parents for giving me to this world :blush: 
Secondly, thanks to the targeted ads that showed me this course.
And thirdly, thanks to the Dare IT team for giving me a second chance:pray:  
10 years ago, a person close to me said: you can become a software tester. I studied theory for a few days, 
but then I gave up. What can I say? The next 10 years were not very good:unamused:...  
Why do I need this course? 
1. [ ] I want to stop depending on other people finally — to provide for myself and my son on my own:money_with_wings:
2. [x] I'm the type of person who rearranges the price tags in the store if they are not under the corresponding product:sweat_smile: I like to find errors, come up with scenarios, improve the product and HELP the people I interact with.   

So I think this role is made for me. Let's imagine that these 10 years of downtime didn't exist:grimacing:  
What do I expect from the course? That then everything will be as clear and structured as in the first task. Then my chances of success are great.  
My goal? First, win an internship, and then we'll see!:smirk:  

I mentally wish good luck to everyone.

### Daria:new_moon_with_face: 
</details>

# Task 2: Selectors

### Subtask 1 

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
