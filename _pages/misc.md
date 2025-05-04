---
permalink: /misc/
title: "Miscellaneous"
author_profile: false
---

## Public Goods

- [Advice for empirical papers](https://blogs.ubc.ca/khead/research/research-advice)

## Interesting Things about AI Arts

- [Guess who draws the Pikachu!](https://sijielin.github.io/files/what_is_sref.pdf)
- [Can people tell the difference between AI arts and human arts?](https://www.astralcodexten.com/p/how-did-you-do-on-the-ai-art-turing)
- [Karla Ortiz's blog: Why AI Models are not inspired like humans](https://www.kortizblog.com/blog/why-ai-models-are-not-inspired-like-humans)
- [Thousands of creators have signed the Statement on AI Training](https://authorsguild.org/news/sign-the-statement-on-ai-training/)


<div style="text-align:center">
  <img id="slide" src="{{ '/files/what_is_sref/Slide1.JPG' | relative_url }}" style="max-width:100%; height:auto;">
  <br>
  <button onclick="prevSlide()">⟵ Prev</button>
  <button onclick="nextSlide()">Next ⟶</button>
</div>

<script>
  const slides = [
    "/files/what_is_sref/Slide1.JPG",
    "/files/what_is_sref/Slide2.JPG",
    "/files/what_is_sref/Slide3.JPG"
    // Add more if needed
  ];

  let current = 0;

  function showSlide() {
    document.getElementById("slide").src = slides[current];
  }

  function nextSlide() {
    current = (current + 1) % slides.length;
    showSlide();
  }

  function prevSlide() {
    current = (current - 1 + slides.length) % slides.length;
    showSlide();
  }

  // Optional: show correct image on load
  window.onload = showSlide;
</script>
