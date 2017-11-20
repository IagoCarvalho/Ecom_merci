// Importando plugins
var gulp = require('gulp');
var plugin = require('gulp-plugin');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var concat = require('gulp-concat');
var autoReload = require('gulp-auto-reload');
var uglify = require('gulp-uglify');
var pump = require('pump');
const del = require('del');
var gutil = require('gulp-util');
var nano = require('gulp-cssnano');

// Default
gulp.task('default', ['sass', 'watch']);

// Caminhos para fazer a build
var paths = {
  html: "Ecom_merci/**/*.html",
  css: "Ecom_merci/**/*.css"
};

// Task pra pre compilar SASS
gulp.task('sass', function() {
return gulp.src('static/**/*.scss')
.pipe(sass())
.pipe(gulp.dest('static/css'))
})

// logs
gulp.task('css-log', function(){
	console.log('CSS modified!');
});

gulp.task('js-log', function(){
	console.log('JS modified!');
});

gulp.task('html-log', function(){
	console.log('HTML modified!');
});

// Vigiar arquivos
gulp.task('watch', function() {
	gulp.watch('Ecom_merci/**/*.css', ['css-log']);
	gulp.watch('Ecom_merci/**/*.js', ['js-log']);
	gulp.watch('Ecom_merci/*.html', ['html-log']);
});

gulp.task('build', ['sass', 'watch'], function() {
});
