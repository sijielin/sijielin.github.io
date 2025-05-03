---
permalink: /
title: ""
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<style>
.profile-container {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  gap: 40px;
  margin: 40px auto;
  max-width: 1400px;
  flex-wrap: nowrap;
}

/* Profile image column */
.profile-image-block {
  max-width: 320px;
  flex-shrink: 0;
  position: relative;
}

/* Main and hover image logic */
.profile-image-block img {
  width: 100%;
  height: auto;
  border-radius: 4px;
  transition: opacity 0.4s ease;
  display: block;
}

.profile-image-block .hover-image {
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
}

.profile-image-block:hover .hover-image {
  opacity: 1;
}

.profile-image-block:hover .main-image {
  opacity: 0;
}

/* Text column */
.profile-text-block {
  max-width: 1000px;
  font-size: 18px;
  flex: 1;
}

.profile-text-block h1 {
  margin-top: 0;
  color: #011f5b;
  font-size: 24px;
}

.profile-text-block a {
  color: #1a0dab;
  text-decoration: none;
}

/* Responsive behavior for small screens */
@media (max-width: 768px) {
  .profile-container {
    flex-direction: column;
    align-items: center;
    text-align: left;
  }

  .profile-text-block {
    max-width: 100%;
  }
}
</style>

<div class="profile-container">
  <div class="profile-image-block">
    <img src="images/photo.jpg" class="main-image" alt="Profile Image">
    <img src="images/ghibli_new.png" class="hover-image" alt="Hover Image">
  </div>

  <div class="profile-text-block">
    <h1>Sijie Lin</h1>
    <p>Welcome! I'm Sijie Lin (林思捷), a Ph.D. Candidate in Economics at Rotman School of Management, University of Toronto. My research focuses on the impact of generative AI on creative industries.</p>

    <p><strong>Research Interests:</strong> Industrial Organization, Artificial Intelligence, Innovation, Intellectual Property Rights</p>

    <p><strong>Committee:</strong> 
      <a href="https://matthewmitchelltoronto.weebly.com">Matthew Mitchell</a>, 
      <a href="https://sites.google.com/site/heskibarisaac">Heski Bar-Isaac</a>, 
      <a href="https://www.avigoldfarb.com">Avi Goldfarb</a>, 
      <a href="https://discover.research.utoronto.ca/23819-ambarish-chandra">Ambarish Chandra</a>
    </p>

    <p><strong>Email:</strong> <a href="mailto:sijie.lin@mail.utoronto.ca">sijie.lin@mail.utoronto.ca</a><br>
    <strong>Address:</strong> 105 St George Street, Toronto, ON, Canada</p>
  </div>
</div>


