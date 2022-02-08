# 0207_workshop

 ## 1.

```python
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="style.css" />
    <title>Document</title>
  </head>
  <body>
    <!-- 1. Nav -->
    <nav class="fixed-top bg-dark bg-gradient d-flex justify-content-between">
      <a href="#">
        <img src="images/logo.png" alt="Logo Image" />
      </a>
      <ul class="nav justify-content-center align-items-center">
        <li class="nav-item mx-3">
          <a class="text-decoration-none text-white" href="#">Home</a>
        </li>
        <li class="nav-item mx-3">
          <a class="text-decoration-none text-white" href="#">Community</a>
        </li>
        <li class="nav-item mx-3">
          <a class="text-decoration-none text-white" href="#">Login</a>
        </li>
      </ul>
    </nav>

    <!-- 2. Header -->
    <header
      class="d-flex fw-bold flex-column justify-content-center align-items-center text-white"
    >
      <div class="display-1">Cinema</div>
      <br />
      <div class="display-1">Community</div>
      <div>
        <a type="button" class="btn btn-primary mt-5" href="#">Let's Go</a>
      </div>
    </header>

    <!-- 3. Section -->
    <section class="d-flex flex-column justify-content-between">
      <h2 class="row mx-auto col-3 d-flex justify-content-center my-5">
        Used Skills
      </h2>
      <article
        class="my-5 col-12 d-flex justify-content-evenly align-items-center"
      >
        <div class="d-flex flex-column justify-content-evenly">
          <img src="images/web.png" alt="Web Image" />
          <!-- p에 flexbox 줘도 내부 텍스트 정렬이 된다. -->
          <p class="d-flex justify-content-center">Web</p>
        </div>
        <div>
          <img src="images/html5.png" alt="HTML5 Image" />
          <p class="d-flex justify-content-center">HTML5</p>
        </div>
        <div>
          <img src="images/css3.png" alt="CSS3 Image" />
          <p class="d-flex justify-content-center">CSS3</p>
        </div>
      </article>
    </section>

    <!-- 4. Footer -->
    <footer
      class="fixed-bottom text-white bg-primary d-flex justify-content-center align-items-center"
    >
      <p class="m-0">HTML & CSS project. Created by Marco</p>
    </footer>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"
      integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13"
      crossorigin="anonymous"
    ></script>
  </body>
</html>

```