document.addEventListener('DOMContentLoaded', function() {
    const responseField = document.querySelector('#id_response');
    const recommendedActionsField = document.querySelector('#id_recomended_actions');

    function toggleRecommendedActions() {
        if (responseField.value === 'SIM') {
            recommendedActionsField.hidden = false;
        } else {
            recommendedActionsField.hidden = true;
        }
    }

    // Initial check
    toggleRecommendedActions();

    // Add event listener
    responseField.addEventListener('change', toggleRecommendedActions);
});
