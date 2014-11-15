<?php

require 'vendor/autoload.php';

$settings = [
    'REDIS_BACKEND'     => '127.0.0.1:6379',    // Set Redis Backend Info
    'REDIS_BACKEND_DB'  => '0',                 // Use Redis DB 0
    'COUNT'             => '1',                 // Run 1 worker
    'INTERVAL'          => '5',                 // Run every 5 seconds
    'QUEUE'             => '*',                 // Look in all queues
    'PREFIX'            => 'test',               // Prefix queues with test
    'APP_INCLUDE'       => 'vendor/autoload.php'
];

foreach ($settings as $key => $value) {
    putenv(sprintf('%s=%s', $key, $value));
}
