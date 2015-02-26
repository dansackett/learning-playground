/**
 * Basic Gulpfile for Compiling a React Application
 */
var browserify  = require('browserify');
var browserSync = require('browser-sync');
var gulp        = require('gulp');
var reactify    = require('reactify');
var source      = require("vinyl-source-stream");

// ----------------------------------------------------------------------------

/**
 * Browserify all the things
 */
gulp.task('browserify', function(){
    var b = browserify();
    b.transform(reactify);
    b.add('./src/js/main.js');

    return b.bundle()
            .pipe(source('main.js'))
            .pipe(gulp.dest('./dist/js'));
});

// ----------------------------------------------------------------------------

/**
 * Build initial brwoser-sync server
 */
gulp.task('browser-sync', function() {
    browserSync({
        server: {
            baseDir: "./"
        }
    });
});

// ----------------------------------------------------------------------------

/**
 * Default Task runs all tasks
 */
gulp.task('default', ['browserify', 'browser-sync']);

// ----------------------------------------------------------------------------

/**
 * Watcher task handles bundles on save
 */
gulp.task('watch', function() {
    gulp.watch('src/**/*.*', ['default', browserSync.reload]);
})
