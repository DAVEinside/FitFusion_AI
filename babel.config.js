module.exports = function(api) {
    api.cache(true);
    const presets = ['react-app'];
    const plugins = ['@babel/plugin-transform-private-property-in-object'];
  
    return {
      presets,
      plugins
    };
  };
  