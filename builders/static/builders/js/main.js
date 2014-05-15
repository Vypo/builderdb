$(function () {
    // Activate the raty widget
    $('[data-raty]').raty({
        numberMax: 5,
        path: '/static/builders/vendor/raty/img',
        score: function() {
            return $(this).attr('data-raty-score');
        },
        readOnly: function() {
            return !$(this).is('[data-raty-rw]');
        },
        hints: [null] * 5
    });
});
