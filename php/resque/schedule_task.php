<?php

require 'vendor/autoload.php';

ResqueScheduler::enqueueIn(1, "test", 'Job', [
    'username' => 'dansackett'
]);

echo "Queued job";
