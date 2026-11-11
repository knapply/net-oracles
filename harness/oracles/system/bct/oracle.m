% Brain Connectivity Toolbox (Rubinov and Sporns 2010) oracle driver for GNU
% Octave: reads the fixture corpus and writes golden files. Black-box use.
%   octave --no-gui --quiet oracle.m  (env: FIXTURES, OUT, BCT)
1;
% BCT's charpath calls nanmax from Octave Forge's statistics package, which
% is not installed; Octave's max already skips NaN, so max is the same call.
function varargout = nanmax(varargin)
  [varargout{1:max(nargout, 1)}] = max(varargin{:});
end
function varargout = nanmin(varargin)
  [varargout{1:max(nargout, 1)}] = min(varargin{:});
end
function r = diam(A, which)
  D = distance_bin(A);
  [~, ~, ecc, rad, dia] = charpath(D, 0, 0);
  switch which
    case 3, r = ecc; case 4, r = rad; case 5, r = dia;
  end
end

fixtures = getenv('FIXTURES'); out = getenv('OUT'); addpath(genpath(getenv('BCT')));
NANV = -999; INFV = -1000;
system(['mkdir -p ' out]);
errf = fopen(fullfile(out, 'ERRORS.tsv'), 'w'); fprintf(errf, 'fixture\tvariant\terror\n');
d = dir(fixtures); names = {};
for i = 1:numel(d)
  if d(i).isdir && d(i).name(1) ~= '.' && exist(fullfile(fixtures, d(i).name, 'meta.json'), 'file')
    names{end+1} = d(i).name;
  end
end
names = sort(names);
for k = 1:numel(names)
  nm = names{k};
  meta = fileread(fullfile(fixtures, nm, 'meta.json'));
  n = str2double(regexp(meta, '"n":\s*(\d+)', 'tokens'){1}{1});
  directed = strcmp(regexp(meta, '"directed":\s*(true|false)', 'tokens'){1}{1}, 'true');
  weighted = strcmp(regexp(meta, '"weighted":\s*(true|false)', 'tokens'){1}{1}, 'true');
  lines = strsplit(strtrim(fileread(fullfile(fixtures, nm, 'edges.csv'))), "\n");
  A = zeros(n); W = inf(n);
  for i = 2:numel(lines)
    p = strsplit(strtrim(lines{i}), ',');
    a = str2double(p{1}) + 1; b = str2double(p{2}) + 1;
    w = 1; if weighted, w = str2double(p{3}); end
    if a == b, continue; end   % a matrix input carries neither loops nor parallel edges here
    A(a, b) = 1; W(a, b) = min(W(a, b), w);
    if ~directed, A(b, a) = 1; W(b, a) = min(W(b, a), w); end
  end
  L = W; L(isinf(L)) = 0;
  fx = struct('name', nm, 'out', out);
  D = [];
  jobs = {};
  % variant name, function handle returning a matrix/vector/scalar
  if ~directed
    jobs = [jobs; {'degree_all_noloops', @() degrees_und(A)'}];
    jobs = [jobs; {'clustering_zero', @() clustering_coef_bu(A)}];
    jobs = [jobs; {'average_clustering_zero', @() mean(clustering_coef_bu(A))}];
    jobs = [jobs; {'transitivity', @() transitivity_bu(A)}];
    jobs = [jobs; {'coreness_all', @() kcoreness_centrality_bu(A)'}];
    jobs = [jobs; {'dm_local_efficiency', @() mean(efficiency_bin(A, 1))}];
    jobs = [jobs; {'assortativity_degree', @() assortativity_bin(A, 0)}];
    jobs = [jobs; {'density_simple', @() density_und(A)}];
  else
    jobs = [jobs; {'degree_out', @() sum(A, 2)'}];
    jobs = [jobs; {'degree_in', @() sum(A, 1)}];
    jobs = [jobs; {'degree_all_noloops', @() (sum(A, 2)' + sum(A, 1))}];
    jobs = [jobs; {'clustering_zero', @() clustering_coef_bd(A)}];
    jobs = [jobs; {'average_clustering_zero', @() mean(clustering_coef_bd(A))}];
    jobs = [jobs; {'transitivity', @() transitivity_bd(A)}];
    jobs = [jobs; {'assortativity_degree', @() assortativity_bin(A, 1)}];
    jobs = [jobs; {'density_simple', @() density_dir(A)}];
  end
  jobs = [jobs; {'betweenness', @() betweenness_bin(A)'}];
  if weighted, jobs = [jobs; {'betweenness_weighted', @() betweenness_wei(L)'}]; end
  jobs = [jobs; {'dm_global_efficiency', @() efficiency_bin(A)}];
  jobs = [jobs; {'distances', @() distance_bin(A)}];
  jobs = [jobs; {'diameter', @() diam(A, 5)}];
  jobs = [jobs; {'radius', @() diam(A, 4)}];
  jobs = [jobs; {'eccentricity', @() diam(A, 3)'}];
  for j = 1:size(jobs, 1)
    v = jobs{j, 1};
    try
      r = jobs{j, 2}();
      r(isnan(r)) = NANV; r(isinf(r)) = INFV;
      if strcmp(v, 'distances'), r(1:n+1:end) = 0; end
      fs = fullfile(out, nm); system(['mkdir -p ' fs]);
      fid = fopen(fullfile(fs, [v '.csv']), 'w'); fprintf(fid, 'value\n');
      if isvector(r) || isscalar(r)
        fprintf(fid, '%.17g\n', r(:));
      else
        for i = 1:size(r, 1), fprintf(fid, '%s\n', strjoin(arrayfun(@(x) sprintf('%.17g', x), r(i, :), 'UniformOutput', false), ' ')); end
      end
      fclose(fid);
    catch err
      fprintf(errf, '%s\t%s\t%s\n', nm, v, strrep(err.message, "\n", ' '));
    end
  end
end
fclose(errf);
printf('Octave %s, BCT %s\n', version(), getenv('BCT_RELEASE'));

