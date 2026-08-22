// ========================================
// THE WATCHER - APP.JS
// General UI functionality
// ========================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("The Watcher frontend loaded successfully.");

    // ----------------------------------------
    // SIDEBAR NAVIGATION
    // ----------------------------------------

    const navItems = document.querySelectorAll(".nav-item");

    navItems.forEach((item) => {

        item.addEventListener("click", (event) => {

            event.preventDefault();

            navItems.forEach((nav) => {
                nav.classList.remove("active");
            });

            item.classList.add("active");

            const pageName = item.innerText.trim();

            console.log("Selected:", pageName);
        });

    });


    // ----------------------------------------
    // NOTIFICATION BUTTON
    // ----------------------------------------

    const notificationButton =
        document.querySelector(".notification-btn");

    if (notificationButton) {

        notificationButton.addEventListener("click", () => {

            alert("You have 3 new monitoring updates.");

        });

    }


    // ----------------------------------------
    // ADD COMPETITOR BUTTON
    // ----------------------------------------

    const addCompetitorButton =
        document.querySelector(".primary-btn");

    if (addCompetitorButton) {

        addCompetitorButton.addEventListener("click", () => {

            openCompetitorModal();

        });

    }


    // ----------------------------------------
    // VIEW BUTTONS
    // ----------------------------------------

    const viewButtons =
        document.querySelectorAll(".view-btn");

    viewButtons.forEach((button) => {

        button.addEventListener("click", () => {

            const competitor =
                button
                    .closest(".competitor")
                    .querySelector("h3")
                    .innerText;

            alert(`Opening details for ${competitor}`);

        });

    });


    // ----------------------------------------
    // VIEW FULL INSIGHT
    // ----------------------------------------

    const insightButton =
        document.querySelector(".secondary-btn");

    if (insightButton) {

        insightButton.addEventListener("click", () => {

            alert(
                "AI Insight:\n\n" +
                "A significant pricing change was detected. " +
                "The competitor reduced the product price by approximately 12%."
            );

        });

    }


    // ----------------------------------------
    // VIEW ALL CHANGES
    // ----------------------------------------

    const viewAllButton =
        document.querySelector(".text-btn");

    if (viewAllButton) {

        viewAllButton.addEventListener("click", () => {

            alert("Opening all detected changes...");

        });

    }

});


// ========================================
// ADD COMPETITOR MODAL
// ========================================

function openCompetitorModal() {

    // Prevent duplicate modal
    if (document.querySelector(".modal-overlay")) {
        return;
    }


    const modalHTML = `

        <div class="modal-overlay">

            <div class="competitor-modal">

                <button class="modal-close">
                    ×
                </button>

                <div class="modal-icon">
                    👁
                </div>

                <h2>Add Competitor</h2>

                <p class="modal-description">
                    Enter a website URL that you want
                    The Watcher to monitor.
                </p>


                <label for="competitor-url">
                    Website URL
                </label>

                <input
                    type="url"
                    id="competitor-url"
                    placeholder="https://example.com"
                />


                <label for="monitor-frequency">
                    Monitoring Frequency
                </label>

                <select id="monitor-frequency">

                    <option value="1h">
                        Every 1 hour
                    </option>

                    <option value="6h">
                        Every 6 hours
                    </option>

                    <option value="12h">
                        Every 12 hours
                    </option>

                    <option value="24h">
                        Every 24 hours
                    </option>

                </select>


                <button class="start-monitoring-btn">
                    Start Watching
                </button>

            </div>

        </div>

    `;


    document.body.insertAdjacentHTML(
        "beforeend",
        modalHTML
    );


    // Close modal

    const closeButton =
        document.querySelector(".modal-close");

    closeButton.addEventListener("click", closeCompetitorModal);


    // Close when clicking outside modal

    const overlay =
        document.querySelector(".modal-overlay");

    overlay.addEventListener("click", (event) => {

        if (event.target === overlay) {
            closeCompetitorModal();
        }

    });


    // Start monitoring button

    const startButton =
        document.querySelector(".start-monitoring-btn");

    startButton.addEventListener("click", () => {

        const url =
            document.querySelector("#competitor-url").value.trim();

        const frequency =
            document.querySelector("#monitor-frequency").value;


        if (!url) {

            alert("Please enter a website URL.");

            return;

        }


        alert(
            `Monitoring started!\n\n` +
            `Website: ${url}\n` +
            `Frequency: ${frequency}`
        );


        closeCompetitorModal();

    });

}


function closeCompetitorModal() {

    const modal =
        document.querySelector(".modal-overlay");

    if (modal) {
        modal.remove();
    }

}