---
permalink: /misc/
title: "Miscellaneous"
author_profile: false
---

## Public Goods

- [Keith Head's advice for empirical papers](https://blogs.ubc.ca/khead/research/research-advice)
- [Virtual digital economy seminar](https://www.digitalecon.org/seminar)

## Interesting Things about AI Arts
- [Can people tell the difference between AI arts and human arts?](https://www.astralcodexten.com/p/how-did-you-do-on-the-ai-art-turing)
- [Karla Ortiz's blog: Why AI Models are not inspired like humans](https://www.kortizblog.com/blog/why-ai-models-are-not-inspired-like-humans)
- [Thousands of creators have signed the Statement on AI Training](https://authorsguild.org/news/sign-the-statement-on-ai-training/)
- [A roboticist/skier/triathlete who inspired my AI art researches](https://aliciachenw.github.io/)
- **Guess who draws the Pikachu!**


<div class="slider" style="text-align: center;">
  <img id="slideImg" src="https://sijielin.github.io/files/what_is_sref/Slide1.JPG" alt="Slide 1" style="max-width: 100%; height: auto;" />
  <div style="margin-top: 10px;">
    <button onclick="prevSlide()">⟵ Prev</button>
    <button onclick="nextSlide()">Next ⟶</button>
  </div>
</div>

<script>
  /* JavaScript Slider Code - wrapped in block comments to avoid // issues */
  let slideIndex = 0;
  const slides = [
    "https://sijielin.github.io/files/what_is_sref/Slide1.JPG",
    "https://sijielin.github.io/files/what_is_sref/Slide2.JPG",
    "https://sijielin.github.io/files/what_is_sref/Slide3.JPG"
  ];

  function showSlide(index) {
    const img = document.getElementById("slideImg");
    if (index < 0) slideIndex = slides.length - 1;
    else if (index >= slides.length) slideIndex = 0;
    else slideIndex = index;
    img.src = slides[slideIndex];
  }

  function nextSlide() {
    showSlide(slideIndex + 1);
  }

  function prevSlide() {
    showSlide(slideIndex - 1);
  }

  // Initial display
  showSlide(slideIndex);
</script>

