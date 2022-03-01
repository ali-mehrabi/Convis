Changelog
==========

See also the more complete changelog [in the documentation](https://jahuth.github.io/convis/changelog.html).


Version 0.6.4 (release pending) and current github version
-----------------------------------------------------------

  - fixed bug in convolution filter alignment in `Conv2d` and `Conv3d`: odd sized filters are now centered correctly
  - fixed two bugs in `LeakyIntegrateAndFireNeuron` and `RefractoryLeakyIntegrateAndFireNeuron`:
      + The default time step from `convis.default_resolution` was not copied to the internal variable `tau`. Now layers will use the value from the time of their creation.
      + The input was not normalized with the step size, leading to different results when changing the resolution and leak simultaneously.
 - added `flip` argument (default: True) to `Conv3d.set_weight` to keep the filter and impulse response aligned.
 - fixed bug in plot_impulse (impulse was too long due to padding)
 - added Difference Layer `convis.filters.Diff`
 - added spiking layers `convis.filters.spiking.Poisson` and `convis.filters.spiking.IntegrativeMotionSensor`, which is a DVS like Layer
 - added `convis.streams.ProcessingStream` and `convis.streams.MNISTStream` (and neuromorphic versions: `PoissonMNISTStream` and `PseudoNMNIST`)
 - fixed bug in variable describe
 - added usage docs about inputs and outputs


Version 0.6.3
--------------

 - GanglionSpiking had a bug in the refractory period
 - the different implementations of OPL Layers now produce roughly the same output
 - FullConvolutionOPLFilter now creates a filter from configuration options
 - `Layer.run()` now always returns an `Output` object
     + fixed a bug where it returned an `Output` object wrapped in a `Output` object
 - `Layer.run()` can now process infinite streams if it gets an argument `max_t`
 - added warnings to `convis.streams` classes that are unstable
 - fixed `convis.streams.ImageSequence`
 - `utils.plot_tensor` is now available as `convis.plot_tensor` 

Version 0.6.2
--------------

A small amount of bug fixes:

 - Fixed a bug in `convis.filters.retina.GanglionInput`:
    - the convolution filters now initialize without having to reapply a configuration to the layer/parameters
 - made padding flags in `convis.filters.Conv3d` default to True
    - in contrast to PyTorch `Conv3d` the output will now have the same shape as the input *by default*. To disable, use `time_pad=False` and `autopad=False` as arguments.
 - fixed a bug when calling `.array()` on `convis.base.Output`s.
 - fixed a bug where `resolution` was not a valid argument to `convis.filters.Conv3d.gaussian`

Version 0.6.1
---------------

 - It is now possible to disable the computational graph.
 - some issues with creating inline plots in Python 3 were fixed

Version 0.6
-----------

 - fixed compatibility with PyTorch 0.4.0
    + `convis` is now compatible with PyTorch <= 0.3 and PyTorch 0.4.0
 - VirtualParameters are now also included in the `named_parameter` dictionary and also appear in the `model.p.<tab>` parameter list.
 - the `variables` submodule now offers the functions `zeros`, `zeros_like`, `ones`, `rand` and `randn` which give a autograd.Variable or a Tensor, depending on PyTorch version.