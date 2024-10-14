require "bundler/gem_tasks"
require "jekyll"
require "listen"
require "parallel"
require "uglifier"
require "rake"

def listen_ignore_paths(base, options)
  [
    /_config\.ya?ml/,
    /_site/,
    /\.jekyll-metadata/
  ]
end

def listen_handler(base, options)
  site = Jekyll::Site.new(options)
  Jekyll::Command.process_site(site)
  proc do |modified, added, removed|
    t = Time.now
    c = modified + added + removed
    n = c.length
    relative_paths = c.map{ |p| Pathname.new(p).relative_path_from(base).to_s }
    print Jekyll.logger.message("Regenerating:", "#{relative_paths.join(", ")} changed... ")
    begin
      Jekyll::Command.process_site(site)
      puts "regenerated in #{Time.now - t} seconds."
    rescue => e
      puts "error:"
      Jekyll.logger.warn "Error:", e.message
      Jekyll.logger.warn "Error:", "Run jekyll build --trace for more information."
    end
  end
end

task :preview do
  base = Pathname.new('.').expand_path
  options = {
    "source"        => base.join('test').to_s,
    "destination"   => base.join('test/_site').to_s,
    "force_polling" => false,
    "serving"       => true,
    "theme"         => "minimal-mistakes-jekyll"
  }

  options = Jekyll.configuration(options)

  ENV["LISTEN_GEM_DEBUGGING"] = "1"
  listener = Listen.to(
    base.join("_data"),
    base.join("_includes"),
    base.join("_layouts"),
    base.join("_sass"),
    base.join("assets"),
    options["source"],
    :ignore => listen_ignore_paths(base, options),
    :force_polling => options['force_polling'],
    &(listen_handler(base, options))
  )

  begin
    listener.start
    Jekyll.logger.info "Auto-regeneration:", "enabled for '#{options["source"]}'"

    unless options['serving']
      trap("INT") do
        listener.stop
        puts "     Halting auto-regeneration."
        exit 0
      end

      loop { sleep 1000 }
    end
  rescue ThreadError
    # You pressed Ctrl-C, oh my!
  end

  Jekyll::Commands::Serve.process(options)
end

desc "Build the Jekyll site"
task :build do
  sh "bundle exec jekyll build"
end

desc "Compile Sass to CSS"
task :css do
  sh "sass --update _sass:assets/css"
end

desc "Minify JavaScript"
task :js do
  input_file = "assets/js/main.js"
  output_file = "assets/js/main.min.js"
  content = File.read(input_file)
  minified_content = Uglifier.new.compile(content)
  File.open(output_file, "w") { |file| file.write(minified_content) }
end

desc "Build site in parallel"
task :parallel_build do
  Parallel.each([:build, :css, :js], in_threads: 3) do |task|
    Rake::Task[task].invoke
  end
end

task default: [:parallel_build]
