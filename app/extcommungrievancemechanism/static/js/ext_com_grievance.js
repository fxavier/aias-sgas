document.addEventListener('DOMContentLoaded', function() {
    const complaintAccepted = document.querySelector('#id_complaintant_accepted');
    const actionTaken = document.querySelector('#id_action_taken');
    const actionTakenLabel = document.querySelector('label[for="id_action_taken"]');

    function toggleActionsTaken() {
        if (complaintAccepted.value === 'YES') {
            actionTaken.hidden = false;
            actionTakenLabel.hidden = false;
        } else {
            actionTaken.hidden = true;
            actionTakenLabel.hidden = true;
        }
    }

    // Initial check
    toggleActionsTaken();

    // Add event listener 
    complaintAccepted.addEventListener('change', toggleActionsTaken);
});

document.addEventListener('DOMContentLoaded', function() {
    const complaintNotified = document.querySelector('#id_complaintant_notified');
    const notifiedMethod = document.querySelector('#id_notification_method');

    function toggleNotifiedMethod() {
        if (complaintNotified.value === 'YES') {
            notifiedMethod.hidden = false;
        } else {
            notifiedMethod.hidden = true;
        }
    }

    // Initial check
    toggleNotifiedMethod();

    // Add event listener
    complaintNotified.addEventListener('change', toggleNotifiedMethod);
});

document.addEventListener('DOMContentLoaded', function() {
    const claimCategory = document.querySelector('#id_claim_category');
    const otherCategory = document.querySelector('#id_other_claim_category');

    function toggleOtherCategory() {
        if (claimCategory.value === 'Other') {
            otherCategory.hidden = false;
        } else {
            otherCategory.hidden = true;
        }
    }

    // Initial check
    toggleOtherCategory();

    // Add event listener
    claimCategory.addEventListener('change', toggleOtherCategory);
});
