# Task 1: Consume Data from an API using Command Line Tools (`curl`)

---

## 1. curl --version

**Command:**
`curl --version`

**Output:**

- curl 7.81.0 (x86_64-pc-linux-gnu)
- libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 brotli/1.0.9 zstd/1.4.8
- Supports protocols: HTTP, HTTPS, FTP, LDAP, and more
- Features: IPv6, HTTP2, GSS-API, NTLM, SPNEGO, etc.

---

## 2. GET Request to Fetch a Post

**Command:**
`curl https://jsonplaceholder.typicode.com/posts/1`

**Output:**

- userId: 1  
- id: 1  
- title: *"sunt aut facere repellat provident occaecati excepturi optio reprehenderit"*  
- body:  
  > quia et suscipit  
  > suscipit recusandae consequuntur expedita et cum  
  > reprehenderit molestiae ut ut quas totam  
  > nostrum rerum est autem sunt rem eveniet architecto

---

## 3. GET Headers Only

**Command:**
`curl -I https://jsonplaceholder.typicode.com/posts`

**Output:**

- Status: HTTP/2 200 OK  
- Date: Sun, 15 Jun 2025 18:49:12 GMT  
- Content-Type: application/json; charset=utf-8  
- Cache-Control: max-age=43200  
- ETag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"  
- Server: cloudflare  
- X-Powered-By: Express  
- Rate Limits:  
  - Limit: 1000  
  - Remaining: 999  
  - Reset: 1749682047  
- Other Headers: Vary, Pragma, Age, Alt-Svc

---

## 4. Simulated POST Request

**Command:**
`curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`

**Output:**

- title: *foo*  
- body: *bar*  
- userId: 1  
- id: 101

---

## Summary

This task demonstrates how to:
- Check curl installation
- Use `GET`, `-I`, and `POST` commands with `curl`
- Understand HTTP headers and JSON responses
