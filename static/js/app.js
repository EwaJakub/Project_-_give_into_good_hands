document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      console.log($stepForms)
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      // e.preventDefault();
      this.currentStep++;
      this.updateForm();
    }
  }
  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }

/**
 * Giving donation form
 *
 */

//const a = Array.from(document.querySelectorAll("input[name=categories]")).filter(function(input){return input.checked}).map(function(input){return input.value})
    const step1 = Array.from(document.querySelectorAll("div[data-step='2']"));
//const step1 = Array.from(document.querySelectorAll("div[data-step='1']"));
//const step3 = Array.from(document.querySelectorAll("div[data-step='3']"));
// const step4 = step3.from(document.querySelectorAll("div"));


  step1.forEach(function(element) {
      element.addEventListener('click', function(e) {
        if(e.target.tagName !== 'BUTTON' && array.length !== 0) return;
        let array = Array.from(document.querySelectorAll("input[name=categories]")).filter(function(input){return input.checked}).map(function(input){return input.value});
        console.log(array); // ['5']
        if (array.length === 0) {
          arrayNewLength = Array.from(document.querySelectorAll("input[name=categories]")).length
          console.log(array)
          for (let i = 1; i <= arrayNewLength; i ++) {
            array.push(i)
          }
        }
        const step3 = Array.from(document.querySelectorAll("div[data-step='3'] .form-group--checkbox"));
        // console.log(step3); // wyciągnięte checkboxy instytucji
        array.forEach(function(el) {
          // console.log(el) // 5 - iterowanie po elementach array
          step3.forEach(function(e) {
            // console.log(e)  // pojedynczy checkbox
            // console.log(e.dataset.categories) //1,2,
            const dataset_info = e.dataset.categories.split(",")
            //console.log(dataset_info)
            const newArray = dataset_info.filter(function(element) {
              return el === element
            });
            if (newArray.length === 0 && newArray.length < array.length) {
                  e.style.display = 'none'
                };
            });
        });
      });
  });
  });

/**
 * Giving donation form data
 *
 */

const step4 = Array.from(document.querySelectorAll("div[data-step='4']"));
  console.log(step4)


    step4.forEach(function(element) {
      element.addEventListener('click', function(e) {
        if (e.target.tagName !== 'BUTTON') return;
        const categories = Array.from(document.querySelectorAll("input[name=categories]")).filter(function(input){return input.checked}).map(function(input){return input.nextElementSibling.nextElementSibling.innerText }).join(', ');
          console.log(categories)
        const organization = Array.from(document.querySelectorAll("input[name=organization]")).filter(function(input){return input.checked}).map(function(input){return input.value}).join('')
          console.log(organization)
        const bags = document.querySelector("input[name=bags]").value
          console.log(bags)
        const address = document.querySelector("input[name=address]").value
          console.log(address)
        const city = document.querySelector("input[name=city]").value;
          console.log(city)
        const postcode = document.querySelector("input[name=postcode]").value;
          console.log(postcode)
        const phone = document.querySelector("input[name=phone]").value;
          console.log(phone)
        const data = document.querySelector("input[name=data]").value;
          console.log(data)
        const time = document.querySelector("input[name=time]").value;
          console.log(time)
        const more_info = document.querySelector("textarea[name=more_info]").value;
          console.log(more_info)
        const step5 = document.querySelector("div[data-step='5']");
        console.log(step5)
        const summaryText1 = step5.querySelector('span.icon-bag').nextElementSibling
        summaryText1.innerHTML = `${bags}  x worek z rzeczami w kategoriach:  ${categories}`
        console.log(summaryText1 )
        const summaryText2 = step5.querySelector('span.icon-hand').nextElementSibling
        summaryText2.innerHTML = `Dla fundacji:  ${organization}`
        console.log(summaryText1 )
        const column1 = step5.querySelector('.form-section--columns').firstElementChild.lastElementChild.children
        console.log(column1)
        column1[0].innerHTML = address
        column1[1].innerHTML = city
        column1[2].innerHTML = postcode
        column1[3].innerHTML = phone
        const column2 = step5.querySelector('.form-section--columns').lastElementChild.lastElementChild.children
        console.log(column1)
        column2[0].innerHTML = data
        column2[1].innerHTML = time
        column2[2].innerHTML = more_info
      }) });