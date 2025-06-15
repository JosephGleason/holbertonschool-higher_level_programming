# Task 0: Basics of HTTP/HTTPS

## Differences Between HTTP and HTTPS

HTTP is the HyperText Transfer Protocol, used to send and receive data between clients (like browsers) and servers. It does not encrypt data, meaning anyone on the network can potentially see or tamper with the information being transferred.

HTTPS (HyperText Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to protect data in transit, making it unreadable to third parties. It also authenticates the server's identity and ensures integrity.

Main differences:
- HTTP sends data in plain text; HTTPS encrypts it.
- HTTP uses port 80; HTTPS uses port 443.
- HTTPS requires an SSL certificate.
- HTTPS is used for any site that handles personal, sensitive, or financial data.

## Structure of an HTTP Request and Response

Example HTTP Request:

```http
GET /learning/ssl/why-is-http-not-secure/ HTTP/1.1
Host: www.cloudflare.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Connection: keep-alive

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Encoding: gzip
Content-Length: 15678
Cache-Control: max-age=600
```

## Exploring HTTP Methods and Status Codes

### Common HTTP Methods

- **GET** – Retrieves data from the server. Used when loading web pages or requesting information.
- **POST** – Sends new data to the server. Commonly used in form submissions or when creating new records.
- **PUT** – Updates an existing resource on the server.
- **DELETE** – Removes a resource from the server.

### Common HTTP Status Codes

- **200 OK** – The request was successful.
- **201 Created** – A new resource was successfully created (after a POST request).
- **400 Bad Request** – The server could not understand the request due to malformed syntax.
- **404 Not Found** – The requested resource does not exist.
- **500 Internal Server Error** – The server encountered an unexpected condition.

## 2. GET Request to Fetch Posts

**Command:**

```bash
curl https://jsonplaceholder.typicode.com/posts/1
