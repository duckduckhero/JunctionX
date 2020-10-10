**type : post** 

**호출 : /killuser** 

input 으로 입력한 username 을 가진 user 를 사망으로 처리한다. 

input 

```
{
    'username' : 'username'
}
```

output (성공시)

```
{
    'StatusCode' : '200', 
    'Message' : 'User Killing Success'
}
```

 

**type : post** 

**호출 : /login** 

input 으로 입력한 username 과 password 가 맞는지 틀린지를 판단해준다. 

input 

```
{
    'username' : 'username',
    'password' : 'password'
}
```

output (로그인 성공시)

```
{
    'StatusCode' : '200', 
    'Message' : 'LogIn Success'
}
```

 output (로그인 실패시)

```
{
    'StatusCode' : '400', 
    'Message' : 'LogIn Fail'
}
```









