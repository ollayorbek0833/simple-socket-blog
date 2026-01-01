import socket
from urllib.parse import parse_qs
from get_posts import get_posts, create_post, get_post_by_id


HOST = "127.0.0.1"
PORT = 8080


def parse_post_data(request):
    body = request.split("\r\n\r\n", 1)[1]
    data = parse_qs(body)
    title = data.get("title", [""])[0]
    description = data.get("description", [""])[0]
    return title, description

def render_posts_html(posts):
    html = ""
    for idx, (title, desc, created) in enumerate(posts, start=1):
        html += f"""
        <a href="/post?id={idx}" style="text-decoration:none; color:black;">
            <div style="border:1px solid #ccc; padding:10px; margin:10px;">
                <h3>{title}</h3>
                <p>{desc[:100]}...</p>
                <small>{created}</small>
            </div>
        </a>
        """
    return html


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server running: http://{HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    request = client_socket.recv(8192).decode(errors="ignore")

    # ---- SINGLE POST PAGE ----
    if request.startswith("GET /post"):
        try:
            path = request.split(" ")[1]  # /post?id=1
            query = path.split("?", 1)[1]
            params = parse_qs(query)
            post_id = int(params.get("id", [0])[0])

            post = get_post_by_id(post_id)

            if not post:
                raise Exception("Post not found")

            title, desc, created = post

            body = f"""
            <html>
              <body>
                <a href="/">← Back</a>
                <h1>{title}</h1>
                <p>{desc}</p>
                <small>{created}</small>
              </body>
            </html>
            """

        except:
            body = "<h1>Post not found</h1>"

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(body.encode())}\r\n"
            "\r\n"
            + body
        )

        client_socket.sendall(response.encode())
        client_socket.close()
        continue


    # ---- CREATE POST ----
    if request.startswith("POST /create"):
        title, description = parse_post_data(request)
        if title and description:
            create_post(title, description)

        response = (
            "HTTP/1.1 302 Found\r\n"
            "Location: /\r\n"
            "\r\n"
        )
        client_socket.sendall(response.encode())
        client_socket.close()
        continue

    # ---- HOME PAGE ----
    posts = get_posts()
    posts_html = render_posts_html(posts)

    body = f"""
    <html>
      <body>
        <h1>Create Post</h1>

        <form method="POST" action="/create">
          <input type="text" name="title" placeholder="Title" required><br><br>
          <textarea name="description" placeholder="Description" required></textarea><br><br>
          <button type="submit">Create Post</button>
        </form>

        <hr>

        <h1>Posts</h1>
        {posts_html}
      </body>
    </html>
    """

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(body.encode())}\r\n"
        "\r\n"
        + body
    )

    client_socket.sendall(response.encode())
    client_socket.close()
