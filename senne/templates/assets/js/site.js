// Figures open in one shared <dialog>. Without JavaScript the links simply open the image.
const viewer = document.getElementById("viewer");

if (viewer?.showModal) {
  const figure = viewer.querySelector("figure");
  const caption = viewer.querySelector("figcaption");

  document.addEventListener("click", (event) => {
    const link = event.target.closest("a[data-viewer]");
    // Modified clicks keep their browser meaning (new tab, new window).
    if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    const img = new Image();
    img.src = link.href;
    img.alt = link.dataset.viewer;
    figure.querySelector("img")?.remove();
    figure.prepend(img);
    caption.textContent = link.dataset.viewer;
    viewer.showModal();
  });

  // A click on the backdrop closes the viewer, like Esc and the button do.
  viewer.addEventListener("click", (event) => {
    if (event.target === viewer) viewer.close();
  });
}
