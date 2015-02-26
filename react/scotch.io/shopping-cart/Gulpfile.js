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
    b.add('./src/js/app.js');

    return b.bundle()
            .pipe(source('app.js'))
            .pipe(gulp.dest('./dist/js'));
});

// ----------------------------------------------------------------------------

/**
 * Move CSS
 */
gulp.task('css', function(){
    return gulp.src('./src/css/app.css').pipe(gulp.dest('./dist/css'));
});

// ----------------------------------------------------------------------------

/**
 * Move Images
 */
gulp.task('images', function(){
    return gulp.src('./src/img/*').pipe(gulp.dest('./dist/img'));
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
gulp.task('default', ['browserify', 'browser-sync', 'css', 'images']);

// ----------------------------------------------------------------------------

/**
 * Watcher task handles bundles on save
 */
gulp.task('watch', function() {
    gulp.watch('src/**/*.*', ['default', browserSync.reload]);
})
