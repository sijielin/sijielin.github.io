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
  <img id="slide" src="{{ '/files/what_is_sref/Slide1.JPG' | relative_url }}" alt="Slide image" style="max-width:100%; height:auto;">
  <br>
  <button id="prevBtn">⟵ Prev</button>
  <button id="nextBtn">Next ⟶</button>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const slides = [
      "{{ '/files/what_is_sref/Slide1.JPG' | relative_url }}",
      "{{ '/files/what_is_sref/Slide2.JPG' | relative_url }}",
      "{{ '/files/what_is_sref/Slide3.JPG' | relative_url }}"
    ];

    console.log("Slides array:", slides); // 👈 Check this in console
    
    let current = 0;

    function showSlide() {
      console.log("Showing slide:", current, slides[current]); // 👈 Add this
      document.getElementById("slide").src = slides[current];
    }

    document.getElementById("nextBtn").addEventListener("click", function () {
      console.log("Next button clicked"); // 👈 Check if this appears
      current = (current + 1) % slides.length;
      showSlide();
    });

    document.getElementById("prevBtn").addEventListener("click", function () {
      console.log("Prev button clicked"); // 👈 Check if this appears
      current = (current - 1 + slides.length) % slides.length;
      showSlide();
    });

    showSlide();
  });
</script>
