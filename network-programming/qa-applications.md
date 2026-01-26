# 🧪 Practical Test Cases for API & Network Testing
| **#** | **Test Case Title** | **Scenario**  | **Expected Result (Success Criteria)** |
| :--- | :--- | :--- |:--- |
|1| **Encoding Mismatch Handling** | Send an API request containing special characters (e.g., ą, ź, ) using UTF-8 encoding, but set the header to ISO-8859-1 | The system should either correctly transcode the data or return a 400 Bad Request. No "mojibake" (corrupted text) in the database|
|2| **Network Resilience (Packet Loss)** | Use a network throttling tool (like Charles Proxy) to simulate 50% packet loss during a large data transfer| The application should handle the delay gracefully. TCP should attempt retransmission. The user should see a "Loading" state or a clear "Timeout" error, not a system crash|
|3| **Port & Protocol Security** | Attempt to access the API endpoint via an incorrect port (e.g., call Port 80 instead of Port 443 for an SSL-only server) | The server should refuse the connection or redirect to HTTPS (301 Moved Permanently). Technical server logs/details should not be exposed|
|4| **Data Integrity (Intact Data)** | Intercept an API response and manually modify a few bits of the body before it reaches the client | The client-side application (or the TCP layer) should detect that the data is no longer intact and trigger an error or request retransmission | 
