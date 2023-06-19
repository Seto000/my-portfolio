$(document).ready(function() {
    $("form").on("submit", function(event) {
        event.preventDefault();

        var $form = $(this);
        var $errorAlert = $("#errorAlert");
        var $successAlert = $("#successAlert");

        $.ajax({
            data: $form.serialize(),
            type: "POST",
            url: "/"
        })
        .done(function(data) {
            if (data.error) {
                $errorAlert.html(data.error + '<button type="button" class="btn-close" aria-label="Close"></button>').show();
                $successAlert.hide();
            } else {
                $successAlert.html(data.success + '<button type="button" class="btn-close" aria-label="Close"></button>').show();
                $errorAlert.hide();
            }

            $form.trigger("reset");
        });
    });

    $(document).on("click", ".btn-close", function() {
        var $alert = $(this).closest(".alert");
        $alert.hide();
    });
});
