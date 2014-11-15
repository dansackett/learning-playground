<?php

require 'vendor/autoload.php';

$id = Resque::enqueue('test', 'Job', [
    'username' => 'dansackett'
], true);

echo 'Queued job ' . $id;
